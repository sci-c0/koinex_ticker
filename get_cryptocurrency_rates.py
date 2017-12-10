import pycurl
from StringIO import StringIO

target_URL = "https://koinex.in/api/ticker"

def fetch_data(URL):

    proceed = True

    buffer = StringIO()
    c = pycurl.Curl()
    body = ''

    if(proceed == True):
        try:
            c.setopt(c.URL, URL)
        except TypeError as e:
            print(repr(e))
            proceed = False
        except pycurl.error as pe:
            print(repr(pe))
            proceed = False

    if(proceed == True):
        try:
            c.setopt(c.WRITEDATA, buffer)
        except TypeError as e:
            print(repr(e))
            proceed = False
        except pycurl.error as pe:
            print(repr(pe))
            proceed = False
    
    if(proceed == True):
        try:
            c.perform()
        except pycurl.error as pe:
            print(repr(pe))
            proceed = False
    
    if(proceed == True):
        try:
            body = buffer.getvalue()
        except UnicodeError as e:
            print(repr(e))
            proceed = False
    
    c.close()
    buffer.close()

    return body

def main():
    
    body = fetch_data(target_URL)
    print(body)

if __name__ == "__main__":
    main()

