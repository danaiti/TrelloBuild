from datetime  import datetime
import requests
from csv import reader
def create_board(key, token):

    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    board_name = "SanPham" + current_time
    print(board_name)
    url = "https://api.trello.com/1/boards/"
    querystring = {"name": board_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    print (response.json()["shortUrl"])
    board_id = response.json()["shortUrl"].split("/")[-1].strip()
    return board_id

def create_list(key, token ,board_id, list_name):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"name": list_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    list_id = response.json()["id"]
    return list_id

def create_card(key, token, list_id, card_name):
    url = f"https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": list_id, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id

def readDataFromCsv(key, token):
    try:
        board_id = create_board(key, token)
        with open("dataImport.csv", "r") as f1:
            csv_reader = reader(f1)
            listName = 'fakeList'
            cardName = 'fakeCard'
            for row in csv_reader:
                if row[0] != '':
                    listName = row[0]
                    list_id = create_list(key, token, board_id, listName)
                    create_card(key, token, list_id, row[1])
                elif row[1] != '':
                    create_card(key, token, list_id, row[1])
        return board_id
    except Exception as e:
        return "err"

