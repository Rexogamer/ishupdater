import argparse
import subprocess
import sys

class Updater:  
    # arguments
    def arguments(self):
        p = argparse.ArgumentParser(add_help=True)
        p.add_argument('-all',action='store_true',help='Updates everything.')
        p.add_argument('-noapk',action='store_true',help="Doesn't update Alpine.")
        p.add_argument('-nomotd',action='store_true',help="Doesn't update the MOTD.")
        args = p.parse_args()
        if args.all:
            self.updateall()
        elif args.noapk:
            self.updatemotd()
        elif args.nomotd:
            self.updatealpine()
        if len(sys.argv[0]) != 1:
            print('Run python3 updater.py --help to see the options.')
    # the motd updater
    def updatemotd(self):
        ishCVer = ""
        ishCBuild = ""
        ishNVer = ""
        ishNBuild = ""
        if ishCVer == "":
            ishCVer = input("Old iSH version: ")
        if ishCBuild == "":
            ishCBuild = input("Old iSH build: ")
        if ishNVer == "":
            ishNVer = input("New iSH version: ")
        if ishNBuild == "":
            ishNBuild = input("New iSH build: ")

        # update the motd
        subprocess.check_call("sed -i 's/{}/{}/g' /etc/motd".format(ishCVer, ishNVer), shell=True)
        subprocess.check_call("sed -i 's/{}/{}/g' /etc/motd".format(ishCBuild, ishNBuild), shell=True)
        print("MOTD updated; restart to see changes.")

    # the alpine updater
    def updatealpine(self):
        apkCVer = ""
        apkNVer = ""
        if apkCVer == "":
            apkCVer = input("Current Alpine version: ")
        if apkNVer == "":
            apkNVer = input("New Alpine version: ")

        # update alpine
        subprocess.check_call("sed -i 's/{}/{}/g' /etc/apk/repositories".format(apkCVer, apkNVer), shell=True)
        subprocess.check_call("apk update", shell=True)
        subprocess.check_call("apk upgrade --available && sync", shell=True)
        print("Updated Alpine.")

    def updateall(self):
        self.updatemotd()
        self.updatealpine()
            
if __name__ == "__main__":
  Updater().arguments()
