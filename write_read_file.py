import os

#create file
#function for write data in file
def writeDataInFile(_filename, data):
    if os.path.exists(_filename):
        f = open(_filename, 'a')
        f.write(str(data))
        f.write("\n")

        #closing file
        f.close()
    else:
        print("WARNING:file not exists")


#funcion for read file
def readDataFromFile(_filename):
    try:
        with open(_filename) as tmp_var:
            contentDataBase = tmp_var.read()
    except FileNotFoundError:
        contentDataBase = '<<< NOT FOUND >>>'
    return contentDataBase


#function for delete files
def deleteFile(_filename):
    os.remove(_filename)