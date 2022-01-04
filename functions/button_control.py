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
B = 6
TIMER = 16
SHUTDOWN = 24

BOUNCE = 300

repeat_status = {
    REFRESH: False,
    B: False,
    TIMER: False,
    SHUTDOWN: False,
}


def on(buttons, bounce=BOUNCE):
    """Handle a joystick direction or button push
    Decorator. Use with @joystick.on(joystick.UP)
    :param buttons: List, or single instance of joystick button constant
    :param bounce: Debounce delay in milliseconds: default 300
    """

    buttons = buttons if isinstance(buttons, list) else [buttons]

    def register(handler):
        for button in buttons:
            GPIO.remove_event_detect(button)
            GPIO.add_event_detect(button, GPIO.FALLING, callback=handler, bouncetime=bounce)

    return register


def millis():
    """Return the current time in milliseconds."""
    return int(round(time.time() * 1000))


def repeat(button, handler, delay=0.1, ramp=1.0):
    """Detect a held direction and repeat
    If you want to hold a direction and have it auto-repeat,
    call this within a joystick direction handler.
    :param button: Joystick button constant to watch
    :param handler: Function to call every repeat
    :param delay: Delay, in seconds, before repeat starts and between each repeat
    :param ramp: Multiplier applied to delay after each repeat, 1.0=linear speed up
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
up = GPIO.setup(REFRESH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
down = GPIO.setup(B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
left = GPIO.setup(TIMER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
right = GPIO.setup(SHUTDOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
