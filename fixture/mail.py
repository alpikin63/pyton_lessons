from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import errors
# If modifying these scopes, delete the file token.json.


class Gmail:

    SCOPES = 'https://www.googleapis.com/auth/gmail.modify'
    SCOPES_FILTER = 'https://www.googleapis.com/auth/gmail.settings.basic'

    def __init__(self):
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        #     # time.
        store = file.Storage('../token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('../credentials.json', self.SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('gmail', 'v1', http=creds.authorize(Http()))

    def auth_settings(self):
        store = file.Storage('../token_auth.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('../credentials_auth.json', self.SCOPES_FILTER)
            creds = tools.run_flow(flow, store)
        self.service = build('gmail', 'v1', http=creds.authorize(Http()))
        print(self.service.users().settings().filters().list(userId='me').execute())

    def get_labels(self):

        # Call the Gmail API
        results = self.service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
        else:
            print(labels)
            return labels

    def createLabel(self, label_name=''):

        label_object = self.MakeLabel(label_name=label_name)
        label = self.service.users().labels().create(userId='me', body=label_object).execute()
        return label

    def MakeLabel(self, label_name, mlv='show', llv='labelShow'):
        """Create Label object."""
        label = {'messageListVisibility': mlv,
                 'name': label_name,
                 'labelListVisibility': llv}
        return label

    def deletelabel(self, lable_name):
        label_list = self.get_labels()
        lable_id = ''
        for label in label_list:
            if label['name'] == lable_name:
                lable_id = label['id']
        self.service.users().labels().delete(userId='me', id=lable_id).execute()

    def makeFilter(self, sender, label):
        filter = {
          "id": 'test',
          "criteria": {
            "from": sender,
          },
          "action": {
            "addLabelIds": [
                label
            ]
          }
        }
        return filter

    def createFilter(self, sender, labdel):
        filterobj = self.makeFilter(sender, labdel)
        filter = self.service.users().settings().filters().create(userId='me', body=filterobj).execute()
        return filter



a = Gmail()
#a.get_labels()
a.auth_settings()
#a.createFilter("pikin@aeroidea.ru", 'Label_2')
#a.createLabel(label_name='test1234')
#a.deletelabel('test1234')




