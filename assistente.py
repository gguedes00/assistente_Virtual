import sounddevice as sd
import speech_recognition as sr
import pyttsx3
import os
import sys
import time
import webbrowser
from colorama import init, Fore

init()

class Colors:
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    YELLOW = Fore.YELLOW
    GREEN = Fore.GREEN
    RED = Fore.RED
    BLUE = Fore.BLUE
    END = Fore.RESET

content_dir = os.path.join(os.getcwd(), "content")
os.makedirs(content_dir, exist_ok=True)

def get_audio():
    """Captura áudio do microfone e converte para texto"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(Colors.CYAN + "Ouvindo..." + Colors.END)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        print(Colors.YELLOW + f"COMANDO RECONHECIDO: {text}" + Colors.END)
        return text.lower()
    except sr.UnknownValueError:
        print(Colors.RED + "Não entendi o que você disse." + Colors.END)
        return ""
    except sr.RequestError:
        print(Colors.RED + "Erro ao conectar com o serviço de reconhecimento." + Colors.END)
        return ""

def speak(text, lang="pt-br"):
    """Sintetiza voz a partir do texto"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.say(text)
    engine.runAndWait()

def clear_terminal():
    """Limpa o terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def respond(command):
    """Processa os comandos de voz"""
    sites = {
        'google': ("Google", "https://www.google.com"),
        'wikipedia': ("Wikipedia", "https://www.wikipedia.org"),
        'wikipédia': ("Wikipedia", "https://www.wikipedia.org"),
        'youtube': ("YouTube", "https://www.youtube.com"),
        'dio': ("DIO", "https://www.dio.me/"),
        'dio.me': ("DIO", "https://www.dio.me/"),
        'plataforma dio': ("DIO", "https://www.dio.me/"),
        'digital innovation one': ("DIO", "https://www.dio.me/"),
    }

    exit_commands = ['sair', 'encerrar', 'fechar', 'parar']
    if any(exit_cmd in command for exit_cmd in exit_commands):
        print(Colors.WHITE + "\nFinalizando o programa..." + Colors.END)
        speak("Finalizando o programa...")
        time.sleep(1)
        clear_terminal()
        sys.exit()

    for key in sites:
        if key in command:
            name, url = sites[key]
            print(Colors.GREEN + f"\nAbrindo {name}..." + Colors.END)
            speak(f"Abrindo {name}")
            webbrowser.open(url)
            return

    print(Colors.RED + "\nComando não reconhecido!" + Colors.END)
    speak("Desculpe, não entendi o comando. Por favor, tente novamente.")

print(Colors.WHITE + "\n--- Assistente Virtual por Voz ---\n" + Colors.END)
speak("Bem vindo ao Assistente Virtual. Você pode pedir para abrir Google, Wikipedia, YouTube, DIO ou dizer 'sair' para encerrar.")

while True:
    print(Colors.CYAN + "\nDiga um comando (ou 'sair' para encerrar)..." + Colors.END)
    command = get_audio()
    
    if command:
        respond(command)
    else:
        speak("Não consegui entender. Por favor, repita o comando.")