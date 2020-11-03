from tkinter import Tk, Canvas
from pynput.mouse import Button, Controller


class Main():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.cx = 400
        self.cy = 400
        self.root.title("Testing the Wii u Pro Controller")
        self.c = Canvas(self.root, width=800, height=800)
        self.stick_outside = self.c.create_oval(0, self.cy - 133, 266, self.cy + 133, fill="#ffffff", outline="#000000")
        self.censtickpos = [(self.c.coords(self.stick_outside)[0] + self.c.coords(self.stick_outside)[2]) / 2, (self.c.coords(self.stick_outside)[1] + self.c.coords(self.stick_outside)[3]) / 2]
        self.stick = self.c.create_oval(self.censtickpos[0] - 5, self.cy - 5, self.censtickpos[0] + 5, self.cy + 5, fill="#000000")
        self.stick_outside2 = self.c.create_oval(800 - 266, self.cy - 133, 800, self.cy + 133, fill="#ffffff", outline="#000000")
        self.censtickpos2 = [(self.c.coords(self.stick_outside2)[0] + self.c.coords(self.stick_outside2)[2]) / 2, (self.c.coords(self.stick_outside2)[1] + self.c.coords(self.stick_outside2)[3]) / 2]
        self.stick2 = self.c.create_oval(self.censtickpos2[0] - 5, self.cy - 5, self.censtickpos2[0] + 5, self.cy + 5, fill="#000000")
        self.stickcpos = list(self.c.coords(self.stick))
        self.pressedButtons = []
        self.Acheck = self.c.create_oval(self.cx + 125, self.cy + 235, self.cx + 145, self.cy + 255, fill="#ffffff", outline="#000000")
        self.Bcheck = self.c.create_oval(self.cx + 100, self.cy + 260, self.cx + 120, self.cy + 280, fill="#ffffff", outline="#000000")
        self.Xcheck = self.c.create_oval(self.cx + 100, self.cy + 210, self.cx + 120, self.cy + 230, fill="#ffffff", outline="#000000")
        self.Ycheck = self.c.create_oval(self.cx + 75, self.cy + 235, self.cx + 95, self.cy + 255, fill="#ffffff", outline="#000000")
        self.Lcheck = self.c.create_rectangle(self.cx - 100, self.cy + 175, self.cx - 80, self.cy + 195, fill="#ffffff", outline="#000000")
        self.Rcheck = self.c.create_rectangle(self.cx + 100, self.cy + 175, self.cx + 120, self.cy + 195, fill="#ffffff", outline="#000000")
        self.ZLcheck = self.c.create_rectangle(self.cx - 100, self.cy + 150, self.cx - 80, self.cy + 170, fill="#ffffff", outline="#000000")
        self.ZRcheck = self.c.create_rectangle(self.cx + 100, self.cy + 150, self.cx + 120, self.cy + 170, fill="#ffffff", outline="#000000")
        self.HOMEcheck = self.c.create_oval(self.cx - 10, self.cy + 190, self.cx + 10, self.cy + 210, fill="#ffffff", outline="#000000")
        self.MINUScheck = self.c.create_oval(self.cx - 35, self.cy + 190, self.cx - 15, self.cy + 210, fill="#ffffff", outline="#000000")
        self.PLUScheck = self.c.create_oval(self.cx + 35, self.cy + 190, self.cx + 15, self.cy + 210, fill="#ffffff", outline="#000000")
        self.DLcheck = self.c.create_rectangle(self.cx - 125, self.cy + 235, self.cx - 105, self.cy + 255, fill="#ffffff", outline="#000000")
        self.DRcheck = self.c.create_rectangle(self.cx - 75, self.cy + 235, self.cx - 55, self.cy + 255, fill="#ffffff", outline="#000000")
        self.DUcheck = self.c.create_rectangle(self.cx - 100, self.cy + 210, self.cx - 80, self.cy + 230, fill="#ffffff", outline="#000000")
        self.DDcheck = self.c.create_rectangle(self.cx - 100, self.cy + 260, self.cx - 80, self.cy + 280, fill="#ffffff", outline="#000000")
        self.Atext = self.c.create_text((self.c.coords(self.Acheck)[0] + self.c.coords(self.Acheck)[2]) / 2, (self.c.coords(self.Acheck)[1] + self.c.coords(self.Acheck)[3]) / 2, text="A", anchor="c")
        self.Btext = self.c.create_text((self.c.coords(self.Bcheck)[0] + self.c.coords(self.Bcheck)[2]) / 2, (self.c.coords(self.Bcheck)[1] + self.c.coords(self.Bcheck)[3]) / 2, text="B", anchor="c")
        self.Xtext = self.c.create_text((self.c.coords(self.Xcheck)[0] + self.c.coords(self.Xcheck)[2]) / 2, (self.c.coords(self.Xcheck)[1] + self.c.coords(self.Xcheck)[3]) / 2, text="X", anchor="c")
        self.Ytext = self.c.create_text((self.c.coords(self.Ycheck)[0] + self.c.coords(self.Ycheck)[2]) / 2, (self.c.coords(self.Ycheck)[1] + self.c.coords(self.Ycheck)[3]) / 2, text="Y", anchor="c")
        self.Ltext = self.c.create_text((self.c.coords(self.Lcheck)[0] + self.c.coords(self.Lcheck)[2]) / 2, (self.c.coords(self.Lcheck)[1] + self.c.coords(self.Lcheck)[3]) / 2, text="L", anchor="c")
        self.Rtext = self.c.create_text((self.c.coords(self.Rcheck)[0] + self.c.coords(self.Rcheck)[2]) / 2, (self.c.coords(self.Rcheck)[1] + self.c.coords(self.Rcheck)[3]) / 2, text="R", anchor="c")
        self.ZLtext = self.c.create_text((self.c.coords(self.ZLcheck)[0] + self.c.coords(self.ZLcheck)[2]) / 2, (self.c.coords(self.ZLcheck)[1] + self.c.coords(self.ZLcheck)[3]) / 2, text="ZL", anchor="c")
        self.ZRtext = self.c.create_text((self.c.coords(self.ZRcheck)[0] + self.c.coords(self.ZRcheck)[2]) / 2, (self.c.coords(self.ZRcheck)[1] + self.c.coords(self.ZRcheck)[3]) / 2, text="ZR", anchor="c")
        self.HOMEtext = self.c.create_text((self.c.coords(self.HOMEcheck)[0] + self.c.coords(self.HOMEcheck)[2]) / 2, (self.c.coords(self.HOMEcheck)[1] + self.c.coords(self.HOMEcheck)[3]) / 2, text="\u2302", anchor="c")
        self.MINUStext = self.c.create_text((self.c.coords(self.MINUScheck)[0] + self.c.coords(self.MINUScheck)[2]) / 2, (self.c.coords(self.MINUScheck)[1] + self.c.coords(self.MINUScheck)[3]) / 2, text="-", anchor="c")
        self.PLUStext = self.c.create_text((self.c.coords(self.PLUScheck)[0] + self.c.coords(self.PLUScheck)[2]) / 2, (self.c.coords(self.PLUScheck)[1] + self.c.coords(self.PLUScheck)[3]) / 2, text="+", anchor="c")
        self.DLtext = self.c.create_text((self.c.coords(self.DLcheck)[0] + self.c.coords(self.DLcheck)[2]) / 2, (self.c.coords(self.DLcheck)[1] + self.c.coords(self.DLcheck)[3]) / 2, text="\u003c", anchor="c")
        self.DRtext = self.c.create_text((self.c.coords(self.DRcheck)[0] + self.c.coords(self.DRcheck)[2]) / 2, (self.c.coords(self.DRcheck)[1] + self.c.coords(self.DRcheck)[3]) / 2, text="\u1433", anchor="c")
        self.DUtext = self.c.create_text((self.c.coords(self.DUcheck)[0] + self.c.coords(self.DUcheck)[2]) / 2, (self.c.coords(self.DUcheck)[1] + self.c.coords(self.DUcheck)[3]) / 2, text="\u1431", anchor="c")
        self.DDtext = self.c.create_text((self.c.coords(self.DDcheck)[0] + self.c.coords(self.DDcheck)[2]) / 2, (self.c.coords(self.DDcheck)[1] + self.c.coords(self.DDcheck)[3]) / 2, text="\u142f", anchor="c")
        self.mouse = Controller()
        print(self.stickcpos, "\u2302", "\u2324", "\u2334", "\u003c")
        self.c.pack()
        self.c.update()
        self.root.after(1, self.after)
        self.root.mainloop()



    def after(self):
        with open("/dev/input/js0", "rb") as self.control:
            self.control.read(168)
            while True:
                self.id = self.control.read(8).hex()
                if self.id[-4:-2] == "02":
                    self.vertical = self.id[-8:-6]
                    self.horizontal = self.id[-6:-4]
                    self.vertical = int(self.vertical, 16)
                    self.horizontal = int(self.horizontal, 16)
                    if self.horizontal > 127:
                        self.horizontal -= 256
                    if self.vertical > 127:
                        self.vertical -= 128
                    self.vstickpos = (self.cy - 133) + self.vertical
                    """
                    if self.id[-2:] == "00":
                        self.mouse.move(self.horizontal, 0)
                    elif self.id[-2:] == "01":
                        self.mouse.move(0, self.horizontal)
                    """
                    self.vertical += self.cy
                    if self.id[-2:] in ["00", "01"]:
                        if self.id[-2:] == "00":
                            self.horizontal += self.censtickpos[0]
                            self.c.coords(self.stick, self.horizontal - 5, self.cy - 5, self.horizontal + 5, self.cy + 5)
                        else:
                            self.horizontal += self.censtickpos[1]
                            self.c.coords(self.stick, self.censtickpos[0] - 5, self.horizontal - 5, self.censtickpos[0] + 5, self.horizontal + 5)
                    if self.id[-2:] in ["02", "03"]:
                        if self.id[-2:] == "02":
                            self.horizontal += self.censtickpos2[0]
                            self.c.coords(self.stick2, self.horizontal - 5, self.cy - 5, self.horizontal + 5, self.cy + 5)
                        else:
                            self.horizontal += self.censtickpos2[1]
                            self.c.coords(self.stick2, self.censtickpos2[0] - 5, self.horizontal - 5, self.censtickpos2[0] + 5, self.horizontal + 5)
                """
                elif self.id[-2:] == "01":
                    self.mouse.click(Button.left, 1)
                elif self.id[-2:] == "00":
                    self.mouse.click(Button.right, 1)
                elif self.id[-2:] == "02":
                    self.mouse.click(Button.middle, 1)
                elif self.id[-2:] == "03":
                    self.mouse.click(Button.left, 2)
                elif self.id[-2:] == "04":
                    self.mouse.click(Button.scroll_down, 1)
                elif self.id[-2:] == "05":
                    self.mouse.click(Button.scroll_up, 1)
                """
                if self.id[-8:-6] == "01":
                    if self.id[-4:] == "0100":
                        self.c.itemconfig(self.Bcheck, fill="#ff0000")
                    if self.id[-4:] == "0101":
                        self.c.itemconfig(self.Acheck, fill="#ff0000")
                    if self.id[-4:] == "0102":
                        self.c.itemconfig(self.Xcheck, fill="#ff0000")
                    if self.id[-4:] == "0103":
                        self.c.itemconfig(self.Ycheck, fill="#ff0000")
                    if self.id[-4:] == "0104":
                        self.c.itemconfig(self.Lcheck, fill="#ff0000")
                    if self.id[-4:] == "0105":
                        self.c.itemconfig(self.Rcheck, fill="#ff0000")
                    if self.id[-4:] == "0106":
                        self.c.itemconfig(self.ZLcheck, fill="#ff0000")
                    if self.id[-4:] == "0107":
                        self.c.itemconfig(self.ZRcheck, fill="#ff0000")
                    if self.id[-4:] == "0108":
                        self.c.itemconfig(self.MINUScheck, fill="#ff0000")
                    if self.id[-4:] == "0109":
                        self.c.itemconfig(self.PLUScheck, fill="#ff0000")
                    if self.id[-4:] == "010a":
                        self.c.itemconfig(self.HOMEcheck, fill="#ff0000")
                    if self.id[-4:] == "010b":
                        self.c.itemconfig(self.stick, fill="#ff0000", outline="#ff0000")
                    if self.id[-4:] == "010c":
                        self.c.itemconfig(self.stick2, fill="#ff0000", outline="#ff0000")
                    if self.id[-4:] == "010d":
                        self.c.itemconfig(self.DUcheck, fill="#ff0000")
                    if self.id[-4:] == "010e":
                        self.c.itemconfig(self.DDcheck, fill="#ff0000")
                    if self.id[-4:] == "010f":
                        self.c.itemconfig(self.DLcheck, fill="#ff0000")
                    if self.id[-4:] == "0110":
                        self.c.itemconfig(self.DRcheck, fill="#ff0000")
                if self.id[-8:-6] == "00":
                    if self.id[-4:] == "0100":
                        self.c.itemconfig(self.Bcheck, fill="#ffffff")
                    if self.id[-4:] == "0101":
                        self.c.itemconfig(self.Acheck, fill="#ffffff")
                    if self.id[-4:] == "0102":
                        self.c.itemconfig(self.Xcheck, fill="#ffffff")
                    if self.id[-4:] == "0103":
                        self.c.itemconfig(self.Ycheck, fill="#ffffff")
                    if self.id[-4:] == "0104":
                        self.c.itemconfig(self.Lcheck, fill="#ffffff")
                    if self.id[-4:] == "0105":
                        self.c.itemconfig(self.Rcheck, fill="#ffffff")
                    if self.id[-4:] == "0106":
                        self.c.itemconfig(self.ZLcheck, fill="#ffffff")
                    if self.id[-4:] == "0107":
                        self.c.itemconfig(self.ZRcheck, fill="#ffffff")
                    if self.id[-4:] == "0108":
                        self.c.itemconfig(self.MINUScheck, fill="#ffffff")
                    if self.id[-4:] == "0109":
                        self.c.itemconfig(self.PLUScheck, fill="#ffffff")
                    if self.id[-4:] == "010a":
                        self.c.itemconfig(self.HOMEcheck, fill="#ffffff")
                    if self.id[-4:] == "010b":
                        self.c.itemconfig(self.stick, fill="#000000", outline="#000000")
                    if self.id[-4:] == "010c":
                        self.c.itemconfig(self.stick2, fill="#000000", outline="#000000")
                    if self.id[-4:] == "010d":
                        self.c.itemconfig(self.DUcheck, fill="#ffffff")
                    if self.id[-4:] == "010e":
                        self.c.itemconfig(self.DDcheck, fill="#ffffff")
                    if self.id[-4:] == "010f":
                        self.c.itemconfig(self.DLcheck, fill="#ffffff")
                    if self.id[-4:] == "0110":
                        self.c.itemconfig(self.DRcheck, fill="#ffffff")
                self.c.update()



if __name__ == "__main__":
    game = Main()
