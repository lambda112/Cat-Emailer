import smtplib
from random import randint 
from httpx import get
from get_html import find_images
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Collect src from images
def get_images():
    divs = find_images()
    images = [i.attrs["src"] for i in divs]
    return images

# Save images
def save_images():
    images = get_images()
    count = 0
    for img in images:

        # Get content of source in bytes
        count += 1
        img = get(img)

        # Write images to file
        with open(f"catfolder\cat_images{count}.png", "wb") as file:
            file.write(img.content)


# Get a random image located in folder
with open(f"catfolder\cat_images{randint(1,24)}.png", "rb") as file:
    image = file.read()

# Email image 
msg = MIMEMultipart()
msg['Subject'] = 'Automated Message by James From Team Rocket'
msg['From'] = "lambdaa112@gmail.com"
msg['To'] = 'kamazim121212@gmail.com'
image = MIMEImage(image)
msg.attach(image)
print("added attachment")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = "lambdaa112@gmail.com", password = "moyn eugt kmga xrck")
    print("logged in")
    connection.sendmail(from_addr="lambdaa112@gmail.com", to_addrs="kamazim121212@gmail.com", msg = msg.as_bytes())
    print("sent email")