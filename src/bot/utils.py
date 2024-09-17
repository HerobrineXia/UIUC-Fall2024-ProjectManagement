from os import listdir
from os.path import isdir, join

def get_directory(path):
    return [f for f in listdir(path) if isdir(join(path, f))]