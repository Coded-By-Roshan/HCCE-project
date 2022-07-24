import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def welcome():
  speak("Hello Roshan, I am your personal assistance.How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognize...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except:
        speak("Problem in recognizing voice. Please try again")
    return query

def login_facebook():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://www.facebook.com/')
    username = driver.find_element_by_xpath('//*[@id="email"]')
    username.send_keys("username@yahoo.com")
    password = driver.find_element_by_xpath('//*[@id="pass"]')
    password("**********")
    login_btn = driver.find_element_by_xpath('//*[@id="u_0_9_SS"]')
    login_btn.click()


if __name__ == "__main__":
    welcome()
    while True:
        query = takeCommand().lower()
        if ('what is' in query) or ('who is' in query):
            query = query.replace('what is','')
            query = query.replace('who is','')
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)
            print(result)

        if 'open' in query:
            query = query.replace('open', '')
            print(query)
            webbrowser.open(query.strip())
            speak(query)
            speak("Is searched")
        
        if 'make note' in query:
            f = open("note.txt","w")
            speak("What should i note sir?")
            notes = takeCommand().lower()
            f.write(notes)
            f.close()
            speak("Noted the information")
        
        if("login" in query and "facebook" in query):
            speak("Logging to your facebook account")
            login_facebook()
          
        if 'shutdown' in query:
            exit()
        


    

