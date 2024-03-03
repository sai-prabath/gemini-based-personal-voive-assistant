from __init__ import *
from functions import *

if __name__=='__main__':

    # Configuring ChatBot
    try:
        count=1
        chatbot = Chatbot(psid,psidts)
        print("ChatBot connected")
    except:
        chatbot=""
        API_KEY=palmAPIkey
        palm.configure(api_key=API_KEY)
        response=palm.chat(prompt='hi')
        print("Failed to connect to internet.. generetes pretrained response")
        say("Failed to connect to internet.. generetes pretrained response")

    while(True):

        print("im listening....")
        say("I.m listening")
        query = takecmd()
        
        # quit
        if "close".lower() in query.lower():
            say("mac signing off")
            break

        # Sites checker
        sites=[["youtube","https://youtube.com"]]

        if "open".lower() in query.lower():
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    say(f"opening.. {site[0]}")
                    OpenSite(site[1])
                    break

        # Time
        if "time".lower() in query.lower():
            TellTime()


        #bard call
        if "mac".lower() in query.lower():
            b_res=tobard(chatbot,query,response,count)
            if b_res[1]==1:
                count+=2
            print(b_res)
            say(b_res[0])


        