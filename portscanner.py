
#importing needed libraries
import os
import socket
import subprocess
import requests
from colorama import Fore
from colorama import Style


def ResetColor():
    print(Style.RESET_ALL)

# finding out OS running to clear the terminal/cmd

os_in_execution = os.name
if os_in_execution == "nt":
    subprocess.call("cls",shell=True)
elif os_in_execution == "posix":
    subprocess.call("clear",shell=True)
else:
    exit()

# asking for host & checking length to detect errors

host = input(Fore.YELLOW + "[*] HOST (WITHOUT PROTOCOL): ")
if len(host) < 5:
    print("[*] Invalid host.")
    ResetColor()
    exit()
ResetColor()

# resolving the host & asking for protocol

host_ip = socket.gethostbyname(host)
choice = int(input(Fore.YELLOW + "[*] Choose 1 or 2 in case the selected host has HTTP or HTTPS protocol: "))
if choice == 1:
    print(Fore.YELLOW + "[*] You selected HTTP.")
    print(Fore.BLUE + "[*] Resolving %s to %s." %(host,host_ip))
    print(Fore.BLUE + "-" * 50)
    ResetColor()
    r = requests.get("http://" + host)
elif choice == 2:
    print(Fore.YELLOW + "[*] You selected HTTPS.")
    print(Fore.BLUE + "[*] Resolving %s to %s." %(host,host_ip))
    print(Fore.BLUE + "-" * 50)
    ResetColor()
    r = requests.get("https://" + host)
else:
    print(Fore.RED + "[*] No other choice available.")
    ResetColor()
    exit()

# checking reponse from the site

response = r.status_code
if response == 200:
    print(Fore.GREEN + "[*] %s was found (200)." %host_ip)


# asking for the range of ports to test
print(Fore.YELLOW + "[*] Now you'll be asked to enter the ports range you are going to test.")
first_port = int(input(Fore.BLUE + "[*] First port: "))
last_port = int(input(Fore.BLUE + "[*] Last port: "))
if first_port <= 0 or last_port <= 0:
    print(Fore.RED + "[*] Invalid port number.")
    ResetColor()
    exit()

# port scanning

for port in range(first_port,last_port):
    try:
        # creating TCP socket & loop over every port in the range
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((host,port))
        if result == 0:
            print(Fore.GREEN + "[*] Port %d : Open." %port)
            ResetColor()
        s.close()
    except KeyboardInterrupt:
        exit()




