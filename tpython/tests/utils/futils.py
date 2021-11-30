from lib.utils.futils import writeFile, readFile
import os
import pytest

folder = "tests"
file = "futil_test_file"
path = folder + '/' + file


def test_write_file():
    os.remove(path)
    os.rmdir(folder)
    contents = "i am the content"
    writeFile(folder,file,contents)
    assert os.path.exists(path)
    opened_file = open(path, "r")
    read_file = opened_file.read()
    assert contents == read_file

def test_read_file():
    os.remove(path)
    os.rmdir(folder)
    list_of_lines = []
    contents = "i am the content \r\n and this is a line with a line terminator for mac"
    writeFile(folder, file, contents)
    new_file = readFile(path)
    assert '\r' not in new_file

def test_get_image():
    remove_test_dir
    try:
        os.remove("image.jpg")
    except:
        pass
    os.mknod("image.jpg")
    test_img = getImageFile("image")
    assert test_img == "image.jpg"
