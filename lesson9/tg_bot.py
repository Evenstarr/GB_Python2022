from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commans import *
from settings import token

app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("days_NY", days_NY))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()
print("Server start")

app.run_polling()
