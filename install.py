import shutil

import os

import sys

import subprocess

def add_to_path(folder_path):
    """
    Adds a folder to the system's Path environment variable using setx.
    Requires administrative privileges.
    """
    try:
        # Get current Path
        current_path = subprocess.check_output("echo %PATH%", shell=True).decode().strip()
        
        # Add new folder if not already present
        if folder_path not in current_path:
            new_path = f"{folder_path};{current_path}"
            subprocess.run(f'setx PATH "{new_path}"', shell=True, check=True)
            print(f"Added '{folder_path}' to Path. Restart required for full effect.")
        else:
            print(f"'{folder_path}' is already in Path.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding to Path: {e}")
        print("Ensure you are running with administrative privileges.")

os.system("git clone https://github.com/jhfhngj/The-Pur-Project-C.git")

def get_os_type():
    platform = sys.platform
    if platform.startswith('win'):
        return "Windows"
    elif platform.startswith('linux'):
        return "Linux"
    elif platform == 'darwin':
        return "macOS"
    else:
        return "Unknown OS"

os_name = get_os_type()
print(f"The operating system is: {os_name}")

if os_name == "Windows":
  print("Run as admin/root or use sudo to do this.")
  print("Adding Pur to PATH for install...")
  os.makedirs("C:\\Program Files\\Pur\\", exist_ok=True)
  os.system("xcopy The-Pur-Project-C\\ C:\\Program Files\\Pur\\ /E /H /C /I /Y")
  add_to_path(r"C:\\Program Files\\Pur\\")
  print("Restart to apply changes.")
elif os_name == "Linux":
  print("Run as admin/root or use sudo to do this.")
  print("Adding Pur to PATH for install...")
  os.system("chmod +x ./The-Pur-Project-C/main.py")
  os.system("cp ./The-Pur-Project-C/main.py /bin/pur")
elif os_name == "Darwin":
  print("Run as admin/root or use sudo to do this.")
  print("Adding Pur to PATH for install...")
  os.system("chmod +x ./The-Pur-Project-C/main.py")
  os.system("cp ./The-Pur-Project-C/main.py /etc/path/pur")
else:
  print("Unknown system. Not able to install Pur.")
