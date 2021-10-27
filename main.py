import os
import socket
import platform
import datetime
import shutil
from distutils.dir_util import copy_tree

def hostinfo():
    try:
        print("\n=== Host PC info ===")
        print("OS Version:", platform.system(),platform.version())
        print("Host name:", socket.gethostname())
        winid = os.getlogin()
        print("Login Account:", winid)
    except Exception as ex:
        print(ex)
    return winid

def log():
    print("123")

def create(path):
    print("Create Directory Path:",path+"/Desktop/Art")
    try:
        os.makedirs(path+"/Desktop/Art/Chrome",exist_ok=True)
        os.makedirs(path +"/Desktop/Art/Edge", exist_ok=True)
        os.makedirs(path +"/Desktop/Art/IE", exist_ok=True)
    except Exception as ex:
        print(ex)

def chrome(path):
    try:
        print("\n[*] Chrome Browser artifact Collecting...")
        check = os.path.isdir(path+"/AppData/Local/Google")
        if check == False:
            print("[!] Not Found Chrome Path... Default Path is"+check)
        else:
            print("[!] Chrome Directory Path: "+path+"/AppData/Local/Google")
        print("[+] Chrome History, Cache, Cookies, Download List Copying...")

        history = path+"/AppData/Local/Google/Chrome/User Data/Default/History"
        cookies = path+"/AppData/Local/Google/Chrome/User Data/Default/Cookies"
        cache = path+"/AppData/Local/Google/Chrome/User Data/Default/Cache/"

        shutil.copy2(history, path+"/Desktop/Art/Chrome/History")
        shutil.copy2(cookies, path + "/Desktop/Art/Chrome/Cookies")
        copy_tree(cache, path + "/Desktop/Art/Chrome/Cache")

    except Exception as ex:
        print(ex)

def edge():
    try:
        print("1")
    except Exception as ex:
        print(ex)

def ie():
    try:
        print("1")
    except Exception as ex:
        print(ex)

def main():
    print("[*] Browser artifact parsing module")
    runtime = datetime.datetime.now()
    print("[+] Run Time:", runtime)
    info = hostinfo()
    path = "C:/Users/{}".format(info)
    create(path)
    chrome(path)

    print("End")


if __name__=="__main__":
    main()
