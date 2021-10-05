from trello import TrelloClient
import pandas as pd

def getData():
    API_KEY = ""
    TOKEN = ""

    with open("data.txt", "r") as f1:
        contents1 = f1.read()
        if "|" not in contents1:
            f1.close()
            return 1
        API_KEY = contents1.split(" | ")[0]
        TOKEN = contents1.split(" | ")[1]
    f1.close()

    client = TrelloClient(
        api_key = API_KEY,
        token = TOKEN
    )

    try:
        all_boards = client.list_boards()
    except Exception as e:
        return 1

    nameList = []
    nameCard = []
    attach = []
    try:
        for myboard in all_boards:
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


