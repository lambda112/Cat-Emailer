import smtplib
from random import randint 
from httpx import get
from get_html import find_images

divs = find_images()
def get_images():
    images = [i.attrs["src"] for i in divs]
    return images

images = get_images()
count = 0

for img in images:
    count += 1
    img = get(img)

    with open(f"catfolder\cat_images{count}.png", "wb") as file:
        file.write(img.content)

