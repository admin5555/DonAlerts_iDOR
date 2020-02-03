import requests
from random import randrange


while True:
    url = "http://static.donationalerts.ru/audiodonations/"
    rint1 = randrange(11111, 99999)
    url = url + str(rint1) + '/'
    rint2 = randrange(111,999)
    url = url + str(rint1) + str(rint2) + ".wav"
    try:
        req = requests.get(url)
        st = req.status_code
        if st == 200:
            print("connection done! " + url)
            with open('result.txt', 'a') as file: # Saving result to result.txt
                file.write(url + '\n')
    except:
        pass
    
