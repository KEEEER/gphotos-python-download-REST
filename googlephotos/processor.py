import requests
import os.path

database = 'https://www.googleapis.com/drive/v3/files/'
download = '?alt=media&access_token='

class Processor:

    def download_albums(self , albums , root_path):
        for album in albums:
            path = root_path + '/' + album
            try:
                os.makedirs(path)
            except Exception:
                pass

            print("downloading  album : {}".format(album))
            for media in albums[album]:            
                if not os.path.isfile(path + '/' + media['filename']):    
                    print("media file : {}".format(media['filename']))
                    responds = requests.get(media['baseUrl'])
                    file = open(path + '/' + media['filename'] , "wb")
                    file.write(responds.content)
                    file.close()
        return

    def download_mediaItems(self , mediaItems , root_path):
        for items in mediaItems:
            for item in items:
                if not os.path.isfile(root_path + '/' + item['filename']):
                    print("downloading media file : {}".format(item['filename']))
                    responds = requests.get(item['baseUrl'])
                    file = open(root_path + '/' + item['filename'] , "wb")
                    file.write(responds.content)
                    file.close()
        return
#=======================================================================================