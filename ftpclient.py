import socket


def Main() :
    host = "192.168.43.50"
    port = 8080
    
    s = socket.socket()
    s.connect((host,port))
    
    print ("Connecting to server...")
    
    
    print ("Server Connected!")
    
    option = input("What action do you wish to do? (d->download/u->upload) : ") 
    
    s.send(str.encode(option))
    
    if option == 'u' : #if user choose to send file to server
        filename1 = input("File name? : ")
        file = open(filename1,'rb')  #Read
        print('sending file...')
        data = file.read(1024)   # read data file
        s.send(data)
        print('File Sent!!')
    
    elif option == 'd' : #if user choose to retrieve file from server
        filename = input("File name? : ")
        if filename != 'x':
            s.send(str.encode(filename))
            filedata = s.recv(1024).decode()
            print (filedata)
            if filedata[:5] == "Exist": #if filename input by user exist in server, client will download the file
                filesize = int(filedata[5:])
                message = input("File Exist, " + str(filesize)+"Bytes, do you want to download? (Y/N) : ")
                if message == 'y':
                    response = "yes"
                    s.send(str.encode(response))
                    f = open('new_' + filename,'wb')
                    filedata = s.recv(1024)
                    tRecv = len(filedata)
                    f.write(filedata)
                    print ("Download Complete!")
            else: #if filename input by user does not exist in server
                print ("File Does Not Exist!")
    else :
        print("invalid option!!")
    
    s.close()


Main()
            