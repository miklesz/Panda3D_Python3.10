from setuptools import setup

setup(
    name='Panda3D_Python3.10',
    options={
        'build_apps': {
            # Build Panda3D_Python3.10 as a GUI application
            'gui_apps': {
                'Panda3D_Python3.10': 'main.py',
            },

            # Set up output logging, important for GUI apps!
            'log_filename': '$USER_APPDATA/Panda3D_Python3.10/output.log',
            'log_append': False,

            # Include the OpenGL renderer and OpenAL audio plug-in
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],
        }
    }
)
