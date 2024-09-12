import os
from PIL import Image

# the directory where my .webp images are stored
directory = "/Users/smitm/Downloads/us_home"

# list all files in the directory e.g., ['img1.webp','img2.webp']
files = os.listdir(directory)

for index, file in enumerate(files, start=1):
    if file.endswith(".webp"):

        # open the .webp image
        # join() joins all items in iterable into one string
        # e.g., '/Users/smitm/Downloads/us_home' + '/us home 1.webp'
        # to '/Users/smitm/Downloads/us_home/us home 1.webp'
        img = Image.open(os.path.join(directory, file))

        # convert opened image to RGB mode (webp may have transparency)
        img = img.convert("RGB")

        # renaming the image
        new_name = f"US_HOME_{index}.jpg"

        # save the image as .jpg
        img.save(os.path.join(directory, new_name), "JPEG")

        # removes old .webp image (optional! Because I don't want it anymore)
        os.remove(os.path.join(directory, file))

print("Files converted")
