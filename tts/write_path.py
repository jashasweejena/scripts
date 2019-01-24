import sys
import os

fname = sys.argv[1]

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Documents and Settings\All Users\Start Menu\Programs\Startup'
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'python %s' % file_path)
path = os.path.abspath(fname)

if os.path.isfile(path) :
    add_to_startup(file_path = path)
else :
    print("File not found!")