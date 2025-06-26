import os

from dotenv import load_dotenv
from deepmultilingualpunctuation import PunctuationModel

load_dotenv()

TOKEN = os.getenv('TOKEN')
MODEL_PATH = 'vosk-model'

PUNCT_MODEL = PunctuationModel()
