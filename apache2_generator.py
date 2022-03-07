import sys
import os
from socfaker import SocFaker
from datetime import datetime
import time



def apache2_access_log(faker,timeNow): 
    try:
        f = open("demofile.log", "a")

        while(1):
            try:
                time.sleep(1)
                apacheTime = timeNow.strftime("%d/%b/%Y:%H:%M:%S %Z")

                # 127.0.0.1 - - [10/Feb/2022:15:22:42 +0200] "GET /etc/passwd HTTP/1.1" 404 488 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"

                logMessage = faker.network.ipv4 + " - - " + "[" + apacheTime + "+0200] \"" + faker.http.method.upper(
                )+" "+faker.url.path + " HTTP/1.1\" " + str(faker.http.status_code) + " " + str(faker.http.bytes) + " \"-\" \"" + faker.user_agent+"\""

                f.write(logMessage+"\n")
            except:
                print("******** An error occurred ********")

                decision = input("Continue? [Y/N]:")
                if decision.lower() == "y":
                    continue
                elif decision.lower() == "n":
                    sys.exit()
                else:
                    sys.exit()
            
    except:
        print("An error happend while openning the file")
    finally:
                f.close()





# open and read the file after the appending:
f = open("demofile.log", "r")
#print(f.read())


def main():
    socFaker= SocFaker()
    timeNow = datetime.now()
    print("Hello From Logrhthm")
    print("Current directory: "+ os.getcwd())
    makeDirectory=input("Continue? [Y/N]:")

    print(makeDirectory.lower())
    if makeDirectory.lower() =="n":
        sys.exit()
    elif makeDirectory.lower() =="y":
        apache2_access_log(socFaker,timeNow)
    else:
        main()

if __name__ == "__main__":
    main()
