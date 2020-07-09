from ftplib import FTP
import os

class ftpConnect:
    def __init__(self, host: str):
        self.host = host
        self.ftp = None # main ftp object

    # connect to host
    def connect(self):
        try:
            self.ftp = FTP(self.host)
            print("Connected:", self.host)
        except:
            print("Unable to connect:", self.host)

    # login to host
    def login(self, username: str, password: str):
        try:
            self.ftp.login(user = username, passwd = password)
            print("Logged in:", self.host)
        except:
            print("Unable to login:", self.host)

    # kill connection
    def kill(self):
        try:
            self.ftp.quit()
            print("Closed:", self.host)
        except:
            print("Unable to close:", self.host)

    # go to path (cd)
    def path(self, path: str):
        try:
            self.ftp.cwd(path)
            print("Path:", path)
        except:
            print("Path not valid:", path)

    # list items in directory (ls)
    def list(self):
        self.ftp.retrlines('LIST')

    # download and return file
    def downloadFile(self, filename: str):
        # download file
        with open(filename, 'wb') as file :
            newName = filename + self.host
            self.ftp.retrbinary('RETR %s' % filename, file.write)         
        
        print("File downloaded:", filename, "|", self.host)

    # read local file
    def readFile(self, filename: str):
        f = open(filename, "r")
        data = f.read()
        f.close()
        return data

    # edit local file
    def editFile(self, filename: str, data: str):
        f = open(filename, "a+")
        f.write("\n" + data)
        f.close()

    # upload file
    def uploadFile(self, filename: str):
        self.ftp.storbinary("STOR " + filename, open(filename, "rb"))
        print("File uploaded:", filename)

    # deletes local file
    def deleteFile(self, filename: str):
        try:
            os.remove(filename)
            print("File deleted:", filename)
        except:
            print("Unable to delete file:", filename)