import requests
import os.path

album_database = 'https://photoslibrary.googleapis.com/v1/albums'
media_database = 'https://photoslibrary.googleapis.com/v1/mediaItems'
search_database = 'https://photoslibrary.googleapis.com/v1/mediaItems:search'


params = {
        'access_token' : "no",
        'fields' : "*"
}
#Class==================================================================================
class Metadata:
    def __init__(self , access_token):
        params['access_token'] = access_token

    def list_media(self):
        print("listing files......(may take times)")
        database = 'https://photoslibrary.googleapis.com/v1/mediaItems'
        lists = []
        while True:
            responds = requests.get(database , params = params).json()
            if 'mediaItems' in responds:
                lists.append(responds['mediaItems'].copy())
            if 'nextPageToken' in responds:
                params["pageToken"] = responds["nextPageToken"]
            else:
                return lists

    def list_album_media(self):
        print("listing files......(may take times)")
        database = 'https://photoslibrary.googleapis.com/v1/albums'
        albums = []
        while True:
            responds = requests.get(database , params = params).json()
            if 'albums' in responds:
                albums.append(responds[kind_str].copy())
            if 'nextPageToken' in responds:
                params["pageToken"] = responds["nextPageToken"]
            else:
                break;

        dicts = {}
        params_search = {
            "albumId": "id",
            "access_token" : "none"
        }
        params['access_token'] = params['access_token']
        dicts = {}
        for album in albums:
            for items in album:
                print("finding media items of : {}".format(items['title']))
                params['albumId'] = items['id']          
                responds = requests.post(search_database , params = params_search).json()
                if 'mediaItems' in responds:
                    dicts[items['title']] = responds['mediaItems']
        return  dicts

#=======================================================================================

