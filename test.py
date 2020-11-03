import os
import sys
class WiiUPro():
    def __init__(self):
        self.num = 0


    def pbi(self):
        try:
            while True:
                with open("/dev/input/js{}".format(self.num)) as self.remote:
                    print(self.remote.read(8).hex()[-4:])
        except OSError:
            self.num += 1

    def pbn(self):
        print("mode pbn")
        try:
            with open('/dev/input/js{}'.format(self.num), 'rb') as self.remote:
                while True:
                    self.fullid = self.remote.read(8).hex()
                    self.id = self.fullid[-4:]
                    if str(self.fullid[-8:-6]) == "00":
                        print("Released ", end="")
                    if str(self.fullid[-8:-6]) == "01":
                        print("Pressed ", end="")
                    if self.fullid != None:
                        """
                        if str(self.id) == "0100":
                            print("B")
                        if str(self.id) == "0101":
                            print("A")
                        if str(self.id) == "0102":
                            print("X")
                        if str(self.id) == "0103":
                            print("Y")
                        if str(self.id) == "0104":
                            print("L")
                        if str(self.id) == "0105":
                            print("R")
                        if str(self.id) == "0106":
                            print("ZL")
                        if str(self.id) == "0107":
                            print("ZR")
                        if str(self.id) == "0108":
                            print("-")
                        if str(self.id) == "0109":
                            print("+")
                        if str(self.id) == "010a":
                            print("HOME")
                        if str(self.id) == "010b":
                            print("Analog stick")
                        if str(self.id) == "010c":
                            print("C stick")
                        if str(self.id) == "010d":
                            print("D pad Up")
                        if str(self.id) == "010e":
                            print("D pad Down")
                        if str(self.id) == "010f":
                            print("D pad Left")
                        if str(self.id) == "0110":
                            print("D pad Right")
                        if str(self.id) == "0200": 
                            if str(self.fullid)[-8:-4] == "0180":
                                print("Analog Up")
                            elif str(self.fullid)[-8:-4] == "ff7f":
                                print("Analog Down")
                            print("Analog Sideways")
                        if str(self.id) == "0201":
                            print("Analog Vertically")
                        if str(self.id) == "0202":
                            print("C Stick Sideways")
                        if str(self.id) == "0203":
                            print("C stick Vertically")
                        """
                        print(int(self.fullid[-8:-6], 16))

        except OSError:
            self.num += 1



    def fullid(self):
        try:
            with open('/dev/input/js{}'.format(self.num), 'rb') as self.remote:
                self.remote.read(16*10)
                while True:
                    self.id = self.remote.read(8).hex()
                    if self.id[-4:] == "0105":
                        os.system("clear")
                    else:
                        print(self.id[-8:])
        except OSError:
            self.num += 1


    def mode(self):
        try:
            with open('/dev/input/js{}'.format(self.num), 'rb') as self.remote:
                self.remote.read(16*10)
                while True:
                    self.id = self.remote.read(8).hex()[-4:]
                    if str(self.id) == "0101":
                        self.pbi()
                    elif str(self.id) == "0100":
                        sys.exit()
                    elif str(self.id) == "0102":
                        self.pbn()
                    elif str(self.id) == "0103":
                        self.fullid()
        except OSError:
            self.num += 1


if __name__ == "__main__":
    main = WiiUPro()
    main.mode()
