import dropbox

class TrasnferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_folder(self,folder_from,folder_to):
        dbx = dropbox.Dropbox(self.access_token)

        folder = open(folder_from,'rb')
        dbx.files_upload(folder.read(),folder_to)

def main():
    access_token = 'sl.BHrO3yGLY5nep2_XYZY0u511rTctF-c9ARjyhZdojVrTHKpYgDjlMKKiut66YWPHK8ENxFjOl5P7yMBQoWVmAg7kgPi7vKjPg_tgP-EEBuAvqR7-mJ5SHwnN8gFmYPVrbomjWCU'
    transferData  = TrasnferData(access_token)

    folder_from = input("Enter the folder path to transfer: ")
    folder_to = input("Enter the full path to upload to the dropbox: ")
    
    transferData.upload_folder(folder_from,folder_to)

    print("Folder has been uploaded")

main()
