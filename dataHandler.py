import pygame
import csv
from dataclasses import dataclass

"""
This node dataclass is the format of each data point that will be imported from the csv
"""
@dataclass
class Node:
    # Properties
    color: str = "BLACK"
    cluster: int = -1
    # Data
    id: str
    data: list[int]

"""
This DataHandler object serves as the central hub of the data.
    It imports data and handles updating each unique node's ID, color, and data.
"""
class DataHandler:
    def __init__(self, filename: str):
        self.dataSet = self.importFromFile(filename)        # Data as list[Node]

    # This function takes a string input and returns 
    def importFromFile(self, filename: str) -> list[Node]:
        with open(filename) as file:
            csvReader = csv.reader(file, delimiter=',')
            lineCount = 1
            for row in csvReader: # Each row of the csv gets loaded into list "row"
                self.dataSet[lineCount].id = row[1:] # 1: Slice the first element
                self.dataSet[lineCount].data = row

    def updateColor(self, node):
            match node.cluster:
                case 1:
                    node.color = (200, 0, 0) # Red
                case 2:
                    node.color = (0, 200, 0) # Blue
                case 3:
                    node.color = (0, 0, 200) # Green
                case other:
                    node.color = (160,32,240) # Purple