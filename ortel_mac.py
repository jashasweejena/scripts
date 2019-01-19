#!/usr/bin/env python
# coding: utf-8
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import sys

path = sys.argv[1]

def replace(file_path):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                mac = line.split()[0]
                new_file.write(line.replace(mac, convert(mac)))
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def convert(mac):
    converted = " "
    length = len(mac)
    x = 0

    for i in range(0, length, 2):
        converted = converted + ":" + (mac[x:i])
        x = i

    final = converted[3 : len(converted)]
    return final
    
replace(path)
