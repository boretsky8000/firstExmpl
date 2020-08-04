# coding: utf-8
#/.github/workflows/python-package.yml
print("Content-Type: text/html\n\n")

from horoscope import generate_prophecies
from datetime import datetime as dt



def generate_page(head, body):
    page = "<html>" + head + body + "</html>"
    return page

def generate_head(title):
    head = f"""<head>
	<meta charset='utf-8'>
	<title>{title}</title>
	</head>
	"""
    return head


def generate_body(header, paragraphs):
    body = "<h1>" + header + "</h1>"
    for p in paragraphs:
        body += "<p>" + p + "</p>"
    return "<body>" + body + "</body>"

def save_page(title, header, paragraphs, output="index.html"):
    fp = open(output, "w", encoding="utf-8")
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, paragraphs = paragraphs)
    )
    print(page, file=fp)
    fp.close()

today = dt.now().date()
save_page(
    title = "Гороскоп на сегодня",
    header = "Ваш гороскоп на " + str(today) + ":",
    paragraphs = generate_prophecies()

)

print(" ")
