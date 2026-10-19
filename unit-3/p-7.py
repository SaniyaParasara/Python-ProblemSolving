# UNIT 3 - Q7: Write a program to copy, move and delete files using the
#               shutil module.
# SCENARIO: Backup utility: copy report files to a backup folder, move old
#           files to an archive and remove temporary folders.

import shutil, os

os.makedirs("work", exist_ok=True)
os.makedirs("backup", exist_ok=True)
os.makedirs("archive", exist_ok=True)
with open("work/report.txt", "w") as f:
    f.write("Quarterly report data")

shutil.copy("work/report.txt", "backup/report_copy.txt")       # copy file
shutil.copy2("work/report.txt", "backup/report_meta.txt")      # copy + metadata
print("Backup folder :", os.listdir("backup"))

shutil.copytree("backup", "backup_full")                        # copy folder
print("backup_full   :", os.listdir("backup_full"))

shutil.move("work/report.txt", "archive/report_old.txt")        # move
print("Archive       :", os.listdir("archive"))
print("work folder   :", os.listdir("work"))

total, used, free = shutil.disk_usage(".")
print("Free disk (GB):", round(free / 1024**3, 1))

for d in ("work", "backup", "backup_full", "archive"):          # delete folders
    shutil.rmtree(d)
print("All deleted. work exists?", os.path.exists("work"))
