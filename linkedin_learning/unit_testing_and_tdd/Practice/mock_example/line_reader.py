import os

def readFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("File not found")
    else:
        file_obj = open(filename, 'r')
        line = file_obj.readline()
        return line