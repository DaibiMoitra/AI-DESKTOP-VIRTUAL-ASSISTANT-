import datetime
import speak1
import webbrowser
import weather
import os

def Action(send):   
    data_btn = send.lower()

    if "what is your name" in data_btn:
        speak1.speak("my name is virtual Assistant")  
        return "my name is virtual Assistant"

    elif "hello" in data_btn or "hye" in data_btn or "hay" in data_btn: 
        speak1.speak("Hey madam, How I can help you!")  
        return "Hey madam, How I can help you!" 

    elif "how are you" in data_btn:
        speak1.speak("I am doing great these days madam") 
        return "I am doing great these days madam"   

    elif "thanku" in data_btn or "thank" in data_btn:
        speak1.speak("It's my pleasure madam to stay with you")
        return "It's my pleasure madam to stay with you"      

    elif "good morning" in data_btn:
        speak1.speak("Good morning madam, I think you might need some help")
        return "Good morning madam, I think you might need some help"   

    elif "time now" in data_btn:
        current_time = datetime.datetime.now()
        Time = str(current_time.hour) + " Hour : " + str(current_time.minute) + " Minute"
        speak1.speak(Time)
        return Time 

    elif "shutdown" in data_btn or "quit" in data_btn:
        speak1.speak("ok sir")
        os._exit(0)  # optional if you want to exit
        return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak1.speak("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"

    elif 'open google' in data_btn or 'google' in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak1.speak("Google open")  
        return "Google open"

    elif 'youtube' in data_btn or "open youtube" in data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak1.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn or "open weather" in data_btn:
        url = 'https://www.weather.com/'   # or any weather site you prefer
        webbrowser.get().open(url)
        speak1.speak("Weather open") 
        return "Weather open"


    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak1.speak("songs playing...")
        return "songs playing..." 

    else:
        speak1.speak("I'm not able to understand!")
        return "I'm not able to understand!"
