"""
Client that sends the file (uploads)
"""
import socket
import tqdm
import os
import argparse
from zipfile import ZipFile
from os.path import basename

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4 #4KB

def send_file(filename, host, port):
    # get the file size
    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    #Create a zip file
    with ZipFile('send.zip', 'w') as zipObj:
        # Iterate over all the files in directory
        dirName = filename
        for folderName, subfolders, filenames in os.walk(dirName):
            for filename_zip in filenames:
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename_zip)
                # Add file to zip
                zipObj.write(filePath, basename(filePath))

    # send the filename and the size of the zip that is actually sent
    filesize = os.path.getsize("send.zip")
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open("send.zip", "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    os.remove("send.zip")

    # close the socket
    s.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple File Sender")
    parser.add_argument("file", help="File name to send")
    parser.add_argument("host", help="The host/IP address of the receiver")
    parser.add_argument("-p", "--port", help="Port to use, default is 5001", type=int, default=5001)
    args = parser.parse_args()
    filename = args.file
    host = args.host
    port = args.port

    send_file(filename, host, port)