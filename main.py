import smtplib
from get_html import find_images


divs = find_images()

def get_images():
    images = [i.attrs["src"] for i in divs]
    return images

print(get_images())