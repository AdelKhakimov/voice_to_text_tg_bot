# 🤖 Telegram Voice-to-Text Bot

Этот бот принимает голосовые сообщения в Telegram и преобразует их в текст с помощью 
[Vosk](https://alphacephei.com/vosk/) (офлайн-распознавание речи) и Deep Multilingual Punctuation (добавление пунктуации).  
Он поддерживает как обычные голосовые сообщения, так и кружочки (Voice Notes).

---

## 🚀 Возможности

- ✅ Распознавание русской речи офлайн
- ✅ Добавление знаков препинания к результату
- ✅ Работа с voice messages и кружочками
- ✅ Удобный запуск и настройка через `.env`

---

## ⚙ Установка

```bash
# Клонируйте репозиторий
git clone git@github.com:AdelKhakimov/voice_to_text_tg_bot.git
cd voice_to_text_tg_bot

# Создайте виртуальное окружение
python -m venv venv

# Активируйте окружение
# Для Linux / macOS:
source venv/bin/activate
# Для Windows:
venv\Scripts\activate

# Установите зависимости
pip install -r requirements.txt
```

---

## 📥 Подготовка Vosk модели

- Скачайте модель Vosk для русского языка, например:
👉 [vosk-model-small-ru-0.22](https://alphacephei.com/vosk/models)

- Распакуйте архив в папку проекта с именем vosk-model.

```bash
voice_to_text_tg_bot/
├── vosk-model/
│   └── (модельные файлы)
```

---

## 🔑 Настройка токена
- Создайте файл .env в корне проекта и добавьте в него токен.

---

## ▶ Запуск бота

```bash
python voice_bot.py
```

---

## 🗂 Структура проекта

```bash
voice_to_text_tg_bot/
├── vosk-model/            # Папка с моделью Vosk
├── buttons.py             # Логика кнопок (если используется)
├── constants.py           # Константы проекта
├── handle.py              # Обработчики сообщений
├── recognize.py           # Логика распознавания речи
├── voice_bot.py           # Основной файл запуска бота
├── requirements.txt       # Зависимости проекта
├── .env                   # Файл с токеном
└── README.md              # Описание проекта
```

---

## 🛠 Используемые технологии
| Библиотека                                                                                     | Назначение                                            |
| ---------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **[Vosk](https://alphacephei.com/vosk/)**                                                      | Офлайн-распознавание речи с поддержкой русского языка |
| **[deep-multilingual-punctuation](https://github.com/oliverguhr/deepmultilingualpunctuation)** | Добавление пунктуации к распознанному тексту          |
| **[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)**          | Работа с Telegram Bot API                             |
| **[pydub](https://github.com/jiaaro/pydub)**                                                   | Обработка и конвертация аудиофайлов                   |
| **[python-dotenv](https://pypi.org/project/python-dotenv/)**                                   | Загрузка переменных окружения из `.env` файла         |

---
## 👤 Автор проекта

**Адель Хакимов**  
💬 [Телеграм](https://t.me/KhakimovAdel)  
💼 [GitHub](https://github.com/AdelKhakimov)
