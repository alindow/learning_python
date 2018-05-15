import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'loc, temp, cond')

def main():
    print_header()
    code = input("Enter your zip-code: ")
    html = get_html_from_web(code)

    # parse the html
    get_weather_from_html(html)

    report = get_weather_from_html(html)

    print("The temperature in {} is {} and {}".format (
        report.loc,
        report.temp,
        report.cond
    ))
    # display for the forecast
    print("Hello from main")


def print_header():
    print("----------------------------")
    print("-  Weather Forecast Client -")
    print("----------------------------")
    print()


def get_html_from_web(code):
    url = "https://www.wunderground.com/weather-forecast/{}".format(code)
    response = requests.get(url)
    return response.text



def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    loc = soup.find(class_='city-header').find('h1').get_text()
    loc = cleanup(loc)
    loc = find_city_and_state(loc)
    cond = soup.find(class_='condition-icon').get_text()
    cond = cleanup(cond)
    temp = soup.find(class_='current-temp').get_text()
    temp=cleanup(temp)
    temp = find_temp_and_scale(temp)
    # return loc,cond,temp
    report = WeatherReport(cond=cond, temp = temp, loc = loc)
    return report

def find_city_and_state(loc:str):
    parts = loc.split('\n')
    return parts[0].strip()


def find_temp_and_scale(temp:str):
    parts = temp.split('\n')
    return parts[0].strip() + "°" +parts[1].strip()


def cleanup(text : str):
    if not text:
        return text

    text = text.strip()
    return text



if __name__ == '__main__':
    main()