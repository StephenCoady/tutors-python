from genericpath import isfile
from lib.utils.futils import getParentFolder, writeFile, readFile, getImageFile, getDirectories
import os

folder = "tests"
file = "futil_test_file"
mdfile = "test_md_file.md"
path = folder + '/' + file
mdpath = folder + '/' + mdfile
img_file = "image.jpg"


def test_write_file():
    try:
        os.remove(path)
        os.rmdir(folder)
    except:
        print("Doesn't exist")
    contents = "i am the content"
    writeFile(folder,file,contents)
    assert os.path.exists(path)
    opened_file = open(path, "r")
    read_file = opened_file.read()
    assert contents == read_file

def test_read_file():
    try:
        os.remove(path)
        os.rmdir(folder)
    except:
        print("Doesn't exist")
    contents = "i am the content \r\n and this is a line with a line terminator for mac"
    writeFile(folder, file, contents)
    new_file = readFile(path)
    assert '\r' not in new_file

def test_get_image():
    try:
        os.remove("image.jpg")
    except:
        print("Doesn't exist")
    os.mknod("image.jpg")
    test_img = getImageFile("image")
    assert test_img == "image.jpg"

def test_get_parent_folder():
    parent = getParentFolder()
    assert parent == "src" # This must be changed to your parent folder to pass

def test_get_directories():
    try:
        os.remove(mdpath)
        os.rmdir(folder)
    except:
        print("Doesn't exist")
    src = "."
    writeFile(src, mdfile, "test")

    directories = []
    directories = getDirectories(src)
    for item in directories:
        assert isfile(item)

    