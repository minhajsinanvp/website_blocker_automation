import ctypes
import sys
from datetime import datetime as dt
import time


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False



hostpath = "C:\Windows\System32\drivers\etc\hosts"
temp = "hosts"
redirect = "127.0.0.1"

website_list = ["www.facebook.com", "facebook.com",r"https://www.facebook.com/"]
if is_admin():

    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 20):
            print("working hours......")

            with open(hostpath, "r+") as f:
                content = f.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        f.write(redirect + "  " + website + "\n")

        else:
            
            with open(hostpath, "r+") as f:

                content = f.readlines()
                f.seek(0)
                for line in content:

                    if not any(website in line for website in website_list):
                        f.write(line)

                f.truncate()

            print("watch some Naruto episodes boy......")
            time.sleep(5)
    # print(1)


else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
