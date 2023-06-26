import PyPDF2
import pyttsx3



book = open("O Homem que Confundiu sua Mulher com um Chapéu - Oliver Sacks.pdf", "rb")
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

entire_book = ''
for i in range(pages):
    entire_book += pdfReader.pages[i].extract_text()


entire_book = entire_book.replace('\n', ' ')

# page = pdfReader.getPage(20)
# text = page.extractText()
# speaker = pyttsx3.init()
# speaker.say(text)
# speaker.runAndWait()

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Código para mudar a voz.
# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()
#     engine.stop()


voice_id_ingles_mulher = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
voice_id_ingles_homem = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
voice_id_portugues_mulher = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0'

engine.setProperty('voice', voice_id_portugues_mulher)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

# engine.say(updated_text)
engine.save_to_file(entire_book, 'audio.mp3')
engine.runAndWait()
print(entire_book)
