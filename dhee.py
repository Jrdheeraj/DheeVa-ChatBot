import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import threading
from transformers import pipeline
class LocalAIVoiceChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline AI Voice & Text Chatbot")
        self.root.geometry("800x600")
        self.root.configure(bg="#2C3E50")

        
        self.generator = pipeline("text-generation", model="gpt2")

        
        self.tts_engine = pytts
        x3.init()
        self.tts_engine.setProperty('rate', 150)

        
        self.recognizer = sr.Recognizer()

        self.listening = False
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self.root, text="🤖 Offline AI Voice & Text Chatbot",
            font=("Arial", 20, "bold"), fg="white", bg="#2C3E50"
        )
        title_label.pack(pady=10)

        self.chat_display = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, width=80, height=20,
            font=("Arial", 10), bg="#ECEFF1", fg="#0C243C"
        )
        self.chat_display.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        input_frame = tk.Frame(self.root, bg="#2C3E50")
        input_frame.pack(fill=tk.X, padx=20, pady=(0, 10))

        self.text_input = tk.Entry(input_frame, font=("Arial", 12), bg="white", width=50)
        self.text_input.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)
        self.text_input.bind("<Return>", self.send_text_message)

        send_btn = tk.Button(input_frame, text="Send", command=self.send_text_message,
                             bg="#3498DB", fg="white", font=("Arial", 10, "bold"), width=8)
        send_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.voice_btn = tk.Button(input_frame, text="🎤 Voice", command=self.toggle_voice_input,
                                   bg="#E74C3C", fg="white", font=("Arial", 10, "bold"), width=10)
        self.voice_btn.pack(side=tk.LEFT, padx=(0, 10))

        clear_btn = tk.Button(input_frame, text="Clear", command=self.clear_chat,
                              bg="#95A5A6", fg="white", font=("Arial", 10, "bold"), width=8)
        clear_btn.pack(side=tk.LEFT)

        self.status_label = tk.Label(self.root, text="Ready to chat! Type or use voice input.",
                                     font=("Arial", 10), fg="white", bg="#2C3E50")
        self.status_label.pack(pady=(0, 10))

        self.add_to_chat("Bot", "Hello! I'm your offline AI assistant. You can type or speak to me!")

    def add_to_chat(self, sender, message):
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.see(tk.END)

    def send_text_message(self, event=None):
        message = self.text_input.get().strip()
        if message:
            self.text_input.delete(0, tk.END)
            self.add_to_chat("You", message)
            threading.Thread(target=self.get_ai_response, args=(message,), daemon=True).start()

    def toggle_voice_input(self):
        if not self.listening:
            self.start_voice_input()
        else:
            self.stop_voice_input()

    def start_voice_input(self):
        self.listening = True
        self.voice_btn.config(text="🔴 Listening...", bg="#E67E22")
        self.status_label.config(text="Listening... Speak now!")
        threading.Thread(target=self.listen_for_voice, daemon=True).start()

    def stop_voice_input(self):
        self.listening = False
        self.voice_btn.config(text="🎤 Voice", bg="#E74C3C")
        self.status_label.config(text="Ready to chat!")

    def listen_for_voice(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = self.recognizer.recognize_google(audio)
            self.root.after(0, self.process_voice_input, text)
        except sr.WaitTimeoutError:
            self.root.after(0, self.handle_voice_error, "Listening timeout.")
        except sr.UnknownValueError:
            self.root.after(0, self.handle_voice_error, "Could not understand audio.")
        except sr.RequestError as e:
            self.root.after(0, self.handle_voice_error, f"Speech recognition error: {e}")
        finally:
            self.root.after(0, self.stop_voice_input)

    def process_voice_input(self, text):
        self.add_to_chat("You (Voice)", text)
        threading.Thread(target=self.get_ai_response, args=(text,), daemon=True).start()

    def handle_voice_error(self, error_msg):
        self.status_label.config(text=error_msg)

    def get_ai_response(self, user_message):
        """Generate AI response locally using GPT-2"""
        try:
            self.root.after(0, lambda: self.status_label.config(text="AI is thinking..."))
            result = self.generator(user_message, max_length=100, num_return_sequences=1)
            ai_response = result[0]['generated_text'].replace(user_message, "").strip()
            self.root.after(0, self.display_ai_response, ai_response)
        except Exception as e:
            self.root.after(0, self.display_ai_response, f"Error: {e}")

    def display_ai_response(self, response):
        self.add_to_chat("Bot", response)
        self.status_label.config(text="Ready to chat!")
        threading.Thread(target=self.speak_response, args=(response,), daemon=True).start()

    def speak_response(self, text):
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            print("TTS Error:", e)

    def clear_chat(self):
        self.chat_display.delete(1.0, tk.END)
        self.add_to_chat("Bot", "Chat cleared! How can I help you?")


if __name__ == "__main__":
    root = tk.Tk()
    app = LocalAIVoiceChatbot(root)
    root.mainloop()
