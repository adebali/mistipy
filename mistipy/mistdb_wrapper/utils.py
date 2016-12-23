import requests
# from config import Config
# from mistdb_wrapper import config

session = requests.Session()
session.params = {}


def streamElements(basic_url, elementLimit, elementStart):
    elementNumberPerPage = 30
    page = int((elementStart-1)/elementNumberPerPage)
    elementNumber = elementStart
    elementAvailable = True
    while elementAvailable:
        page += 1
        forechar = '&' if '?' in basic_url else '?'
        url = basic_url + forechar + 'page=' + '{}'.format(page)
        response = session.get(url)
        result = response.json()
        if result == []:
            elementAvailable = False
        else:
            for element in result:
                if elementNumber <= elementLimit:
                    yield element
                else:
                    elementAvailable = False
                    break
                elementNumber += 1


def noQuote(string, replaceWith='_'):
    return string.replace("\"", replaceWith).replace("'", replaceWith)
