import os

from pydub import AudioSegment
from telegram import Update
from telegram.ext import ContextTypes

from recognize import recognize_voice_vosk


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


async def handle_video_note(update: Update,
                            context: ContextTypes.DEFAULT_TYPE
                            ):
    file = await update.message.video_note.get_file()
    ogg_path = 'video_note.ogg'
    wav_path = 'video_note.wav'

    await file.download_to_drive(ogg_path)

    # Конвертация в WAV с нужными параметрами
    audio = AudioSegment.from_file(ogg_path)
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    audio.export(wav_path, format='wav')

    text = recognize_voice_vosk(wav_path)

    await update.message.reply_text(text)

    os.remove(ogg_path)
    os.remove(wav_path)
