# importar a biblioteca
import speech_recognition as sr

 

# Recognizer serve para reconhecer
rec = sr.Recognizer()

 

#iniciar o microfone
with sr.Microphone() as mic:

 

#ajutar ao barulho ambiente (do microfone)
    rec.adjust_for_ambient_noise(mic)
    print('Fale algo e aguarde ...')
#captar o audio (do microfone)
    audio = rec.listen(mic)
#transformar o audio em texto pelo google (reconhece a variavel audio, escolha a lingua)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)

 

#abrir navegador
    if "navegador" in texto:
        os.system('start Chrome.exe')

