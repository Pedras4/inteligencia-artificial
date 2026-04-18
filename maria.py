import speech_recognition as sr
import os
import pyttsx3 as tts
import datetime
import wikipedia
import pywhatkit
import pyautogui
from time import sleep

engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
engine.say("Fale comigo beibi")
engine.runAndWait()

rec = sr.Recognizer()

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Fale algo agora ...")
    audio = rec.listen(mic)
    texto = rec.recognize_goggle(audio, language="pt-PT")
    print(texto)
    
    if "Maria" in texto:
        
        if "navegador" in texto:
            os.system("start Chrome.exe")
            
        elif "horas" in texto:
            hora = datetime.datetime.now().strftime("%H:%M")
            engine.say("Agora são" + hora)
            engine.runAndWait()
            
        elif "Procure por" in texto:
            procurar = texto.replace("Maria Prouce por","")
            wikipedia.set_lang("pt")
            resultado = wikipedia.summary(procurar, 2)
            print(resultado)
            engine.say(resultado)
            engine.runAndWait()
            
        elif "toque" in texto:
            toque = texto.replace("Maria Toque","")
            pywhatkit.sendwhatmsg("+351911716901","Teste Phyton", 16, 13)
            print(busca)
            
        elif "Quem é" in texto:
            link = texto.replace("Maria Quem é","")
            pyautogui.press("win")
            sleep(0,5)
            pyautogui.press("win")
            sleep(0,5)
            pyautogui.press("win")
            sleep(0,5)
            pyautogui.write("Chrome")
            sleep(1)
            pyautogui.write("http://linkedin.com/")
            sleep(1)
            pyautogui.press("enter")
            sleep(5)
            pyautogui.press(["tab", "tab", "tab", "tab", "tab"])
            sleep(2)
            pyautogui.write(link, interval=0.05)
            pyautogui.press("enter")