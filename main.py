import random
import os
import json
import pathlib

from sys import platform


curr_path = str(pathlib.Path(__file__).parent.absolute()) + "/"

def get_object_list():
    path = curr_path + 'data/objects.json'
    f = open(path)
    data = json.load(f)
    f.close()
    return data


def output(image_path):
    if platform == "darwin":
        os.system('imgcat ' + image_path)
    elif platform == "linux" or platform == "linux2":
        os.system('kitty +kitten icat ' + image_path)
    else:
        raise RuntimeError("Unsupported platform")

object_list = get_object_list()
ids = object_list['objects']
total = object_list['total']
obj = ids[random.randrange(0, total-1)]
image_path = curr_path+'data/' + str(obj['objectID']) + '.jpg'

title = obj['title']
artist = obj['artistDisplayName']
date = obj['objectDate']

print(title + ", " + artist + ", " + date)
print("\n")
output(image_path)
