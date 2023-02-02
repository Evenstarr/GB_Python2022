from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}! \n'
                                    f'Смотри, что я умею: \n'
                                    f'/hi - здороваться; \n'
                                    f'/time - знаю время; \n'
                                    f'/sum - умею считать сумму 2 чисел.')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    if len(items) == 3:
        a = int(items[1])
        b = int(items[2])
        message = a + b
    else:
        message = 'Нужно ввести 2 числа через пробел'
    await update.message.reply_text(message)
