# coding: utf-8
import os
import sys
import random
import math
import json

ROOT_DIR = os.getcwd()


with open('C0026_2.json', 'a') as outfile:
    json_decode = json.load(outfile)

for i in json_decode:
    print("key: ", i)
    print("value: ", dict[i])
    if i == "x":
        print("value: ", dict[i])
        print ("add to value : ", 10+dict[i])