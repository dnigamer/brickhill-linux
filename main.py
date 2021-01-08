#!/usr/bin/python

import os
import sys
import subprocess
import re
import time

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

prgname = colors.BOLD + colors.OKBLUE + "Brick Hill " + colors.ENDC + colors.BOLD + colors.WARNING + "Linux " + colors.ENDC + colors.BOLD + "installer by DniGamer" + colors.ENDC
distro = subprocess.check_output("lsb_release -ds", shell=True, universal_newlines=True)

def find(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def err_handler(section, error):
    print()
    print(colors.FAIL + colors.BOLD + "! "*25, colors.ENDC)
    if section == "requirements":
        print(colors.BOLD + "Something went wrong in dependencies install. Please report the error to the developer." + colors.ENDC)
        sys.exit()
    
    if section == "pre-req":
        print(colors.BOLD + "Something went wrong in dependencies install. Please report the error to the developer." + colors.ENDC)
        sys.exit()

    if section == "download":
        print(colors.BOLD + "Something went wrong when downloading files. Please check if you have internet access and try again" + colors.ENDC)
        print(error)
        sys.exit()

def command(command):
    return subprocess.check_output(command, shell=True, universal_newlines=True)

def installer():
    # MONO FOLDER CREATOR AND DOWNLOADER 
    if os.path.exists("/usr/share/wine/mono") == False:
        print()
        print(colors.BOLD + "/usr/share/wine/mono folder " + colors.ENDC + colors.BOLD + colors.FAIL +  "doesn't exist. Creating directory."+ colors.ENDC + colors.BOLD + " Sudo permissions can be asked!"+ colors.ENDC)
        print(colors.BOLD + "/usr/share/wine/mono/wine-mono-5.1.1-x86.msi executable " + colors.ENDC + colors.BOLD + colors.FAIL +  "doesn't exist. Downloading files."+ colors.ENDC + colors.BOLD + " Sudo permissions can be asked!"+ colors.ENDC)
        print()
        try:
            command("sudo mkdir /usr/share/wine/mono")
            command("sudo wget http://dl.winehq.org/wine/wine-mono/5.1.1/wine-mono-5.1.1-x86.msi -P /usr/share/wine/mono/")
        except Exception as err:
            err_handler("download", err)
    else:
        print(colors.BOLD + "/usr/share/wine/mono folder " + colors.ENDC + colors.BOLD + colors.OKGREEN + "exists" + colors.ENDC)
        if os.path.exists("/usr/share/wine/mono/wine-mono-5.1.1-x86.msi") == False:
            print()
            print(colors.BOLD + "/usr/share/wine/mono/wine-mono-5.1.1-x86.msi executable " + colors.ENDC + colors.BOLD + colors.FAIL +  "doesn't exist. Downloading files."+ colors.ENDC + colors.BOLD + " Sudo permissions can be asked!"+ colors.ENDC)
            print()
            try:
                command("sudo wget http://dl.winehq.org/wine/wine-mono/5.1.1/wine-mono-5.1.1-x86.msi -P /usr/share/wine/mono/")
            except Exception as err:
                err_handler("download", err)
        else:
            print(colors.BOLD + "/usr/share/wine/mono/wine-mono-5.1.1-x86.msi executable " + colors.BOLD + colors.OKGREEN + "exists" + colors.ENDC)
            print()

    # GECKO FOLDER CREATOR AND DOWNLOADER 
    if os.path.exists("/usr/share/wine/gecko") == False:
        print()
        print(colors.BOLD + "/usr/share/wine/gecko folder " + colors.ENDC + colors.BOLD + colors.FAIL + "doesn't exist. Creating directory."+ colors.ENDC + colors.BOLD + " Sudo permissions can be asked!"+ colors.ENDC)
        print(colors.BOLD + "/usr/share/wine/gecko/wine_gecko-2.47-x86.msi executable " + colors.ENDC + colors.BOLD + colors.FAIL + "doesn't exist. Downloading files."+ colors.ENDC + colors.BOLD + " Sudo permissions can be asked!"+ colors.ENDC)
        print()
        try:
            command("sudo mkdir /usr/share/wine/gecko")
            command("sudo wget http://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86.msi -P /usr/share/wine/gecko/")
        except Exception as err:
            err_handler("download", err)
    else:
        print(colors.BOLD + "/usr/share/wine/gecko folder " + colors.BOLD + colors.OKGREEN + "exists" + colors.ENDC)
        if os.path.exists("/usr/share/wine/gecko/wine_gecko-2.47-x86.msi") == False:
            print()
            print(colors.BOLD + "/usr/share/wine/gecko/wine_gecko-2.47-x86.msi executable " + colors.ENDC + colors.BOLD + colors.FAIL +  "doesn't exist. Downloading files."+ colors.ENDC + colors.BOLD + " Sudo permissions can be asked!"+ colors.ENDC)
            print()
            try:
                command("sudo wget http://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86.msi -P /usr/share/wine/gecko/")
            except Exception as err:
                err_handler("download", err)
        else:
            print(colors.BOLD + "/usr/share/wine/gecko/wine_gecko-2.47-x86.msi executable " + colors.BOLD + colors.OKGREEN + "exists" + colors.ENDC)
            print()

    # BRICK-HILL INSTALLER DOWNLOADER AND INSTALLER
    print()
    user = input(colors.BOLD + "To what Linux user do you want Brick Hill to get installed to? " + colors.ENDC)
    try:
        if os.path.exists(f"/home/{user}/.wine/drive_c/users/{user}/Application Data/Brick Hill/") != True:
            print("-"*35)
            print(colors.BOLD + "Installing " + colors.OKBLUE + "Brick Hill" + colors.ENDC + colors.BOLD + ". Please wait!" + colors.ENDC)
            print("-"*35)
            command("wget https://brkcdn.com/downloads/BrickHillSetup.exe -P /tmp/")
            print()        
            try:
                print(colors.BOLD + "Please continue the installation in the setup window that showed up" + colors.ENDC)
                command("wine /tmp/BrickHillSetup.exe")
                print(colors.BOLD + colors.OKBLUE + "Brick Hill" + colors.OKGREEN + " installation suceeded!" + colors.ENDC)
            except Exception as err:
                err_handler("download", err)        
        else:
            print()
            print(colors.BOLD + colors.OKBLUE +"Brick Hill" + colors.OKGREEN + " already installed in wine" + colors.ENDC)
    except Exception as err:
        err_handler("download", err)

    # AUTOMATED SCRIPTS FOR AUTOMATED RUNNING
    print()
    print(colors.BOLD + "Making a new desktop custom url handler for Brick-Hill..." + colors.ENDC)
    desktop_file = "[Desktop Entry]\nName=Brick Hill\nExec=/usr/bin/brickhill %u\nType=Application\nTerminal=false\nMimeType=x-scheme-handler/brickhill.legacy;text/html;x-scheme-handler/brickhill.client;"""
    command(f"sudo echo '{desktop_file}' > /home/$(whoami)/.local/share/applications/brick-hill.desktop")
    
    print()
    print(colors.BOLD + "Making a new executable for Brick Hill..." + colors.ENDC)
    command("sudo echo 'wine \"/home/$(whoami)/.wine/drive_c/users/$(whoami)/Application Data/Brick Hill/Player.exe\" ${1#$\"brickhill.legacy://client/\"}' > /tmp/brickhill")
    command("sudo mv /tmp/brickhill /usr/bin/brickhill")
    command("sudo chmod +x /usr/bin/brickhill")
    command("sudo update-desktop-database")

    print()
    print(colors.BOLD + colors.OKGREEN + "#"*25 + colors.ENDC)
    print(colors.BOLD + colors.OKGREEN + "Installation finished!!" + colors.ENDC)
    print(colors.BOLD + colors.OKGREEN + "#"*25 + colors.ENDC)
    finish()

def requirements(distro):
    try:
        if distro != "":
            if find('arch')(distro) != None or find('manjaro')(distro) != None:
                try:
                    command("sudo pacman -Sy wine wget --noconfirm")
                    print(colors.OKGREEN + colors.BOLD + f"Pre-installation requirements installed for {distro}", colors.ENDC)
                    return True
                except Exception as err:
                    err_handler("requirements", err)
                    return False
            else:
                pass

            if find('ubuntu')(distro) != None or find('debian')(distro) != None:
                try:
                    command("sudo apt-get update -y")
                    command("sudo apt-get install wget wine sudo -y")
                    print(colors.OKGREEN + colors.BOLD + f"Pre-installation requirements installed for {distro}", colors.ENDC)
                    return True
                except Exception as err:
                    err_handler("requirements", err)
                    return False

            if find('centos')(distro) != None or find('redhat')(distro) != None:
                try:
                    command("sudo yum -y update")
                    command("sudo yum -y install wine wget sudo")
                    print(colors.OKGREEN + colors.BOLD + f"Pre-installation requirements installed for {distro}", colors.ENDC)
                    return True
                except Exception as err:
                    err_handler("requirements", err)
                    return False
            else:
                pass
        else:
            err_handler("pre-req", "No distro detected")
    except Exception as err:
        err_handler("pre-req", err)

def main():
    print("-"*(len(prgname)-34))
    print(prgname)
    print("-"*(len(prgname)-34))
    print(colors.BOLD + "Your distro: " + colors.ENDC + distro)
    conf = input(colors.BOLD + "Is the distro correct? (y/Y or n/N) " + colors.ENDC)
    if conf == "n" or conf == "N":
        print("Please check README.md to install the requirements for your system manually.")
        return 0
    elif conf == "y" or conf == "Y":
        print()
        conf = input(colors.BOLD + "Want to install the dependencies? (y/Y or n/N) " + colors.ENDC)
        if conf == "n" or conf == "N":
            installer()
        elif conf == "y" or conf == "Y":
            print("Installing required dependencies for "+ colors.BOLD + distro + colors.ENDC)
            print(colors.BOLD + colors.WARNING + "WARNING: " + colors.ENDC + colors.BOLD + "sudo password can be prompted for input!" + colors.ENDC)
            state = requirements(distro)
            if state:
                installer()
            else:
                return 1
        else:
            print(colors.BOLD + "Please use only y/Y or n/N"+ colors.ENDC)
            return 0
    else:
        print(colors.BOLD + "Please use only y/Y or n/N"+ colors.ENDC)
        return 0

def finish():
    print()
    print(colors.BOLD + colors.OKBLUE + "Go to the brick hill games home page and start playing!!" + colors.ENDC)
    print()
    print()
    print(colors.BOLD + "For more information, go to https://github.com/dnigamer/brickhill-linux" + colors.ENDC)

if __name__ == "__main__":
    if os.path.isfile("/usr/bin/sudo") == None:
        print(colors.FAIL + colors.BOLD + "YOU DON'T HAVE SUDO INSTALLED ON YOUR SYSTEM!!" + colors.ENDC)
        print(colors.BOLD + "Check how to install sudo on your distro and then run this again!" + colors.ENDC)
        exit()
    else:
        print(colors.OKGREEN + colors.BOLD + "Sudo installed!" + colors.ENDC)
        print()
        pass
    main()