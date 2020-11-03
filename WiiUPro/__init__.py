from __future__ import print_function
import sys
B = "0100"
A = "0101" 
X = "0102" 
Y = "0103" 
L = "0104" 
R = "0105" 
ZL = "0106" 
ZR = "0107" 
PLUS = "0108"
MINUS = "0109" 
HOME = "010a" 
ANALOG = "010b" 
C = "010c" 
UP = "010d" 
DOWN = "010e" 
LEFT = "010f" 
RIGHT = "0110" 
ANY = "0000"
PRESS = "01"
RELEASE = "00"
class Remote():
    def __init__(self, num=0):
        self.num = num
        self.buttons = {
             "B": B, 
             "A": A, 
             "X": X, 
             "Y": Y, 
             "L": L, 
             "R": R, 
             "ZL": ZL, 
             "ZR": ZR, 
             "+": PLUS, 
             "-": MINUS, 
             "H": HOME, 
             "N": ANALOG, 
             "C": C, 
             "U": UP, 
             "D": DOWN, 
             "<": LEFT, 
             ">": RIGHT, 
             "ANY": ANY
        }
        self.buttonss = {
            B: "B",
            A: "A",
            X: "X",
            Y: "Y",
            L: "L",
            R: "R",
            ZL: "ZL",
            ZR: "ZR",
            PLUS: "+",
            MINUS: "-",
            HOME: "H",
            ANALOG: "N",
            C: "C",
            UP: "U",
            DOWN: "D",
            LEFT: "<",
            RIGHT: ">",
            ANY: "ANY"
                }
        self.idlist = self.buttons.values()
        self.callbacks = {}

    def create_callback(self, button, func, on="01"):
        if not str(button)[-4:] in self.idlist and not str(button)[-4:-2] == "02":
            raise ValueError("Fatal: Wrong Value For Button `{}'".format(button))
        self.callbacks[(button, on)] = func

    def check_callbacks(self):
        with open("/dev/input/js{}".format(self.num), "rb") as self.remote:
            self.remote.read(8 * 21)
            self.fullid = self.remote.read(8).hex()
            if str(self.fullid[-4:-2]) != "02":
                self.func = self.callbacks.get(("0000", str(self.fullid[-8:-6])))
                if self.func:
                    self.func(Button(self.buttonss.get(self.fullid[-4:]), self.fullid[-8:-6], self.fullid))
                self.func = self.callbacks.get((str(self.fullid[-4:]), str(self.fullid[-8:-6])))
                if self.func:
                    self.func(Button(self.buttonss.get(self.fullid[-4:]), self.fullid[-8:-6], self.fullid))

class Button():
    def __init__(self, button, on, buttonid):
        self.button = button
        self.on = on
        self.buttonid = buttonid
