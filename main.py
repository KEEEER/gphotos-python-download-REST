from oauth2client.client import GoogleCredentials
from googlephotos.token_refresher import refresh
from googlephotos.metadata import Metadata
from googlephotos.processor import Processor

import os.path
import requests

client_id = "fill"
client_secret = "fill"
refresh_token = "fill"

params = {
        'access_token' : "no",
        'fields' : "*"
}

def read_properties(name):
    global client_id , client_secret , refresh_token
    with open(name) as f:
        for line in f:
            if '=' in line:
                name, value = line.split("=", 1)
                name = name.strip()
                value = value.strip()
                if 'client_id' == name:
                    client_id = str(value)            
                if 'client_secret' == name:
                    client_secret = str(value)                    
                if 'refresh_token' == name:
                    refresh_token = str(value)                 
    f.close()
    return

def main():
    root_path = 'C:/Users/user/Desktop/google photo/python/gphotos-download/download'
    read_properties('local.properties')
    access_token = refresh(client_id , client_secret , refresh_token)
    params['access_token'] = access_token    

    metadata = Metadata(params)
    mediaItems = metadata.list('mediaItems')
    album_basic_info = metadata.list('albums')
    album_with_media = metadata.list_album_media(album_basic_info)

    processor = Processor()
    processor.download_albums(album_with_media , root_path)
    processor.download_mediaItems(mediaItems , root_path)

    print("update complete!")
if __name__ == '__main__':
  main()
