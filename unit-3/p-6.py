# UNIT 3 - Q6: Write a program to perform file and directory operations
#               using os and sys modules.
# SCENARIO: A file-manager / project-setup script that creates folders and
#           files, lists and renames them, and reads command-line arguments.

import os, sys

print("Python version :", sys.version.split()[0])
print("OS name        :", os.name, "| Platform:", sys.platform)
print("Script args    :", sys.argv)
print("Current dir    :", os.getcwd())

os.makedirs("project/docs", exist_ok=True)            # create directories
with open("project/docs/readme.txt", "w") as f:       # create a file
    f.write("Hello from os module")

print("Files in project/docs :", os.listdir("project/docs"))
print("Is file?  :", os.path.isfile("project/docs/readme.txt"))
print("Is dir?   :", os.path.isdir("project/docs"))
print("Size      :", os.path.getsize("project/docs/readme.txt"), "bytes")
print("Abs path  :", os.path.abspath("project/docs/readme.txt"))
print("Split     :", os.path.split("project/docs/readme.txt"))
print("Extension :", os.path.splitext("readme.txt"))

os.rename("project/docs/readme.txt", "project/docs/info.txt")   # rename
print("After rename :", os.listdir("project/docs"))

for root, dirs, files in os.walk("project"):                    # walk tree
    print("Walk ->", root, dirs, files)

os.remove("project/docs/info.txt")                    # delete file
os.rmdir("project/docs"); os.rmdir("project")         # delete empty dirs
print("Cleaned up. Exists?", os.path.exists("project"))
print("Environment USER/HOME:", os.environ.get("HOME", "n/a"))
# sys.exit("message") would stop the program here
