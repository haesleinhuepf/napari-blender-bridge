import warnings

from napari_plugin_engine import napari_hook_implementation
from napari_tools_menu import register_function, register_action


@napari_hook_implementation
def napari_experimental_provide_function():
    return []


@register_function(menu="Blender > Start up Blender")
def start_blender(blender_path="C:/Program Files/Blender Foundation/Blender 3.5/", port:int = 8080):
    from ._public_api import start_blender
    start_blender(blender_path=blender_path, port=port)


@register_action(menu="Blender > Shut down Blender")
def shut_down_blender(viewer:"napari.Viewer"):
    from ._public_api import disconnect
    disconnect()


@register_function(menu="Blender > Send Surface mesh to Blender")
def send_surface_to_blender(surface:"napari.types.SurfaceData"):
    import vedo
    import napari_process_points_and_surfaces as nppas
    from ._public_api import _make_temp_dir, open_ply

    mesh = nppas.to_vedo_mesh(surface)

    filename = _make_temp_dir() + "temp.ply"

    vedo.write(mesh, filename)

    open_ply(filename)



@register_action(menu="Blender > Retrieve all meshes from Blender")
def retrieve_all_meshes_from_blender(viewer:"napari.Viewer"):
    import vedo
    import napari_process_points_and_surfaces as nppas
    from ._public_api import _make_temp_dir, save_stl
    from time import sleep
    import os.path

    filename = _make_temp_dir() + "temp.stl"
    save_stl(filename)

    timeout_in_sec = 60
    counter = 0
    # we're checking if the correspondig .txt file exists, because
    # this one is written after the STL file writing is done.
    while not os.path.isfile(filename + ".txt"):
        sleep(1)
        counter += 1
        if counter > timeout_in_sec:
            warnings.warn("Could not retrieve scene from Blender.")
            return

    new_mesh = vedo.load(filename)
    new_surface = nppas.to_napari_surface_data(new_mesh)
    viewer.add_surface(new_surface)

