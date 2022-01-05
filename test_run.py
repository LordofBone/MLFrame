from functions.build_and_display import BuildDisplay
import logging

if __name__ == "__main__":
    logger = logging.getLogger("frame-logger")
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Beginning test")
    test_run = BuildDisplay(show_image=True)
    test_run.run_neural_transfer()
    test_run.display_to_ink()
