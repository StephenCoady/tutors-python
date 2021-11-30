from genericpath import isfile
from lib.utils.futils import copyFileToFolder, getParentFolder, verifyFolder, writeFile, readFile, getImageFile, getDirectories
import os


folder = "tests"
folders = "test2/subtest/subsubtest"
file = "futil_test_file"
path = folder + '/' + file
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
    mdfile = "test_md_file.md"
    mdpath = folder + '/' + mdfile
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

def test_verify_folder():
    try:
        os.rmdir(folders)
    except:
        print("Doesn't exist")
    assert not os.path.exists(folders)
    verifyFolder(folders)
    assert os.path.exists(folders)

def test_copy_file_to_folder():
    folder_path = "t3/tt3"
    try:
        os.remove(img_file)
        os.remove(folder_path+ "/" + img_file)
        os.rmdir(folder_path)
    except:
        print("Doesn't exist")
    assert not os.path.exists(folder_path)
    os.makedirs(folder_path, exist_ok=True)
    os.mknod(img_file)
    assert os.path.exists(folder_path)
    assert os.path.exists(img_file)
    copyFileToFolder(img_file, folder_path)
    assert os.path.exists(folder_path + "/" + img_file)
