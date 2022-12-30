from PIL import Image

from functions.file_loader import FileHandlerInstance

# this is here so the code can be run on anything, otherwise a non-RPi or a Pi without an inky HAT will fail
try:
    from inky.inky_uc8159 import Inky

    inky = Inky()

    inky_online = True
except ModuleNotFoundError:
    print("Not running on a Pi or inky HAT not installed")
    inky_online = False

saturation = 0.5


# the random parameter determines whether a random image is chosen from outputs or the filename is used
def display_inky(file_time, random_existing=False):
    """
    This function displays the image to the inky display
    :param file_time:
    :param random_existing:
    :return:
    """
    if random_existing:
        image_pre = Image.open(FileHandlerInstance.get_random_file())
    else:
        image_pre = Image.open(FileHandlerInstance.get_specific_file(file_name=f"final_{file_time}.jpeg"))
    size = 640, 400
    image = image_pre.resize(size, Image.ANTIALIAS)

    if inky_online:
        inky.set_image(image, saturation=saturation)
        inky.show()
