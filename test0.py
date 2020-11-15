from WiiUPro import Remote
import WiiUPro
import os
remote = Remote()

def func(event):
    print("hello: ", event.button, event.on, event.buttonid)



def ouch(event):
    os.system("aplay se_item_homerunbat_l.wav")

remote.create_callback(WiiUPro.ANY, func, on=WiiUPro.RELEASE)
remote.create_callback(WiiUPro.ANY, func, on=WiiUPro.PRESS)
remote.create_callback(WiiUPro.L, ouch, on=WiiUPro.PRESS)


while True:
    remote.update()
