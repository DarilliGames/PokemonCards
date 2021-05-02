import requests 

#           For Calling ALL sets
# response = requests.get("https://api.pokemontcg.io/v2/sets")
# response = requests.get("https://api.pokemontcg.io/v2/cards/base1-1")

# print(response.json())


def callAPI(theString):
    req = "https://api.pokemontcg.io/v2/"+theString
    response = requests.get(req)
    return response.json()
    

def loadCard(set, num):
    theString = "cards/" + set +"-"+ num
    return callAPI(theString)

def writeSetToTextFile(cardSet):
    setInfo = callAPI("sets/" + cardSet)
    cards = []
    file_object = open(cardSet+".txt", 'a')
    for x in range(1, setInfo["data"]["total"]+1):
        print(x)
        card = loadCard(cardSet, str(x))
        card = card["data"]
        file_object.write(card["name"]+"\n")
    file_object.close()
    print("Wrote Set")

def writeSet(cardSet, total):
    setInfo = callAPI("sets/" + cardSet)
    cards = []
    for x in range(1, total+1):
        print(x)
        card = loadCard(cardSet, str(x))
        card = card["data"]
        cards.append([card["name"], "", ""])
    return cards

def createSet(setCode, SHEET):
    set_info = callAPI("sets/"+setCode["setId"])["data"]
    print(set_info)
    print(setCode)
    total = set_info["total"]
    cards = writeSet(setCode["setId"], total)
    aaa = SHEET.add_worksheet(setCode["name"], set_info["total"], 3)
    aaa.update("A1:C"+str(total), cards)

# allSets = [
#     "BaseSet", "Jungle", "Fossil", "BaseSet2", "Rocket", "GymHeroes", "GymChallenge", "BlackStarPromo"
# ]



# from allsetshere import allSets

# def insertListOfSets():
#     for i in range(len(allSets)):
#         theSet = {
#             "name": allSets[i]["name"],
#             "setSort": i+1,
#             "setId": allSets[i]["id"]
            
#         }
#         mongo.db.sets.insert_one(theSet)





#       Using Set id from the set API call.  call the function to get write to txt file
# writeSet("neo1")


#       When moving this to flask, the API will write directly to google sheets - but that is future me's problem
