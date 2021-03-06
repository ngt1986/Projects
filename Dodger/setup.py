import cx_Freeze, os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

options = {
    'build_exe': {
        'include_files':["left.png","right.png","up.png","upleft.png","upright.png",
                         "downleft.png","downright.png","down.png","D.png","Crash.wav","Powerup.wav",
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ],
    },
}

executables = [cx_Freeze.Executable("Dodger.py")]

cx_Freeze.setup(
    name="Dodger",
    options=options,
    executables = executables,
    version="1.0.0"
    )
