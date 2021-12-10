from genericpath import exists, isdir
import shutil as sh
from os.path import isfile, join
from os import listdir
import os
import logging
import frontmatter

def writeFile(folder,filename,contents):
    if not os.path.exists(folder):
        os.makedirs(folder)
        os.mknod(folder + '/' + filename)
        file = open(folder + '/' + filename, 'a')
        file.write(contents)
    else:
        pass

def readFile(path1):
    if os.path.exists(path1):
        list_of_lines = []
        open_file = open(path1, "r")
        read_file = open_file.read()
        list_of_lines = read_file.splitlines()
        return list_of_lines[0].replace('\r', '')
    else:
        logging.warning('Unable to locate ' + path1)

def getImageFile(name):
    validImageTypes = ['png','jpg','jpeg','gif']
    image = ''
    for type in validImageTypes:
        image = name + '.' + type
        if os.path.exists(image):
            return image
        else:
            pass

def getParentFolder():
    return os.path.basename(os.path.dirname(os.getcwd())) 

def getDirectories(srcpath):
    onlyfiles = [f for f in listdir(srcpath) if isdir(join(srcpath, f))]
    return onlyfiles

def verifyFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

def copyFileToFolder(src, dest):
    if os.path.exists(src):
        os.makedirs(dest, exist_ok=True)
        sh.copy2(src, dest)

def copyFolder(src, dest):
    sh.copytree(src, dest)

def readWholeFile(path):
    if os.path.exists(path):
        open_content = open(path)
        file_content = open_content.read()
        return file_content
    else:
        print('Unable to locate ' + path)

def readYaml(path):
    yamldata = ''
    with open(path) as yam:
        yamldata = frontmatter.load(yam)
    return yamldata

def readEnrollment(path):
    yamldata = ''
    with open(path) as yam:
        yamldata = frontmatter.load(yam)
    return yamldata

def readCalendar(path):
    yamldata = ''
    with open(path) as yam:
        yamldata = frontmatter.load(yam)
    return yamldata

def withoutHeader(fileName):
    file = open(fileName, "r")
    content = file.read()
    line1 = content.index('\n')
    content = content[line1 + 1 : len(content)]    
    content = content.strip()
    line2 = content.index('\n')
    if(line2 > -1):
        content = content[0 : line2]
    return content

def getHeaderFromBody(body):
    array = body.split('\n')
    header = ''
    if array[0][0] == '#':
        header = array[0][1:]
    else:
        header = array[0]
    return header           

def withoutHeaderFromBody(body):
    content = body
    line1 = content.index('\n')
    content = content[line1 + 1 : len(content)]
    content = content.strip()
    line2 = content.index('\n')
    if line2 > -1:
        content = content[0:line2]
    return content

def initPath(path):
    os.mkdir('-p', path)

