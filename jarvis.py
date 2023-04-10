0
import speech_recognition as sr    #To convert speech into text
import pyttsx3                     #To convert text into speech
import datetime                    #To get the date and time
import wikipedia                   #To get information from wikipedia
import webbrowser                  #To open websites
import os                          #To open files
import time                        #To calculate time
import subprocess                  #To open files
from tkinter import *              #For the graphics
import pyjokes                     #For jokes
from playsound import playsound    #To play sounds
import keyboard                    #To add keyboard activation 
from pydub import AudioSegment
from pydub.playback import play 
import pyaudio
import pywhatkit as kt
import random
import sys
import eel

name_assistant = "Eedith" #The name of the assistant


engine = pyttsx3.init('sapi5')   #'sapi5' is the argument you have to use for windows, I am not sure what it is for Mac and Linux
voices = engine.getProperty('voices')  #To get the voice
engine.setProperty('voice', voices[1].id) #defines the gender of the voice. 

# print(voices[1].id)  0 -> Male Voice.  1-> Female Voice


def speak(text):
    engine.say(text)
    print(name_assistant + " : "  +  text)
    engine.runAndWait()


def get_audio(): 

    r = sr.Recognizer() 
    audio = '' 

    with sr.Microphone() as source: 

        print("Listening...") 
        r.energy_threshold = 100
        r.pause_threshold = 1
        audio = r.listen(source)  
        
    try: 
        print("Recognizing...")
        text = r.recognize_google(audio) 
        print('You ' + ': '+ text)
        return text

    except:
        speak("Please say again")
        return get_audio()
        return "None"


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Eedith, your voice assistant. How can I help you?")


def date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    
    # print(now)
    # print(my_date)

    month_name = now.month
    day_name = now.day
    year_no = str(now.year)
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st'] 
    
    speak("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + " , " + year_no + '.')


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def wikipedia_screen(text):


  wikipedia_screen = Toplevel(screen)
  wikipedia_screen.title(text)
  wikipedia_screen.iconbitmap('app_icon.ico')

  message = Message(wikipedia_screen, text= text)
  message.pack()

# @eel.expose
def Process_audio():
    # eel.init('WebPageFolder')
    # eel.start('jarvis_webpage.html')
    run = 1
    if __name__=='__main__':
        while run==1:    

            app_string = ["open word", "open powerpoint", "open excel","open notepad", "open microsoft edge", "open paint"]
            app_link = [r'\Word.lnk',r'\PowerPoint.lnk', r'\Excel.lnk', r'\Accessories\Notepad.lnk', r'\Microsoft Edge.lnk', r'\Accessories\Paint.lnk' ]
            app_dest = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs' # Write the location of your file

            statement = get_audio().lower()
            results = ''

            if "hello" in statement or "hi" in statement:
                wishMe()               


            elif "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
                speak('Your personal assistant ' + name_assistant +' is shutting down, Good bye')
                # screen.destroy()
                break

            elif 'wikipedia' in statement:
              try:
                speak('Searching Wikipedia...')
                kt.search(statement)
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences = 3)
                speak("According to Wikipedia")
                wikipedia_screen(results)
              except:
                speak("Error")

              speak(results)

            elif 'joke' in statement:
              speak(pyjokes.get_joke())    
     
            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("Opening Youtube")
                time.sleep(5)


            elif 'open google' in statement or 'open chrome' in statement:
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Opening Google chrome")
                    time.sleep(5)


            elif 'open gmail' in statement:
                    webbrowser.open_new_tab("mail.google.com")
                    speak("Opening Google Mail")
                    time.sleep(5)

            elif 'open netflix' in statement:
                    webbrowser.open_new_tab("netflix.com/browse") 
                    speak("Opening Netflix")


            elif 'open prime video' in statement:
                    webbrowser.open_new_tab("primevideo.com") 
                    speak("Opening Amazon Prime Video")
                    time.sleep(5)

            elif app_string[0] in statement:
                os.startfile(app_dest + app_link[0])

                speak("Opening Microsoft office Word")

            elif app_string[1] in statement:
                os.startfile(app_dest + app_link[1])
                speak("Opening Microsoft office PowerPoint")

            elif app_string[2] in statement:
                os.startfile(app_dest + app_link[2])
                speak("Opening Microsoft office Excel")
        
            elif app_string[3] in statement:
                os.startfile(app_dest + app_link[3])
                speak("Opening Notepad")
            
            elif app_string[4] in statement:
                os.startfile(app_dest + app_link[5])
                speak("Opening Microsoft Edge")
                       
            elif app_string[5] in statement:
                os.startfile(app_dest + app_link[6])
                speak("Opening Paint")

            elif 'news' in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com")
                speak('Here are some headlines from the Times of India. Happy reading!')
                time.sleep(6)

            elif 'cricket' in statement:
                news = webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from cricbuzz')
                time.sleep(6)

            elif 'corona' in statement or 'covid' in statement or 'covid-19' in statement:
                news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 numbers')
                time.sleep(6)

            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'date' in statement:
                date()

            elif 'play music' in statement or 'music'in statement:
                music_dir = "D:\Music"
                songs = os.listdir(music_dir)
                speak("Playing Music from your PC")
                os.startfile(os.path.join(music_dir,random.choice(songs)))

            elif 'who are you' in statement or 'what can you do' in statement or 'what is your name' in statement:
                    speak('I am '+name_assistant+', your personal assistant. I am programmed to do minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra') 


            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by Pervez Ahmed Shaik")

            
            elif 'make a note' in statement:
                statement = statement.replace("make a note", "")
                note(statement)


            elif 'note this' in statement:    
                statement = statement.replace("note this", "")
                note(statement)         


            elif 'open code' in statement:
                speak("opening Visual Studio Code")
                codePath = "D:\Visual Studio Code\Microsoft VS Code\Code.exe"
                os.startfile(codePath)

            elif 'play a video' in statement or 'play video' in statement:
                speak("Please say the video to be played")
                query=get_audio()
                speak("Playing")
                kt.playonyt(query)

            elif 'search' in statement:
                speak("Please say the topic to be searched")
                query=get_audio()
                speak("Searching")
                kt.search(query)

            elif 'meaning' in statement:
                kt.search(statement)

            else:
                speak("Searching")
                kt.search(statement)


if __name__ == "__main__":
    
    speak("Hi Pervez!")

    wishMe()
    eel.init('WebPageFolder')
    eel.start('jarvis_webpage.html')
    Process_audio()
    
        
                        
# def change_name():

#   name_info = name.get()

#   name_assistant = name_info

#   file=open("Assistant_name", "w")

#   file.write(name_info)

#   file.close()

#   settings_screen.destroy()


# def change_name_window():
    
#       global settings_screen
#       global name


#       settings_screen = Toplevel(screen)
#       settings_screen.title("Settings")
#       settings_screen.geometry("300x300")
#       settings_screen.iconbitmap('app_icon.ico')

      
#       name = StringVar()

#       current_label = Label(settings_screen, text = "Current name: "+ name_assistant)
#       current_label.pack()

#       enter_label = Label(settings_screen, text = "Please enter your Virtual Assistant's name below") 
#       enter_label.pack(pady=10)   
      

#       Name_label = Label(settings_screen, text = "Name")
#       Name_label.pack(pady=10)
     
#       name_entry = Entry(settings_screen, textvariable = name)
#       name_entry.pack()


#       change_name_button = Button(settings_screen, text = "Ok", width = 10, height = 1, command = change_name)
#       change_name_button.pack(pady=10)


# def info():

#   info_screen = Toplevel(screen)
#   info_screen.title("Info")
#   info_screen.iconbitmap('app_icon.ico')

#   creator_label = Label(info_screen,text = "Created by Pervez Ahmed Shaik")
#   creator_label.pack()


# keyboard.add_hotkey("F4", Process_audio)


# def main_screen():

#       global screen
#       screen = Tk()
#       screen.title(name_assistant)
#       screen.geometry("500x750")
#       screen.iconbitmap('app_icon.ico') #The bitmap must be an ico type, but not png or jpg type, otherwise, the image will not display as the icon.


#       name_label = Label(text = name_assistant,width = 300, bg = "black", fg="white", font = ("Calibri", 13))
#       name_label.pack()


#       microphone_photo = PhotoImage(file = "assistant_logo.png")
#       microphone_button = Button(image=microphone_photo, command = Process_audio)
#       microphone_button.pack(pady=10)

#       settings_photo = PhotoImage(file = "settings.png")
#       settings_button = Button(image=settings_photo, command = change_name_window)
#       settings_button.pack(pady=10)
       
#       info_button = Button(text ="Info", command = info)
#       info_button.pack(pady=10)

#       screen.mainloop()



