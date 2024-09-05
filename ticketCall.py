import requests
import json

api_key = #Enter API key here
password = #Enter account password here
apiURL = #Enter API URL here


def getRCOpen(): #requester_id is 81017809495
    pageOne = requests.get(apiURL + 'tickets', auth = (api_key, password))

    pageOne = pageOne.json()
    RCOpen = []
    
    for i in range(len(pageOne)):
        currentItem = pageOne[i]
        if currentItem['requester_id'] == 81017809495 and currentItem['status'] == 2:
            RCOpen.insert(0, currentItem['id'])
        else:
            pass
        
    return len(RCOpen)
    
def getFRDue(): #check fr_escalated field
    pageOne = requests.get(apiURL + 'tickets', auth = (api_key, password))

    pageOne = pageOne.json()
    FRDue = []
    
    for i in range(len(pageOne)):
        currentItem = pageOne[i]
        if currentItem['fr_escalated'] == True:
            FRDue.insert(0, currentItem['id'])
        else:
            pass
            
        
    return len(FRDue)

def getKody(): #agent_id is 81076038984
    getTickets = requests.get(apiURL + 'search/tickets?query="(agent_id:81076038984) AND (status:2 OR status:3 OR status:6 OR status:11)"', auth = (api_key, password))
    getTickets = getTickets.json()
    totalTickets = getTickets['total']
    
    #if totalTickets > 30:
    #else:
    
    getTickets = getTickets['results']
    
    WoCTickets = []
    openTickets = []
    
    for i in range(len(getTickets)):
        currentItem = getTickets[i]
        if currentItem['status'] == 6:
            WoCTickets.insert(0, currentItem['id'])
        elif currentItem['status'] == 2:
            openTickets.insert(0, currentItem['id'])
        else:
            pass
     
    return totalTickets, len(WoCTickets), len(openTickets)
    
def getJimmy(): #agent_id is 81057782986
    getTickets = requests.get(apiURL + 'search/tickets?query="(agent_id:81057782986) AND (status:2 OR status:3 OR status:6 OR status:11)"', auth = (api_key, password))
    getTickets = getTickets.json()
    totalTickets = getTickets['total']
    
    getTickets = getTickets['results']
    
    WoCTickets = []
    openTickets = []
    
    for i in range(len(getTickets)):
        currentItem = getTickets[i]
        if currentItem['status'] == 6:
            WoCTickets.insert(0, currentItem['id'])
        elif currentItem['status'] == 2:
            openTickets.insert(0, currentItem['id'])
        else:
            pass
     
    return totalTickets, len(WoCTickets), len(openTickets)
    
def getGabe(): #agent_id is 81063055620
    getTickets = requests.get(apiURL + 'search/tickets?query="(agent_id:81063055620) AND (status:2 OR status:3 OR status:6 OR status:11)"', auth = (api_key, password))
    getTickets = getTickets.json()
    totalTickets = getTickets['total']
    
    getTickets = getTickets['results']
    
    WoCTickets = []
    openTickets = []
    
    for i in range(len(getTickets)):
        currentItem = getTickets[i]
        if currentItem['status'] == 6:
            WoCTickets.insert(0, currentItem['id'])
        elif currentItem['status'] == 2:
            openTickets.insert(0, currentItem['id'])
        else:
            pass
     
    return totalTickets, len(WoCTickets), len(openTickets)
    
def getPat(): #agent_id is 81079660605
    getTickets = requests.get(apiURL + 'search/tickets?query="(agent_id:81079660605) AND (status:2 OR status:3 OR status:6 OR status:11)"', auth = (api_key, password))
    getTickets = getTickets.json()
    totalTickets = getTickets['total']
    
    getTickets = getTickets['results']
    
    WoCTickets = []
    openTickets = []
    
    for i in range(len(getTickets)):
        currentItem = getTickets[i]
        if currentItem['status'] == 6:
            WoCTickets.insert(0, currentItem['id'])
        elif currentItem['status'] == 2:
            openTickets.insert(0, currentItem['id'])
        else:
            pass
     
    return totalTickets, len(WoCTickets), len(openTickets)
    
def getRaul(): #agent_id is 81017848311
    getTickets = requests.get(apiURL + 'search/tickets?query="(agent_id:81017848311) AND (status:2 OR status:3 OR status:6 OR status:11)"', auth = (api_key, password))
    getTickets = getTickets.json()
    totalTickets = getTickets['total']
    
    getTickets = getTickets['results']
    
    WoCTickets = []
    openTickets = []
    
    for i in range(len(getTickets)):
        currentItem = getTickets[i]
        if currentItem['status'] == 6:
            WoCTickets.insert(0, currentItem['id'])
        elif currentItem['status'] == 2:
            openTickets.insert(0, currentItem['id'])
        else:
            pass
     
    return totalTickets, len(WoCTickets), len(openTickets)