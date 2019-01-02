from oauth2client.client import GoogleCredentials
from googlephotos.token_refresher import refresh
from googlephotos.metadata import Metadata
from googlephotos.processor import Processor
from googlephotos.read_properties import read
import os.path
import requests

client_id = "fill"
client_secret = "fill"
refresh_token = "fill"

# (v)issue 01 : write read local.properties function
# (v)issue 02 : sprate list() method to list_media() and list_album_media()
# (v)issue 03 : create Metadata class now need only access_token
# issue 04 : 
# issue 05 : 
# issue 06 :

def main():
    root_path = 'C:/Users/user/Desktop/google photo/python/gphotos-download/download'
    
    meta_list = read('local.properties')
    client_id = meta_list['client_id']
    client_secret = meta_list['client_secret']
    refresh_token = meta_list['refresh_token']

    access_token = refresh(client_id , client_secret , refresh_token)
    
    metadata = Metadata(access_token)
    mediaItems = metadata.list_media()
    album_with_media = metadata.list_album_media()

    processor = Processor()
    processor.download_albums(album_with_media , root_path)
    processor.download_mediaItems(mediaItems , root_path)

    print("update complete!")
if __name__ == '__main__':
  main()
