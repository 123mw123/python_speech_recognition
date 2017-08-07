
#part of the code is taken from https://pythonspot.com/en/personal-assistant-jarvis-in-python/


import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from playsound import playsound

import webbrowser

audiofile = 1

def speak(audioString):
    global audiofile
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    file1 = str("hello" + str(audiofile) + ".mp3")
    tts.save(file1)
    playsound(file1, False)
    os.remove(file1)
    audiofile = audiofile+1



def recordAudio():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


    data = ""
    try:

        data = r.recognize_google(audio)
        print("You said: " + data)


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def automate(data):


    if "how are you" in data:
        speak("I am fine")


    if "what time is it" in data:
        speak(ctime())


    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold Sai Teja Ramadev, I will show you where " + location + " is.")
        webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")


     #when you say play songs,this part will search available songs on your pc and play it for you
    if "song" in data:

        songlist = [i for i in os.listdir("C:\Users\saiteja\Music") if i[len(i)-1:len(i)] == str(3)]
        for i in range(len(songlist)):

                print i, "-->" + songlist[i]

        speak("Choose song to play")
        item = recordAudio()
        print 2
        os.startfile(os.path.join("C:\Users\saiteja\Music\\" +songlist[int(item)]))

    if "Facebook" in data:
        webbrowser.open("https://www.facebook.com/")
	
	
        #opening gmail
    if "Gmail" in data:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        data = ""


      #searching on youtube
    if "Youtube" in data:

        data = data.split(" ")
        webbrowser.open("https://www.youtube.com/results?search_query="+data[0])


	#searching on google
    if "Google" in data:
        data = data.split(" ")
        webbrowser.open("https://www.google.co.in/search?q="+data[1])


time.sleep(2)
speak("Hi Sai Teja Ramadev, what can I do for you?")


while 1:
    data = recordAudio()
    automate(data)
