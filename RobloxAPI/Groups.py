import requests

UserGroupAPI = "https://groups.roblox.com/v2/users/id/groups/roles"
GroupAPI = "https://groups.roblox.com/v2/groups?groupIds=id"
V1GroupAPI = "https://groups.roblox.com/v1/groups/id/"
RoleroupAPI = "https://groups.roblox.com/v1/roles?ids="

def getRole(userid, groupid):
    full = UserGroupAPI.replace("id", str(userid))
    json = requests.get(url=full).json()
    for i in json['data']:
        if int(i['group']['id']) == groupid:
            return i['role']['name']

def getRank(userid, groupid):
    full = UserGroupAPI.replace("id", str(userid))
    json = requests.get(url=full).json()
    for i in json['data']:
        if int(i['group']['id']) == groupid:
            return i['role']['rank']


def getName(groupid):
    full = GroupAPI.replace("id", str(groupid))
    json = requests.get(url=full).json()
    return json['data'][0]['name']


def getDescription(groupid):
    full = GroupAPI.replace("id", str(groupid))
    json = requests.get(url=full).json()
    return json['data'][0]['description']


def getOwner(groupid):
    full = GroupAPI.replace("id", str(groupid))
    json = requests.get(url=full).json()
    return json['data'][0]['owner']['id']


def getRoles(groupid):
    full = V1GroupAPI.replace("id", str(groupid)) + "roles"
    json = requests.get(url=full).json()
    return json['roles']


def getRole(roleid):
    full = RoleroupAPI + str(roleid)
    json = requests.get(url=full).json()
    return json['data'][0]


def getUsers(groupid):
    full = V1GroupAPI.replace("id", str(groupid)) + "users"
    json = requests.get(url=full).json()
    return json['data']


def getUsersWithRole(groupid, roleid):
    full = V1GroupAPI.replace("id", str(groupid)) + "roles/id/users?sortOrder=Asc".replace("id", str(roleid))
    json = requests.get(url=full).json()
    return json['data']



