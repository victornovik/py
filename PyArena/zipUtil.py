import shutil
from pathlib import Path
from zipfile import ZipFile

zipFolder = Path("zip")
if not zipFolder.exists():
    zipFolder.mkdir()

with open("zip/1.txt", "w") as file1, open("zip/2.txt", "w") as file2:
    file1.write("1-st line")
    file2.write("1-st line")

with ZipFile("zip/archive.zip", mode="w") as archive:
    for file in zipFolder.iterdir():
        archive.write(file)

with ZipFile("zip/archive.zip", mode="r") as archive:
    # print(archive.infolist())
    archive.extractall("unzip")

shutil.rmtree(zipFolder, ignore_errors=True)
shutil.rmtree("unzip", ignore_errors=True)
