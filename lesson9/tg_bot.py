from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commans import *

app = ApplicationBuilder().token("6018411940:AAE_x7nyM3X3C1EistLXauYhG-Nu3ivEXE4").build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("days_NY", days_NY))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()
print("Server start")

app.run_polling()
