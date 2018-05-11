import requests

def main():
    print_header()
    code = input("Enter your zip-code: ")
    html = get_html_from_web(code)
    # parse the html
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


if __name__ == '__main__':
    main()