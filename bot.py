from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Замените 'YOUR_TOKEN' на токен вашего бота
TOKEN = 'YOUR_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправь мне свой отзыв или вопрос, и я отвечу на него.')

def feedback(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Спасибо за ваш ответ! Я его получил и могу ответить на него. Это занимает не более 24 часов. Ожидай, имей терпение')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, feedback))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main() 
    
