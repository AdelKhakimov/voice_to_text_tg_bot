from telegram.ext import (Application, CommandHandler,
                          MessageHandler, filters)

from buttons import start
from constants import TOKEN
from handle import handle_voice, handle_video_note


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.add_handler(MessageHandler(filters.VIDEO_NOTE, handle_video_note))

    print('🤖 Бот запущен. Ждём голосовые сообщения...')
    app.run_polling()


if __name__ == '__main__':
    main()
