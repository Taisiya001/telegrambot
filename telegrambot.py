from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5657387203:AAG3oc-Bq_Pl37UME2tjxuPYxwoQ-XZvfKc')
updater = Updater(token='5657387203:AAG3oc-Bq_Pl37UME2tjxuPYxwoQ-XZvfKc')
dispatcher = updater.dispatcher

        

def message(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, ' '.join(w for w in text.split(' ') if not w.startswith('абв')))

message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()  # ctrl + c