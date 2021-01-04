# Import the pillow package for image handling
from PIL import Image, ImageFont, ImageDraw
# Import random and string for random name generation
import random
import string

class image:
    # Initializing class
    def __init__(self, im, txt="example"): # Variable txt preset (mainly for testing purposes)
        self.im = Image.open(f"templates/{im}") # Opening image from the templates folder
        self.im_draw = ImageDraw.Draw(self.im) # Drawing the image to a variable for the later writing of text
        self.txt = txt # Text to be put on the meme
        self.txt_len = len(txt) # Length of the text

    def set_txt(self, txt):
        self.txt = txt # Changing the value of the self.txt variable
        print("Reset \"txt\" variable to", txt) # Printing to the screen

    def reset(self):
        # Pasting a black rectangle exactly matching the area where text is put
        # In order to reset the picture to and add more text
        self.im.paste(Image.new('RGB', (621, 63), (0, 0, 0)), (274, 752))

    def show(self):
        # Showing image (mainly debugging/testing purposes)
        self.im.show()
        print("Showing image...") # Printing confirmation to the screen

    def write(self, x=285, y=768, r=275, g=255, b=255): # Preset values (but still able to change for debugging purposes)
        font = ImageFont.truetype('fonts/ArialCE.ttf', self.txt_len*5) # Select arial as the font
        self.im_draw.text((x, y), self.txt, (r, g, b), font=font) # Drawing text on the image
        print("Text drawn!") # Printing confirmation to the screen

    def save(self):
        rand_name = ''.join(random.choice(string.ascii_letters) for i in range(15)) # Generating random name
        self.im.save(f"downloaded/{rand_name}.jpg") # Saving the image to the downloaded directory

        print("Image saved as", rand_name) # Printing confirmation to the screen
        return rand_name # Returning random name for later deletion of the image

# TODO
# Actually utilize the benefits of OOP by adding subclasses for each template
# Use polymorphism with the write() and reset() methods
# Add more meme templates
# Robust error handling when inputting strings       
