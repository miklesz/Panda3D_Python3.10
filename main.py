import platform

from direct.showbase.ShowBase import ShowBase
from panda3d.core import ConfigPageManager, PandaSystem

base = ShowBase()

print(ConfigPageManager.getGlobalPtr())
print('platform.python_version:', platform.python_version())
print('platform.machine:', platform.machine())
print('base.win.gsg.driver_vendor:', base.win.gsg.driver_vendor)
print('base.win.gsg.driver_renderer:', base.win.gsg.driver_renderer)
print('base.win.gsg.supports_basic_shaders:', base.win.gsg.supports_basic_shaders)
print("PandaSystem.version_string:", PandaSystem.version_string)

base.run()
