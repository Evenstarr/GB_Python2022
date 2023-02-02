from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}! \n'
                                    f'Смотри, что я умею: \n'
                                    f'/hi - здороваться; \n'
                                    f'/time - знаю время; \n'
                                    f'/days_NY - знаю, сколько дней до Нового года; \n'
                                    f'/sum - умею считать сумму 2 чисел.')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/days_NY')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.now().time()}')


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


async def days_NY(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.today()
    new_year = datetime(now.year + 1, 1, 1)
    d = new_year-now
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)

    await update.message.reply_text('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))
