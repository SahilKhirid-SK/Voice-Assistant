import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
   hour= int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak("Good Morining")

   elif hour>=12 and hour<18:
      speak("Good Afternoon")

   else:
      speak("Good Evening")

   speak("I am your assistant how may I help you")

def takeCommand():
     #It takes microphone input from the user and returns string output

     r=sr.Recognizer()
     with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

     try:
         print("Recognizing...")
         query=r.recognize_google(audio, language='en-in')
         print(f"user said: {query}\n")

     except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
     return query

if __name__ == '__main__':
    wishMe()
    while True:
   # if 1:
          query=takeCommand().lower()

          if 'wikipedia' in query:
              speak('Searching wikipedia...')
              print("Searching wikipedia...")
              query=query.replace("wikipedia","")
              results=wikipedia.summary(query,sentences=2)
              speak("According to wikipedia")
              print(results)
              speak(results)

          elif 'open youtube' in query:
              speak("Opening youtube")
              webbrowser.open("youtube.com")

          elif 'open google' in query:
              speak("Opening Google")
              webbrowser.open("google.com")


          elif 'open gmail' in query:
              speak("Opening gmail")
              webbrowser.open("gmail.com")

          elif 'play music' in query:
              speak("Playing song")
              music_dir='D:\\music'
              songs=os.listdir(music_dir)
              print(songs)
              os.startfile(os.path.join(music_dir,songs[0]))

          elif 'what is time' in query:
              strTime=datetime.datetime.now().strftime("%H:%M:%S")
              speak(f"time is {strTime}")

          elif'open my data' in query:
              speak("opening your data")
              codePath='D:\\SAHIL_DATA'
              os.startfile(codePath)

          elif 'stop' in query:
              speak("Thankyou for using voice assistant Have a great day")
              exit(0)













