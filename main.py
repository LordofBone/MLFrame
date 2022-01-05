import logging
import os
from time import sleep

import functions.button_control as nav
from functions.build_and_display import BuildDisplay
from functions.timer_control import TimerControl
from config.parameters import log_level

logger = logging.getLogger("frame-logger")
logging.basicConfig(level=log_level)


@nav.on(nav.REFRESH)
def refresh_image(pin):
    logger.info("Refresh button pressed")
    if not TimerControl.running_display:
        TimerControl.running_display = True
        logger.info("Currently not generating anything, running a generation")
        ml_image = BuildDisplay(show_image=False)
        ml_image.run_neural_transfer()
        ml_image.display_to_ink()
        logger.info("Generation complete and displayed")
        TimerControl.running_display = False


@nav.on(nav.RANDOMPIC)
def random_pic(pin):
    logger.info("Random picture button pressed")
    if not TimerControl.running_display:
        TimerControl.running_display = True
        logger.info("Currently not generating anything, displaying a random previously generated image")
        ml_image = BuildDisplay(show_image=False)
        ml_image.display_random_to_ink()
        logger.info("Random image displayed")
        TimerControl.running_display = False


@nav.on(nav.TIMER)
def timer_on_off(pin):
    logger.info("Timer button pressed")
    TimerControl.timer_flip()
    logger.info(f"Timer on switched to: {TimerControl.timer_on}")


@nav.on(nav.SHUTDOWN)
def shutdown_pi(pin):
    logger.info("Shutdown button pressed")
    os.system("sudo shutdown now")
    logger.info("Shutting down")
    sleep(0.2)


while 1:
    sleep(0.05)
