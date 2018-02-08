#!/usr/bin/env python
from time import time

def load_file(filename):
    words = set()
    with open(filename, 'r') as f:
        for line in f:
            words.add(line.strip()) #looks through line and splits by spaces
    return dict.fromkeys(words,0)

def timer(f, a):
    start_time = time()
    retval = f(a)
    end_time = time()
    return end_time-start_time, retval

if __name__ == "__main__":
    sensorsListLocation = '/home/mlfrantz/Documents/Glider/glider_code/rdml_research/deployment_data/09-11-2014.bob.dbd.sensors'
    sensorsList = timer(load_file,sensorsListLocation)#load_file(sensorsListLocation)
    print sensorsList
