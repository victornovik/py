import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Install smtp server in docker image locally
# docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev

# Install smtp server as a global .NET tool locally
# dotnet tool install -g Rnwood.Smtp4dev

tmpl = Template(Path("email_templates/index.html").read_text())
html = tmpl.substitute({"name": "Victor", "date": "tomorrow"})

em = EmailMessage()
em["from"] = "Python"
em["to"] = "victor.novik@mail.ru"
em["subject"] = "My photo"
em.set_content(html, "html")

with open("images/VictorNovik.JPG", "rb") as img:
    img_data = img.read()
    em.add_attachment(img_data, maintype="image", subtype="jpg", filename="VictorNovik.JPG")

with smtplib.SMTP(host="localhost", port=2525) as smtp:
    smtp.ehlo()
    smtp.send_message(em)
    print("Email was sent")
    # smtp.starttls()
    # smtp.login("username", "password")
