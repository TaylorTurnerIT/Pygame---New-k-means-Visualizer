import pygame
import time
import logging

time = time.time()

def debugTime(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
    return wrapper

