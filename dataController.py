import pygame
import csv
from dataclasses import dataclass

"""
This node dataclass is the format of each data point that will be imported from the csv
"""
@dataclass
class Node:
    # Properties
    pos: pygame.Vector2
    color: str = "BLACK"
    cluster: int = -1
    # Data
    id: str
    data: list[int]

"""
This DataController object serves as the central hub of the data.
    It imports data and handles updating each unique node's ID, color, and data.
"""
class DataController:
    def __init__(self, filename: str):
        self.dataSet = self.importFromFile(filename)        # Data as list[Node]

    # This function takes a string input and returns 
    def importFromFile(self, filename: str) -> list[Node]:
        with open(filename) as file:
            csv_reader = csv.reader(file, delimiter=',')
            lineCount = 1
            for row in csv_reader:
                # Write Per Node Operations here
                self.dataSet[lineCount].id = row[1]
                for data in row:
                    self.dataSet[lineCount].data.append(data)

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