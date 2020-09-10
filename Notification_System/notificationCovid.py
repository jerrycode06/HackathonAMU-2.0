from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "icon.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text

def states():
    lst = ['Uttar Pradesh','Delhi','Jammu and Kashmir']
    return lst

if __name__ == "__main__":
    
    while True:
        htmlData = getData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(htmlData, 'html.parser')
        soup.prettify()

        dataStr = ''
        for table in soup.find_all('tbody'):
            dataStr += table.get_text()
        dataStr = dataStr[1:]
        lst = dataStr.split('\n\n')
        
        states = states()
        for i in lst[0:31]:
            final = i.split('\n')
            final = final[1:]
            
            if final[1] in states:
                title = 'Covid-19 cases'
                msg = f"{final[1]}:\n Total : {final[2]}:\n Deaths : {final[3]}:\n Recovered : {final[4]}"
                notify(title,msg)
                time.sleep(8)

        time.sleep(3600)