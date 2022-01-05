import threading
import time

from functions.build_and_display import BuildDisplay

from config.parameters import timer, timer_on


class Timer:
    def __init__(self):
        self.timer_on = timer_on
        self.running_display = False

    def timer_flip(self):
        self.timer_on = not self.timer_on


TimerControl = Timer()


def timer_image():
    while True:
        if TimerControl.timer_on:
            if not TimerControl.running_display:
                TimerControl.running_display = True
                refresh_run = BuildDisplay(show_image=False)
                refresh_run.run_neural_transfer()
                refresh_run.display_to_ink()
                TimerControl.running_display = False
                time.sleep(timer)


t = threading.Thread(target=timer_image)
t.start()
