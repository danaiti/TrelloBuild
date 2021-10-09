from trello import TrelloClient
import pandas as pd
import requests
from lib import uploadTrelloData as ul

API_KEY = ""
TOKEN = ""
all_boards = None
client = None

def getKey():
    global API_KEY
    global TOKEN
    global client

    with open("lib/data.txt", "r") as f1:
        contents1 = f1.read()
        if "-" not in contents1:
            f1.close()
            return 1
        API_KEY = contents1.split("-")[0]
        TOKEN = contents1.split("-")[1]

        client = TrelloClient(
            api_key = API_KEY,
            token = TOKEN
    )
    f1.close()

def getAllBoard(client):
    global all_boards
    try:
        all_boards = client.list_boards()
        print(type(all_boards))
        return 0
    except Exception as e:
        return 1

def create_list(list_name):
    getKey()
    global client
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"name": list_name, "key": API_KEY, "token": TOKEN}
    response = requests.request("POST", url, params=querystring)
    list_id = response.json()["id"]
    return list_id

def getData():
    getKey()
    global all_boards
    global client
    if getAllBoard(client) == 1:
        return 1
    else:
        nameList = []
        nameCard = []
        attach = []
        try:
            for myboard in all_boards:
                print(myboard)
                if "_ignore" not in myboard:
                    for list in myboard.all_lists():
                        for card in list.list_cards():
                            #here
                            hasAtt = False
                            for atc in card.attachments:
                                hasAtt = True
                                attach.append(atc.get('url'))

                            if(hasAtt):
                                nameCard.append(card.name)
                                nameList.append(list.name)

            df = pd.DataFrame({'Product Name':nameCard, 'Img': attach, 'Product Type': nameList})
            df.to_csv('products.csv', index=False, encoding='utf-8')
        except Exception as e2:
            return 2
        return 0

def uploadData(fileName,idBoard):
    getKey()
    return ul.readDataFromCsv(fileName,idBoard,API_KEY, TOKEN)


