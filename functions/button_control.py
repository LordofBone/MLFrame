try:
    import RPi.GPIO as GPIO
except ImportError:
    exit("This library requires the RPi.GPIO module\nInstall with: sudo pip install RPi.GPIO")

import time

"""
Thanks to the inky HAT examples code and also the code for the display-o-tron HAT:
https://github.com/pimoroni/displayotron/blob/master/examples/dot3k/advanced/game.py
https://github.com/pimoroni/displayotron/blob/master/library/dot3k/joystick.py
https://github.com/pimoroni/inky/blob/master/examples/7color/buttons.py
"""

# Set up RPi.GPIO with the "BCM" numbering scheme
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

REFRESH = 5
RANDOMPIC = 6
TIMER = 16
SHUTDOWN = 24

BOUNCE = 300

repeat_status = {
    REFRESH: False,
    RANDOMPIC: False,
    TIMER: False,
    SHUTDOWN: False,
}


def on(buttons, bounce=BOUNCE):
    """
    This is the main program loop and button functions
    """

    buttons = buttons if isinstance(buttons, list) else [buttons]

    def register(handler):
        for button in buttons:
            GPIO.remove_event_detect(button)
            GPIO.add_event_detect(button, GPIO.FALLING, callback=handler, bouncetime=bounce)

    return register


def millis():
    """
    Return the current time in milliseconds
    :return:
    """
    return int(round(time.time() * 1000))


def repeat(button, handler, delay=0.1, ramp=1.0):
    """
    Repeat a button press handler after a delay
    :param button:
    :param handler:
    :param delay:
    :param ramp:
    :return:
    """
    if repeat_status[button]:
        return False
    repeat_status[button] = True
    last_trigger = millis()
    while GPIO.input(button) == 0:
        m = millis()
        if m - last_trigger >= (delay * 1000):
            handler()
            delay *= ramp
            last_trigger = m
    repeat_status[button] = False


# Buttons connect to ground when pressed, so we should set them up
# with a "PULL UP", which weakly pulls the input signal to 3.3V.
GPIO.setup(REFRESH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RANDOMPIC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TIMER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SHUTDOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
