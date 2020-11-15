import sys
buttons_pressed = []
buttons_not_pressed = []


def average(nums):
    sum_nums = sum(nums)
    return sum_nums / len(nums)


with open("/dev/input/js0", "rb") as controller:
    while True:
        try:
            button = int(controller.read(8).hex()[-8:-6], 16)
            if not button in buttons_pressed:
                buttons_pressed.append(button)
        except KeyboardInterrupt:
            for button_id in range(0, 255):
                if not button_id in buttons_pressed:
                    buttons_not_pressed.append(button_id)
            print(*buttons_not_pressed, "Amount of buttons NOT pressed", len(buttons_not_pressed), "Amount of buttons that WERE pressed", len(buttons_pressed))
            print("\n\n\n\n\n\n\n\n", "Range:", str(min(buttons_pressed)) + "-" + str(max(buttons_pressed)), "Average:", average(buttons_pressed))
            sys.exit()

