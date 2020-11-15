import signal
from tkinter import Tk, Canvas

class Timeout(Exception):
    pass



class Main():
    def __init__(self):
        # Initializing graphics engine
        self.root = Tk()
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry("{}x{}".format(self.width, self.height))
        self.c = Canvas(self.root, width=self.width, height=self.height)
        self.c.pack()
        # Initializing buttons pressed values as well as stick value
        self.Bpressed = False
        self.Apressed = False
        self.Xpressed = False
        self.Ypressed = False
        self.Lpressed = False
        self.Rpressed = False
        self.ZRpressed = False
        self.Zlpressed = False
        self.MINUSpressed = False
        self.PLUSpressed = False
        self.HOMEpressed = False
        self.ANApressed = False
        self.Cpressed = False
        self.DU = False
        self.DD = False
        self.DL = False
        self.DR = False
        # Confusing joystick values
        # Depth, 80-ff = going left/up, 00 = neutral, 01-7f = going right/down
        # Other value's purpose is still unknown
        self.analogStickDepth_00 = 00
        self.analogStickDepth_01 = 00
        self.cStickDepth_02 = 00
        self.cStickDepth_03 = 00
        self.analogStickValue_0000 = 00
        self.cStickValue_0000 = 00
        # Making graphical text
        self.stickValues = self.c.create_text(self.width / 2, self.height / 2 - 10, text="Depth Analog 00: {}, Depth Analog 01: {}, Depth C 02: {}, Depth C 03: {}".format(self.analogStickDepth_00, self.analogStickDepth_01, self.cStickDepth_02, self.cStickDepth_03))
        self.stickValues_00 = self.c.create_text(self.width / 2, self.height / 2 + 10, text="Value Analog: {}, Value C {}".format(self.analogStickValue_0000, self.cStickValue_0000))
        # Binding buttons such as esc for quit and start mainloop
        self.root.bind("<Escape>", self.kr)
        self.try_one(lambda: self.root.after(33, self.mainloop), 1)
        # Starting mainloop, no code will be executed after it is started
        self.root.mainloop()



    def kr(self, event=None):
        self.root.destroy()


    def mainloop(self):
        try:
            with open("/dev/input/js0", "rb") as self.controller: 
                self.controller.read(8*21)
                self.id = self.controller.read(8).hex()
                if self.id[-4:-2] == "02":
                    if self.id[-2:] == "00":
                        self.analogStickDepth_00 = self.id[-6:-4]
                        self.analogStickValue_0000 = self.id[-8:-6]
                    if self.id[-2:] == "01":
                        self.analogStickDepth_01 = self.id[-6:-4]
                        self.analogStickValue_0100 = self.id[-8:-6]
                else:
                    pass
        except FileNotFoundError:
            raise RuntimeError("No controller is connected, exiting program")
        self.c.itemconfig(self.stickValues, text="Depth Analog 00: {}, Depth Analog 01: {}, Depth C 02: {}, Depth C 03: {}".format(self.analogStickDepth_00, self.analogStickDepth_01, self.cStickDepth_02, self.cStickDepth_03)) 
        self.c.itemconfig(self.stickValues_00, text="Value Analog: {}, Value C {}".format(self.analogStickValue_0000, self.cStickValue_0000))
        self.try_one(lambda: self.root.after(33, self.mainloop), 1)


    def try_one(self, func, t):
        def timeout_handler(signum, frame):
            raise Timeout()
        old_handler = signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(t) # triger alarm in 3 seconds
        try:
            func()
        except Timeout:
            print('{} timed out after {} seconds'.format(func.__name__,t))
            return None
        finally:
            signal.signal(signal.SIGALRM, old_handler)
        signal.alarm(0)





if __name__ == "__main__":
    window = Main()
