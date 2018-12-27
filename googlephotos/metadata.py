import requests
import os.path

album_database = 'https://photoslibrary.googleapis.com/v1/albums'
media_database = 'https://photoslibrary.googleapis.com/v1/mediaItems'
search_database = 'https://photoslibrary.googleapis.com/v1/mediaItems:search'
#Class==================================================================================
class Metadata:
    def __init__(self , params):
        self.params = params

    def list(self , kind_str):
        print("listing files......(may take times)")
        database = 'https://photoslibrary.googleapis.com/v1/' + kind_str
        params = self.params
        lists = []
        while True:
            responds = requests.get(database , params = self.params).json()
            if kind_str in responds:
                lists.append(responds[kind_str].copy())
            if 'nextPageToken' in responds:
                params["pageToken"] = responds["nextPageToken"]
            else:
                return lists

    def list_album_media(self , albums):
        dicts = {}
        params = {
            "albumId": "id",
            "access_token" : "none"
        }
        params['access_token'] = self.params['access_token']
        dicts = {}
        for album in albums:
            for items in album:
                print("finding media items of : {}".format(items['title']))
                params['albumId'] = items['id']          
                responds = requests.post(search_database , params = params).json()
                if 'mediaItems' in responds:
                    dicts[items['title']] = responds['mediaItems']
        return  dicts

#=======================================================================================

