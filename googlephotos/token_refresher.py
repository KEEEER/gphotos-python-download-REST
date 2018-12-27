from oauth2client.client import GoogleCredentials
import httplib2

def refresh(client_id , client_secret , refresh_token):
    cred = GoogleCredentials(None,client_id,client_secret,
                                    refresh_token,None,"https://accounts.google.com/o/oauth2/token",None)
    http = cred.authorize(httplib2.Http())
    cred.refresh(http)
    return cred.access_token
