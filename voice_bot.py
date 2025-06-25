import os
import json
import wave
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
MODEL_PATH = 'vosk-model'  # Папка с моделью Vosk (например vosk-model-small-ru-0.22)

def recognize_voice_vosk(audio_file_path):
    if not os.path.exists(MODEL_PATH):
        return '❗ Модель Vosk не найдена. Убедись, что папка с моделью находится рядом с этим файлом.'

    model = Model(MODEL_PATH)
    rec = KaldiRecognizer(model, 16000)

    wf = wave.open(audio_file_path, "rb")
    results = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            results.append(res.get('text', ''))

    res = json.loads(rec.FinalResult())
    results.append(res.get('text', ''))

    text = ' '.join(results).strip()
    return text if text else '❗ Не удалось распознать текст'

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.voice.get_file()
    ogg_path = 'voice.ogg'
    wav_path = 'voice.wav'

    await file.download_to_drive(ogg_path)

    # Конвертация OGG -> WAV с нужными параметрами
    audio = AudioSegment.from_file(ogg_path)
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    audio.export(wav_path, format='wav')

    text = recognize_voice_vosk(wav_path)

    await update.message.reply_text(text)

    os.remove(ogg_path)
    os.remove(wav_path)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('👋 Привет! Отправь голосовое сообщение, и я его расшифрую.')

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))

    print('🤖 Бот запущен. Ждём голосовые сообщения...')
    app.run_polling()

if __name__ == '__main__':
    main()
