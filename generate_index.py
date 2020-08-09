
# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt
from about_generator import generate_about_text



def generate_page(head, body):
    page = "<html>" + head + body + "</html>"
    return page

def generate_head(title):
    head = "<head><meta charset=\'utf-8\'>"
    head += "<title>" + title + "</title>"
    head += "</head>"
    return head


def generate_body(header, paragraphs):
    body = "<h1>" + header + "</h1>"
    for p in paragraphs:
        body = body + "<p>" + p + "</p>"
    body += "<a href='about.html'>О чем все это?</a>"
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

############## GENERATE ABOUT PAGE ################



def generate_about_body(header, paragraphs):
    body = "<h1>" + header + "</h1>"
    for p in paragraphs:
        body = body + "<p>" + p + "</p>"
    body += "<a href='about.html'>О чем все это?</a>"
    return "<body>" + body + "</body>"
    

def generate_about_page(title, header, paragraphs):
    fp = open("about.html", "w")
    page = generate_page(
        head = generate_head(title),
        body = generate_body(header=header, paragraphs = paragraphs)
    )
    print(page, file=fp)
    fp.close()


generate_about_page(
    title = "О чем все это?",
    header = "О чем все это?",
    paragraphs = "<img src='logo.png'>" + generate_about_text()
)    
print(" ")
