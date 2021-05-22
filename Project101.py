import dropbox
import os
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                localPath = os.path.join(root,filename)
                relPath = os.path.relpath(localPath,file_from)
                dropboxPath = os.path.join(file2,relPath)

        with open(localPath,'rb') as f:
            dbx.files_upload(f.read(),dropboxPath)
def main():
    access_token = 'I5N1ELwuMdYAAAAAAAAAATcU77sI1-jAUSkVRtt0ShLCvT7gWGX195OwgMndAZWY'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt' # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from,file_to)

if __name__ == '__main__':
    main()