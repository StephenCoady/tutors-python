import os

from genericpath import isdir
from lib.utils.futils import (
    copyFileToFolder,
    copyFolder,
    getDirectories,
    getHeaderFromBody,
    getImageFile,
    getParentFolder,
    initPath,
    readFile,
    readWholeFile,
    readYaml,
    verifyFolder,
    withoutHeader,
    withoutHeaderFromBody,
    writeFile,
)

folder = "test"
folders = "testTwo/subtest/subsubtest"
file = "futil_test_file"
path = folder + "/" + file
img_file = "image.jpg"
mdfile = "test_md_file.md"
mdpath = folder + "/" + mdfile


def test_init_path():
    initPath(folders)
    assert os.path.exists(folders)
    os.removedirs(folders)


def test_write_file():
    contents = "i am the content"
    writeFile(folder, file, contents)
    assert os.path.exists(path)
    opened_file = open(path, "r")
    read_file = opened_file.read()
    assert contents == read_file
    os.remove(path)
    os.rmdir(folder)


def test_read_file():
    contents = "i am the content \r\n and this is a line with a line terminator for mac"
    writeFile(folder, file, contents)
    new_file = readFile(path)
    assert "\r" not in new_file
    os.remove(path)
    os.rmdir(folder)


def test_get_image():
    os.mknod("image.jpg")
    test_img = getImageFile("image")
    assert test_img == "image.jpg"
    os.remove("image.jpg")


def test_get_parent_folder():
    parent = getParentFolder()
    assert parent == "src"  # This must be changed to your parent folder to pass


def test_get_directories():
    src = "."
    os.mknod(mdfile)
    directories = []
    directories = getDirectories(src)
    for item in directories:
        assert isdir(item)
    os.remove(mdfile)


def test_verify_folder():
    assert not os.path.exists(folders)
    verifyFolder(folders)
    assert os.path.exists(folders)
    os.removedirs(folders)


def test_copy_file_to_folder():
    folder_path = "tests3/test4"
    assert not os.path.exists(folder_path)
    os.makedirs(folder_path, exist_ok=True)
    os.mknod(img_file)
    assert os.path.exists(folder_path)
    assert os.path.exists(img_file)
    copyFileToFolder(img_file, folder_path)
    assert os.path.exists(folder_path + "/" + img_file)
    os.remove(img_file)
    os.remove(folder_path + "/" + img_file)
    os.removedirs(folder_path)


def test_copy_folder():
    src = "src"
    dest = "dst"
    os.makedirs(src)
    assert os.path.exists(src)
    assert not os.path.exists(dest)
    copyFolder(src, dest)
    assert os.path.exists(dest)
    os.rmdir(src)
    os.rmdir(dest)


def test_read_whole_file():
    file_path = "tests/readwhole/"
    file_name = "file.txt"
    content = "I am the content"
    file = readWholeFile(file_path + file_name)
    assert not file
    writeFile(file_path, file_name, content)
    assert os.path.exists(file_path + file_name)
    final_file = readWholeFile(file_path + file_name)
    assert final_file == content
    os.remove(file_path + file_name)
    os.removedirs(file_path)


def test_read_yaml():
    file_path = "tests/readyaml/"
    file_name = "file.yaml"
    yaml_content = """json:
  - rigid
  - better for data interchange
yaml: 
  - slim and flexible
  - better for configuration
    """
    writeFile(file_path, file_name, yaml_content)
    assert os.path.exists(file_path + file_name)
    yaml_data = readYaml(file_path + file_name)
    yaml_data = yaml_data.content
    yaml_content = yaml_content.lstrip().rstrip()
    assert yaml_content == yaml_data
    os.remove(file_path + file_name)
    os.removedirs(file_path)


def test_without_header():
    file_path = "tests/nohead/"
    file_name = "file.txt"
    content = "This is line one \nWhile this is line two\nA third? amazing"
    writeFile(file_path, file_name, content)
    new_contents = withoutHeader(file_path + file_name)
    assert new_contents == content[18:-17]
    os.remove(file_path + file_name)
    os.removedirs(file_path)


def test_get_header_from_body():
    file_path = "tests/headfrombody/"
    file_name = "file.txt"
    body = "#This is line one \nWhile this is line two\nA third? amazing"
    index = body.index("\n")
    writeFile(file_path, file_name, body)
    open_file = open(file_path + file_name)
    read_file = open_file.read()
    new_contents = getHeaderFromBody(read_file)
    assert new_contents == body[1:index]
    os.remove(file_path + file_name)
    os.removedirs(file_path)


def test_without_header_from_body():
    file_path = "tests/withoutheadfrombody/"
    file_name = "file.txt"
    body = "#This is line one \nWhile this is line two\nA third? amazing"
    writeFile(file_path, file_name, body)
    open_file = open(file_path + file_name)
    read_file = open_file.read()
    new_contents = withoutHeaderFromBody(read_file)
    assert new_contents == body[19:-17]
    os.remove(file_path + file_name)
    os.removedirs(file_path)
