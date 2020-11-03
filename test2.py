import WiiUPro
from sys import argv


inputs = []


while True:
    inputs = WiiUPro.get_buttons(inputs, num=argv[1])
    if "A" in inputs:
        print("A")
    print(inputs)
