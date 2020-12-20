import socket
import threading
import os

def RetrieveFile(filename, s): #function that send file to client
    filename = s.recv(1024).decode()
    #print (filename)
    if os.path.isfile(filename): #check if fime name requested is available or not
        exist = "Exist" + str(os.path.getsize(filename)) 
        s.send(str.encode(exist))
        response = s.recv(1024).decode()
        print(response)
        if response[:3] == 'yes': #if user yes response yes, it will send the file
            f = open(filename, 'rb')
            SendFile = f.read(1024) 
            s.send(SendFile)
    else:
        Print ("File Does Not Exist!!" ) #if file doesnt exist
    s.close()
    
def SendFile(filename, conn, addr): #receive file from client
    
    #filename = str(addr) #file name under client's ip address name
    filename = "fromclient.txt"
    file = open('new_' + filename, 'wb') # write 
    print('Receiving data...')
    f_data = conn.recv(1024)
    file.write(f_data)
    print('File received!!')
    conn.close()
    
    
def Main():
    host = "192.168.43.50"
    port = 8080
    
    s = socket.socket()
    s.bind((host,port))
    
    s.listen(5)
    
    print ("Server Started...")
    while True:
        conn, addr = s.accept()
        print ("Connection established from : " + str(addr))
        
        option = conn.recv(1024).decode()
        
        if option == 'u':
            print("Client is Uploading a file")
            t = threading.Thread(target = SendFile, args = ("retrivThread",conn, addr)) #thread if client upload file
            t.start()
        elif option == 'd':
            print("Client is Downloading a file")
            t = threading.Thread(target = RetrieveFile, args = ("retrivThread",conn)) #thread if client download file
            t.start()
    s.close()
    
Main()