from cx_Freeze import setup, Executable
import sys
base = None    

include_files = ['lib']

if (sys.platform == "win32"):
    base = "Win32GUI"
executables = [Executable("trelloApp.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
        'include_files':include_files,
    },
}

setup(
    name = "trelloApp",
    options = options,
    version = "0.1",
    description = 'Trello',
    executables = executables,
    author='dan.tran',
    author_email='tranthedan1609@gmail.com',
)
