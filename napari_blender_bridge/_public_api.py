
class _StaticMemory:
    """
    This class serves as some kind of global memory to store things during runtime.
    """
    port = 8080
    temp_folders = []

def start_blender(blender_path="C:/Program Files/Blender Foundation/Blender 3.5/", port=8080):
    """
    This function starts up Blender and runs a script inside
    that listens on an TCP/IP port for commands.
    """
    import subprocess
    import os

    path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/")
    _StaticMemory.port = port

    subprocess.Popen(f'"{blender_path}blender" --python {path}/_blender_server.py -- {port}', shell=True)


def disconnect():
    """
    Close the connection on Blender side. It cannot be restarted without restarting Blender.
    """
    _send_command("disconnect", port=_StaticMemory.port)


def open_ply(filename):
    """
    Make Blender open a PLY file.
    """
    _send_command("open_ply " + filename, port=_StaticMemory.port)


def save_ply(filename):
    """
    Make Blender save the current scene as a PLY file.
    """
    _send_command("save_ply " + filename, port=_StaticMemory.port)


def save_stl(filename):
    """
    Make Blender save the current scene as a STL file.
    """
    _send_command("save_stl " + filename, port=_StaticMemory.port)


def _send_command(command: str = '', host: str = 'localhost', port: int = 8080):
    """
    Send a command to Blender. For supported commands, see _blender_server.py
    """
    import socket

    BUFFER_MAX_SIZE = 4096

    # connect
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # send request
    client_socket.sendall(command.encode("utf-8"))

    # receive response
    response = client_socket.recv(BUFFER_MAX_SIZE)

    # close connection
    client_socket.close()

    return response


def _make_temp_dir():
    """
    Create a temporary directory
    """
    import tempfile
    temp_folder = tempfile.TemporaryDirectory(prefix="napari-blender-bridge")
    import os
    temp_dir = temp_folder.name.replace("\\", "/")
    if not os.path.isdir(temp_dir):
        os.mkdir(temp_dir)
    if not temp_dir.endswith("/"):
        temp_dir = temp_dir + "/"

    _StaticMemory.temp_folders.append(temp_folder)

    return temp_dir