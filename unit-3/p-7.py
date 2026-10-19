# 27. Write a Python program to copy, move and delete files using the shutil module.

import shutil
import os

with open("original.txt", "w") as f:
    f.write("Shutil demo file")
os.makedirs("backup", exist_ok=True)

shutil.copy("original.txt", "copy.txt")             # Copy
print("File copied")
shutil.move("copy.txt", "backup/moved.txt")         # Move
print("File moved to backup folder")
os.remove("original.txt")                           # Delete file
shutil.rmtree("backup")                             # Delete folder with contents
print("Cleanup completed")
