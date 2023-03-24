import speech_recognition as sr
import webbrowser
import subprocess
import os
# create a recognizer object
r = sr.Recognizer()
text = ""
# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")

    # continuously listen for audio and convert it to text
    while True:
        # listen for the user's input
        audio = r.listen(source)

        try:
            # recognize speech using Google Speech Recognition
            text = r.recognize_google(audio)
            test = '''open chittappan tracker open chittapan tracker open chitapan tracker open tracker open sithappan racket open situp and tracker open sit apan tracker open Chittagong tracker open set up and tracker  open setup and tracker open sit up and tracker
            open situp and rocker 
            bus tracker'''
            text_1_close = '''close tracker close chittapan tracker close chitappan tracker close chittappan tracker close set up and tracker close sit up and tracker
            close setup and tracker close situp and rocker close it pen tracker close chit up and tracker
            close chittagong tracker close Chitta pandrakar
            '''
            windows = {}
            text_discord = ''' 
            open discord discord escort listening open discord open the sport pin code open Disco open discord discord open the score open the Scott
            open scot open Disco viscose open the spot open the sport
            '''
            text_telegram = '''
            open telegram telegram
            '''
            text_computer = '''
            open computer my computer my pc open my computer
            '''
            print(text)
            if(text in test):
                link = "https://chittapan-tracker.onrender.com" 
                windows['chittapan'] = webbrowser.open_new_tab(link)
            test_1 = '''bus track one track bus number one number ones bus truck 1 bus number 1 track bus number 1 Raat bus number 1'''
            if(text in test_1):
                link_bus_no_1 = "https://chittapan-tracker.onrender.com/bus_no_1"
                windows['bus_no_1'] = webbrowser.open_new_tab(link_bus_no_1)

            if(text in text_1_close):
                if 'chittapan' in windows:
                    windows['chittapan'].close()
            if(text in text_telegram):
                subprocess.Popen("C:\\Users\\Acer\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
            if(text in text_discord):
                subprocess.Popen("C:\\Users\\Acer\\AppData\\Local\\Discord\\app-1.0.9011\\Discord.exe")
            if(text in text_computer):
                subprocess.Popen('explorer /This PC,"::{20D04FE0-3AEA-1069-A2D8-08002B30309D}"')

        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print("Sorry, my speech service is currently down. Error: " + str(e))


