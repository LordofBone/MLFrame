### Setup

###### Pre-requisites

Before installing anything with pip it is good practice to set up a virtual environment:
https://python.land/virtual-environments/virtualenv

To install everything on an x86-64 Linux system or Windows you should just be able to run:

__pip3 install -r requirements.txt__

For Raspberry Pi, however (where this is meant to be run) you will need to get the PyTorch wheels from elsewhere:

__sudo ./install.sh__

This will download the python3.7 pytorch wheels and build them, then run requirements.txt through pip.

On Raspberry Pi this is meant to run with the inky 7 colour HAT:
https://shop.pimoroni.com/products/inky-impression-4

Then with the inky hat on, run:

__curl https://get.pimoroni.com/inky | bash__

And follow the instructions.

It should now hopefully be ready to go.

### Running

###### Testing

To kick off a test:

__python3 test_run.py__

It will then generate a Neural Transfer image based on the demo image and style included.

If you add more images to the input and style folders this test will randomly pick both.

###### Normal running - button controls

To run the main Frame code:

__python3 main.py__

And first off the Frame will generate an image with the timer on, configurable under:

config/parameters.py

When the timer expires (default 10 minutes) another image will be generated.

The buttons should be facing the left side of the frame.

The top button will refresh and generate a new image - as long as a generation is not currently in progress.

The second button down currently has no function.

The third button down will de-activate the timer so the current image will stay.

The fourth (bottom) button will shut the Frame down.

While the frame is running it will randomly pick from the images, randomly pick a style then generate a neural transfer
from that; then display it. You can add images to "images/input" and "images/style" and it will pick up on them randomly
while the code is running.