import random
import os
from os.path import exists
import json
import pathlib

curr_path = str(pathlib.Path(__file__).parent.absolute()) + "/"

def get_object_list():
    path = curr_path + 'data/objects.json'
    f = open(path)
    data = json.load(f)
    f.close()
    return data


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
os.system('kitty +kitten icat ' + image_path)
