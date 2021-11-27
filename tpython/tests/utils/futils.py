from lib.utils.futils import writeFile
import os
import pytest

def test_write_file():
    folder = "folder_name"
    file = "file_name.temp"
    path = folder + '/' + file
    contents = "i am the content"
    writeFile(folder,file,contents)
    assert os.path.exists(path)
    opened_file = open(path)
    read_file = opened_file.read()
    assert contents == read_file