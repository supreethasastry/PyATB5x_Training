from abc import ABC, abstractmethod
class PC:
    def __init__(self):
        print("PC Initialized")

    @staticmethod
    def loadOS():
        print("starting OS")

    def startmouse(self):
        print("Starting mouse")

    def UseHeadPhone(self):
        print("Using Headphones")

class Motherboard(PC):
    @abstractmethod
    def startMotherBoard(self):
        print("Starting mother board")

class RAM(PC):
    @abstractmethod
    def startRAM(self):
        print("Starting RAM")

class Processor(PC):
    @abstractmethod
    def startProcessor(self):
        print("Starting Processor")

class Storage(PC):
    @abstractmethod
    def storagedata(self):
        print("Storing data")

m=Motherboard()
PC.loadOS()
m.startMotherBoard()


