# path = C:\Windows\System32\drivers\etc\hos

from datetime import datetime as dt
import time
# from traceback import print_tb

hostpath= r"C:\Windows\System32\drivers\etc\hosts"
temp=  "hosts"
redirect = "127.0.0.1" 

website_list = ["www.facebook.com","facebook.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20) :
        print("working hours......")
        
        with open(hostpath, "r+") as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write(redirect + "  " +website + "\n")
                   
                        
            
           
            
        
        
    else:
        with open(hostpath,"r+") as f:
            
            content = f.readlines()
            f.seek(0)
            for line in content:
            
                if not any(website in line for website in website_list):
                    f.write(line)
                    
        
            f.truncate()   
            
            
        print("watch some Naruto episodes boy......")
        time.sleep(5)
    # print(1)
    
     
    
    
   