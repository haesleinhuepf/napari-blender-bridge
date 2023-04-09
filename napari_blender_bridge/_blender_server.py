# This is a script that is executed from within Blender.
# It will most likely not work in your conda environment.
#
# Inspired by:
# https://blender.stackexchange.com/questions/41533/how-to-remotely-run-a-python-script-in-an-existing-blender-instance
# https://devtalk.blender.org/t/multithreading-support-please/13038/18

import bpy
import threading
import queue
from functools import partial

import sys
argv = sys.argv

PORT = int(argv[-1])
HOST = "localhost"
PATH_MAX = 4096
execution_queue = queue.Queue()


def parse_command(command):
    """
    Executes a command such as opening or saving a mesh.
    """
    print("Executing:", command)
    if command.startswith("open_ply "):
        filename = command[9:]
        bpy.ops.import_mesh.ply(filepath=filename)
    elif command.startswith("save_ply "):
        filename = command[9:]
        bpy.ops.export_mesh.ply(filepath=filename)
        # save a .txt file as signal for the other side that PLY file writing is done
        with open(filename + '.txt', 'w') as f:
            f.write('done')
    elif command.startswith("save_stl "):
        filename = command[9:]
        bpy.ops.export_mesh.stl(filepath=filename)
        # save a .txt file as signal for the other side that STL file writing is done
        with open(filename + '.txt', 'w') as f:
            f.write('done')
    else:
        print(f"command '{command}' not understood")
    return True


def heartbeat():
    """
    This function runs a loop that listens to a TCP/IP port for messages.
    Once a message arrives, it stores a function processing the message in
    the global command queue.
    """
    import socket
    from datetime import datetime

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Listening on %s:%s" % (HOST, PORT))
    while True:
        print("still listening")
        connection, address = server_socket.accept()
        command = connection.recv(PATH_MAX)

        if command:
            command = command.decode('utf-8')
            if command == 'disconnect':
                print("disconnecting, leaving blender alive")
                execution_queue.put(partial(quit))
                break
            else:
                execution_queue.put(partial(parse_command, command))
                #global_command = command
                    
        connection.sendall(str(datetime.now()).encode("utf-8"))
        
    server_socket.close()

def breathing():
    """
    This function is executed once in a while checking if there are commands
    in the queue that should be executed. If so, it runs those.
    """
    print("breathing")
    while not execution_queue.empty():
        function = execution_queue.get()
        function()
    return 1.0

# Register breathing timer
bpy.app.timers.register(breathing)

# Start heartbeat thread
thread = threading.Thread(target=heartbeat, name="Heartbeat", args=[])
thread.start()

print("done")

