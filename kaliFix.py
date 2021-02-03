#This file helps in setting up the sources.list in kali linux as well as configuration of network drivers

from os import system as sst

# We aim to install these
mainLine = "sudo apt install apt-file -y && sudo apt-file update && apt-file find rtl8192cufw.bin"

#configure in sources.list
aptRepos = ["deb http://http.kali.org/kali kali-rolling main non-free contrib", "deb-src http://http.kali.org/kali kali-rolling main non-free contrib"]


with open("/etc/apt/sources.list", 'w') as f:
    for i in aptRepos:
        f.write(i + '\n')
    f.close()

sst('sudo apt update && sudo apt upgrade -y ' + mainLine)
print("\n\t \033[93m SUCCESS Up To Date!")


def drivers():
    print("\n  \033[31m  Your Pc will reboot after this \n\n")
    
    with open("logs.log", 'w') as f:
        f.write(" When the roll is called up yonder i will be there ")

    sst("sudo apt-get install git build-essential linux-headers-generic && git clone https://github.com/Mange/rtl8192eu-linux-driver.git && cd rtl8192eu-linux-driver && make && sudo make install && poweroff")

    print("\033[32m SUCCESS cloned !!")


def afterReboot():
    sst('exit && exit ')
    print("\n \033[93m Welcome back, we will be done in a few \n\n")
    sst("cd rtl8192eu-linux-driver && make clean && make && sudo make install")


def runLast():
    with open('logs.log', 'r') as f:
        content = f.readlines()
        print('\n\t \033[31m there is logs !')
        f.close()

    if content:
        afterReboot()
        sst("rm logs.txt")

drivers()
runLast()
