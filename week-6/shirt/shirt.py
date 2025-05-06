import sys
from PIL import Image, ImageOps
import os
if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

ex1 = os.path.splitext(sys.argv[1])[1].lower()
ex2 = os.path.splitext(sys.argv[2])[1].lower()

if ex1 not in ['.jpg', 'jpeg', 'png']:
    sys.exit('Invalid input')
elif ex2 not in ['.jpg', '.jpeg', '.png']:
    sys.exit('Invalid output')
if ex1 != ex2:
    sys.exit('Input and output have different extensions')
try:
    photo = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(photo, size, Image.Resampling.BICUBIC, 0,(0.5, 0.5))
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])
except FileNotFoundError:
    sys.exit('Input does not exist')
