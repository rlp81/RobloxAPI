import requests

UserAPI = "https://users.roblox.com/v1/users/userId"


def getUsername(userid):
    full = UserAPI.replace("userId", str(userid))
    json = requests.get(url=full).json()
    return json['name']


def getDescription(userid):
    full = UserAPI.replace("userId", str(userid))
    json = requests.get(url=full).json()
    return json['description']


def getDisplayname(userid):
    full = UserAPI.replace("userId", str(userid))
    json = requests.get(url=full).json()
    return json['displayName']


def getCreatedAt(userid):
    full = UserAPI.replace("userId", str(userid))
    json = requests.get(url=full).json()
    return json['created']


def isBanned(userid):
    full = UserAPI.replace("userId", str(userid))
    json = requests.get(url=full).json()
    return bool(json['isBanned'])

