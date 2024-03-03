from __init__ import *

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
def tobard(chatbot,query,response,count):
    try:
        response = chatbot.ask(query)
        return [response['content'],0]
    except:
        try:
            response=response.reply(query)
            return [response.messages[count]['content'],1]
        except:
            return ["Sorry i can.t assist you with that",1]

            