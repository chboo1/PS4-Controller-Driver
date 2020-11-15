from pynput.mouse import Controller, Button
class Main():
    def __init__(self):
        self.mouse = Controller()
        while True:
            with open("/dev/input/js0", "rb") as self.controller:
                self.controller.read(168)
                self.input = self.controller.read(8).hex()
                if self.input[-4:-2] == "01":
                    if self.input[-8:-6] == "01":
                        if self.input[-4:] == "0101":
                            self.mouse.press(Button.left)
                        if self.input[-4:] == "0100":
                            self.mouse.press(Button.right)
                    if self.input[-8:-6] == "00":
                        if self.input[-4:] == "0101":
                            self.mouse.release(Button.left)
                        if self.input[-4:] == "0100":
                            self.mouse.release(Button.right)
                if self.input[-4:-2] == "02":
                    if self.input[-2:] == "00":
                        if int(self.input[-6:-4], 16) > 127:
                            self.movement = int(self.input[-6:-4], 16) - 255
                        else:
                            self.movement = int(self.input[-6:-4], 16)
                        self.mouse.move(self.movement / 2, 0)
                    if self.input[-2:] == "01":
                        if int(self.input[-6:-4], 16) > 127:
                            self.movement = int(self.input[-6:-4], 16) - 255
                        else:
                            self.movement = int(self.input[-6:-4], 16)
                        self.mouse.move(0, self.movement / 2)
                    if self.input[-2:] == "02":
                        if int(self.input[-6:-4], 16) > 127:
                            self.movement = int(self.input[-6:-4], 16) - 255
                        else:
                            self.movement = int(self.input[-6:-4], 16)
                        self.mouse.scroll(-self.movement / 2, 0)
                    if self.input[-2:] == "03":
                        if int(self.input[-6:-4], 16) > 127:
                            self.movement = int(self.input[-6:-4], 16) - 255
                        else:
                            self.movement = int(self.input[-6:-4], 16)
                        self.mouse.scroll(0, -self.movement / 2)



if __name__ == "__main__":
    program = Main()
