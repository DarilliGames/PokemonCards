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

def writeSet(cardSet):
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
