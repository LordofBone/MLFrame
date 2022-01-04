wget https://wintics-opensource.s3.eu-west-3.amazonaws.com/torch-1.3.0a0%2Bdeadc27-cp37-cp37m-linux_armv7l.whl
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1nhk7PKDUzcmGGwnx7PK7iW3__2fOJVl1' -O torchvision-0.4.0a0+d31eafa-cp37-cp37m-linux_armv7l.whl
pip3 install torch-1.3.0a0+deadc27-cp37-cp37m-linux_armv7l.whl
pip3 install torchvision-0.4.0a0+d31eafa-cp37-cp37m-linux_armv7l.whl
pip3 install -r requirements.txt