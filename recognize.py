import json
import os
import wave

from vosk import KaldiRecognizer, Model

from constants import MODEL_PATH, PUNCT_MODEL


def recognize_voice_vosk(audio_file_path):
    if not os.path.exists(MODEL_PATH):
        return '❗ Модель Vosk не найдена. ' \
               'Убедись, что папка с моделью находится рядом с этим файлом.'

    model = Model(MODEL_PATH)
    rec = KaldiRecognizer(model, 16000)

    wf = wave.open(audio_file_path, 'rb')
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

    if not text:
        return '❗ Не удалось распознать текст'

    text_with_punct = PUNCT_MODEL.restore_punctuation(text)

    return text_with_punct
