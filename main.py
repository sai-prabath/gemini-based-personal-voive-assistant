import speech_recognition as sr
import wikipedia
import openai
import os
import webbrowser
import datetime
import google.generativeai as palm
from Bard import Chatbot
from config import openaiAPIkey,psid,psidts,palmAPIkey


# Speaks Query
def say(query):
    try:
        os.system(f"say {query}")
    except:
        print("Escape sequence occured, cant readable")

# Takes Voice Command
def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold= 1
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language="en - in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "some Error occured , please check your internet and say again"

# Opens a site
def OpenSite(site):
    try:
        webbrowser.open(site)
    except:
        say("sorry Can.t open site")

# Says the Time
def TellTime():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    say(f"The Time is {time}")


# bard connect
def tobard(query,response,count):
    try:
        response = chatbot.ask(query)
        return response['content']
    except:
        try:
            response=response.reply(query)
            count+=2
            return response.messages[count]['content']
        except:
            print("Sorry i can't assist you with that")



if __name__=='__main__':

    # Configuring ChatBot
    try:
        count=1
        chatbot = Chatbot(psid,psidts)
        API_KEY=palmAPIkey
        palm.configure(api_key=API_KEY)
        response=palm.chat(prompt='hi')
        print("ChatBot connected")
    except:
        print("Failed to connect...")


    say("I am voice assistant")

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
            b_res=tobard(query,response,count)
            print(b_res)
            say(b_res)


        