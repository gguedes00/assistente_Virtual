import os
import sys
import re
import time
import pygame
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
from colorama import init, Fore
from uuid import uuid4

init(autoreset=True)

class TranslationAssistant:
    def __init__(self):
        self.voice_ids = {
            'pt': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_PT-BR_MARIA_11.0',
            'en': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
        }
        
        self.engine = pyttsx3.init()
        self._configure_engine()
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        pygame.mixer.init()
        os.makedirs('translations', exist_ok=True)

    def _configure_engine(self):
        """Configura e testa as vozes instaladas"""
        self.engine.setProperty('rate', 180)
        self.engine.setProperty('volume', 1.0)
        
        available_voices = {v.id: v for v in self.engine.getProperty('voices')}
        
        for lang, voice_id in self.voice_ids.items():
            if voice_id not in available_voices:
                self._show_voice_error(lang, available_voices)
                sys.exit(1)
            
            try:
                self.engine.setProperty('voice', voice_id)
                self.engine.say("Teste de voz bem sucedido" if lang == 'pt' else "Voice test successful")
                self.engine.runAndWait()
            except Exception as e:
                print(f"{Fore.RED}❌ Falha na voz {lang.upper()}: {str(e)}{Fore.RESET}")
                sys.exit(1)

    def _show_voice_error(self, lang, available_voices):
        """Exibe vozes disponíveis em caso de erro"""
        print(f"\n{Fore.RED}ERRO: Voz {lang.upper()} não encontrada!")
        print(f"{Fore.CYAN}Vozes detectadas no sistema:{Fore.RESET}")
        for voice in available_voices.values():
            print(f" - ID: {voice.id}")
            print(f"   Nome: {voice.name}")
            print(f"   Idiomas: {voice.languages}\n")
        print(f"{Fore.YELLOW}Configure uma das vozes acima no código{Fore.RESET}")

    def get_input_mode(self):
        print(f"\n{Fore.BLUE}=== Modo de Entrada ===")
        print(f"{Fore.WHITE}1. 🎤 Usar microfone")
        print(f"2. ⌨ Digitar texto")
        print(f"3. ❌ Sair do programa{Fore.RESET}")
        return input(f"{Fore.YELLOW}► Selecione (1/2/3): {Fore.RESET}").strip()

    def voice_input(self):
        try:
            with sr.Microphone() as source:
                print(f"{Fore.CYAN}🎤 Falar agora... (aguardando 5 segundos){Fore.RESET}")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio, language='pt-BR')
                print(f"{Fore.GREEN}✅ Reconhecido: {text}{Fore.RESET}")
                return text.lower()
        except sr.WaitTimeoutError:
            print(f"{Fore.YELLOW}⏳ Tempo de gravação esgotado{Fore.RESET}")
            return ""
        except Exception as e:
            print(f"{Fore.RED}❌ Erro no reconhecimento: {str(e)}{Fore.RESET}")
            return ""

    def text_input(self):
        while True:
            text = input(f"{Fore.CYAN}✍ Digite o texto: {Fore.RESET}").strip()
            if self.validate_text(text):
                return text
            print(f"{Fore.RED}❌ Texto inválido! Use até 100 caracteres sem símbolos especiais{Fore.RESET}")

    def validate_text(self, text):
        return 0 < len(text) <= 100 and re.match(r'^[\w\sáéíóúàèìòùâêîôûãõç.,!?-]+$', text)

    def translate_text(self, text):
        try:
            pt = self.translator.translate(text, src='pt', dest='en')
            en = self.translator.translate(pt.text, src='en', dest='pt')
            return {
                'original': text,
                'translated': pt.text,
                'pronunciation': en.pronunciation or pt.text
            }
        except Exception as e:
            print(f"{Fore.RED}❌ Falha na tradução: {str(e)}{Fore.RESET}")
            return None

    def generate_audio(self, text, lang):
        try:
            self.engine.setProperty('voice', self.voice_ids[lang])
            
            safe_text = re.sub(r'[^\w\s-]', '', text)[:20]
            filename = f"{lang}_{safe_text}_{uuid4().hex[:4]}.wav"
            output_path = os.path.join('translations', filename)
            
            self.engine.save_to_file(text, output_path)
            self.engine.runAndWait()
            return output_path
        except Exception as e:
            print(f"{Fore.RED}❌ Erro na geração de áudio ({lang.upper()}): {str(e)}{Fore.RESET}")
            return None

    def play_audio(self, file_path):
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
        except pygame.error:
            print(f"{Fore.RED}❌ Erro ao reproduzir o arquivo {file_path}{Fore.RESET}")

    def run(self):
        print(f"\n{Fore.GREEN}=== TRADUTOR V2.0 ===")
        print(f"{Fore.WHITE}Sistema de Tradução PT-EN com Síntese Vocal")
        print(f"Voz Português: Maria")
        print(f"Voz Inglês: David{Fore.RESET}")
        
        while True:
            mode = self.get_input_mode()
            
            if mode == '3':
                print(f"{Fore.MAGENTA}👋 Encerrando o programa...{Fore.RESET}")
                sys.exit()
                
            if mode not in ['1', '2']:
                print(f"{Fore.RED}⚠ Opção inválida!{Fore.RESET}")
                continue
                
            text = self.voice_input() if mode == '1' else self.text_input()
            
            if not text:
                continue
                
            translation = self.translate_text(text)
            if not translation:
                continue
                
            pt_file = self.generate_audio(translation['original'], 'pt')
            en_file = self.generate_audio(translation['translated'], 'en')
            
            print(f"\n{Fore.CYAN}=== Resultados ===")
            print(f"{Fore.WHITE}🔊 Português: {translation['original']}")
            print(f"🔊 Inglês: {translation['translated']}{Fore.RESET}")
            
            if pt_file and en_file:
                print(f"{Fore.YELLOW}▶ Reproduzindo áudios...{Fore.RESET}")
                self.play_audio(pt_file)
                self.play_audio(en_file)

if __name__ == "__main__":
    try:
        TranslationAssistant().run()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}🚫 Programa interrompido pelo usuário{Fore.RESET}")
        sys.exit(0)