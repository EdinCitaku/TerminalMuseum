import random
import os
import json
import pathlib
import argparse

curr_path = str(pathlib.Path(__file__).parent.absolute()) + "/"


def get_object_list():
    path = curr_path + 'data/objects.json'
    f = open(path)
    data = json.load(f)
    f.close()
    return data

def main():
    object_list = get_object_list()
    ids = object_list['objects']
    total = object_list['total']
    obj = ids[random.randrange(0, total-1)]
    image_path = curr_path+'data/' + str(obj['objectID']) + '.jpg'

    title = obj['title']
    artist = obj['artistDisplayName']
    date = obj['objectDate']

    parser = argparse.ArgumentParser(description='A CLI that displays a random painting on the terminal')
    parser.add_argument("-t","--print_title", help="Prints title and additional information about the painting above.", action="store_true")

    parser.add_argument("--command", help="Executes the supplied command with the path to the image: [COMMAND] /path/to/painting.png", required=True)

    args = parser.parse_args()

    if(args.print_title):
        print(title + ", " + artist + ", " + date)
        print("\n")


    os.system( args.command+" "+ image_path)
