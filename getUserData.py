from urllib.request import urlopen
import json
from pprint import pprint

username = "ij2827"

# returns json data from url
def getJson(url):
    data = urlopen(url).read().decode('utf-8')
    return json.loads(data)

# returns JSON DATA as a list
def getRepoJson(username):
    url = "https://api.github.com/users/"
    url += username + '/repos'
    data = urlopen(url).read().decode('utf-8')
    return [json.loads(data)]

def getRepoJsonSaved():
    with open('gists.json') as jsonData:
        data = json.load(jsonData)
    # pprint(data)
    return data
# TODO make repoClean() read test 'gistsTest.json' by default to lower calls to api/ set time limit
# return a list of cleaned repo data
# set 'isSavedData=True' when cleaning data from saved gist.json file
def repoClean( isSavedData=False, test_mode=True):
    # Get data from api.github.com if isSavedData=False
    if not isSavedData:
        gitData = getRepoJson(username)
        repoDict = {}
        repoList = []
        for repos in gitData:
            for i, repo in enumerate(repos):

                repoDict['user_name'] = repo['owner']['login']
                repoDict['url'] = repo['html_url']
                repoDict['title'] = repo['name']
                repoDict['about'] = repo['description']
                repoDict['languages'] = getJson(repo['languages_url'])
                repoDict['id'] = i
                repoList[i] = repoDict.items()
        pprint(repoList)
        return repoList
    else:
        print('reloading from saved')
        gitData = getRepoJsonSaved()
        pprint(gitData)
        return gitData

# Saves a dictionary to a json file
def saveJson(data):
    with open('gists.json', 'w') as output:
        json.dumps(data, output)




repoClean()
# saveJson(repoClean(git))