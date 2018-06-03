import bs4
import requests
import collections
import datetime
import re

def main():
    print_header()
    html = get_html_from_web()

    # parse the html
    report = get_traffic_list_from_html(html)

    print("{} um {}".format (
        report, datetime.datetime.now()
    ))

def print_header():
    print("----------------------------")
    print("-  Traffic Messages Client -")
    print("----------------------------")
    print()


def get_html_from_web():
    url = "http://www.radiobremen.de/bremenvier/programm/vier-news/verkehr130.html"
    response = requests.get(url)
    return response.text


def get_traffic_list_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    # print(soup)
    soup.find(id='verlauf_inner_content')
    title = soup.find(id='verlauf_inner_content').find('h1').get_text()
    title = cleanup(title)
    for x in soup.find_all(class_='verkehr'):
        print(cleanup(x.get_text()))
        print("********************")
    return title


def cleanup(text : str):
    if not text:
        return text

    text = re.sub(r"\s+", " ", text, flags=re.UNICODE)
    return text



if __name__ == '__main__':
    main()