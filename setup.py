'''
Create a .exe from a python file using cx_Freeze

Steps:
1. Install python, add it to environmental variables, and add any packages including cx_freeze. 
I couldn't get it to work with anaconda or pip due to folder paths
2. Change file_name to your python file name
3. Change installer_name variable to a custom name
4. Include any packages your python file uses in the packages list
5. Place the setup.py script in the same folder as your python script
6. Run it as: setup.py FolderName
'''

from cx_Freeze import setup, Executable

base = None    
file_name = "file_name.py"
installer_name = 'Program'

executables = [Executable(file_name, base=base, icon = None)]

packages = ["subprocess","sys","os","tkinter"]

options = {
    'build_exe': {
        'build_exe': './/build'
    }
}

setup(
    name = installer_name,
    options = options,
    version = "6.2",
    description = '',
    executables = executables
)
