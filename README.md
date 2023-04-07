# napari-blender-bridge

[![License](https://img.shields.io/pypi/l/napari-blender-bridge.svg?color=green)](https://github.com/haesleinhuepf/napari-blender-bridge/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-blender-bridge.svg?color=green)](https://pypi.org/project/napari-blender-bridge)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-blender-bridge.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/napari-blender-bridge/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-blender-bridge/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/napari-blender-bridge/branch/master/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/napari-blender-bridge)
[![Development Status](https://img.shields.io/pypi/status/napari-blender-bridge.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-blender-bridge)](https://napari-hub.org/plugins/napari-blender-bridge)

Transfer surface layers between Napari and Blender. This plugin is young and has just limited functionality. Contributions are welcome.

----------------------------------

## Checklist
After the code for this plugin has been generated, go through this list:
* Write a minimal user guide below. Assume someone finds your plugin online and wonders how to quickly try it on your example data and on their data. Where should they start? What are the minimum necessary steps that need to be listed and explained? 
* Search for "TODO" in this file and the code to make sure all functions are properly documented.
* Make sure the requirements.txt correctly lists all dependencies and installation works as described below.
* Remove this checklist from the documentation.

## Usage

This plugin has its own submenu with all functionality under `Tools > Blender`.

![img.png](https://github.com/haesleinhuepf/napari-blender-bridge/raw/main/docs/easter.gif)


## Installation instructions

* Download and install [Blender 3.5](https://www.blender.org/download/). 
* Start Blender and click the menu `Edit > Preferences`. Activate `Developer extras`.

![img.png](https://github.com/haesleinhuepf/napari-blender-bridge/raw/main/docs/blender_preferences.png)

* It is recommended to run this plugin in a conda environment together with [devbio-napari](https://github.com/haesleinhuepf/devbio-napari), 
[vedo](https://vedo.embl.es/) and [napari-process-points-and-surfaces](https://github.com/haesleinhuepf/napari-process-points-and-surfaces).
To install these, please run these commands line-by-line:
```
mamba create --name napari-blender-env python=3.9 devbio-napari vedo -c conda-forge
mamba activate napari-blender-env
pip install napari-process-points-and-surfaces napari-blender-bridge
```

## Similar and related plugins

There are other plugins for working with surface meshes:
* [napari-stress](https://github.com/campaslab/napari-stress)
* [napari-pymeshlab](https://github.com/zacsimile/napari-pymeshlab)
* [napari-process-points-and-surfaces](https://github.com/haesleinhuepf/napari-process-points-and-surfaces)

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [GNU GPL v3.0] license,
"napari-blender-bridge" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/haesleinhuepf/cookiecutter-napari-assistant-plugin
[file an issue]: https://github.com/haesleinhuepf/napari-blender-bridge/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
