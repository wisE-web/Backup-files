import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BFDa0F2JKOKjyi_QJ_UfpCCz4uO7E3QIw889oXAiBGCmoiwxVAVDr_gE9hdi4WNWzwnWlnSWr8VG-kMUedpR7LP-15dSQjrextPeX7WLXPkaDBMcivCEVHTBz5Fid203bgcAh5nlSvc3'
    transferData = TransferData(access_token)

    file_from = 'text2.txt'
    file_to = '/test_dropbox/text2.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()