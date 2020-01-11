import subprocess

# get some variables
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
subprocess.check_call("sed 's/{}/{}/g' /etc/motd".format(ishCVer, ishNVer), shell=True)
subprocess.check_call("sed 's/{}/{}/g' /etc/motd".format(ishCBuild, ishNBuild), shell=True)

# update alpine (currently only supports the index/the edge repository)
subprocess.check_call("apk update", shell=True)
subprocess.check_call("apk upgrade --available && sync", shell=True)

print("Update complete, restart iSH to see changes.")
