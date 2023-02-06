from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from prophecy import prophecies
from datetime import datetime
import random
import math, decimal

dec = decimal.Decimal


def get_prophecy_text():
    return prophecies[random.randint(0, len(prophecies))]


def position():
    now = datetime.now()

    diff = now - datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))

    return lunations % dec(1)


def phase(pos):
    index = (pos * dec(8)) + dec("0.5")
    index = math.floor(index)
    return {
      0: "Новолуние",
      1: "Молодая луна",
      2: "Первая четверть",
      3: "Прибывающая луна",
      4: "Полнолуние",
      5: "Убывающая луна",
      6: "Последняя четверть",
      7: "Старая луна"
    }[int(index) & 7]


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}! \n'
                                    f'Смотри, что я умею: \n'
                                    f'/hi - здороваться; \n'
                                    f'/time - знаю время; \n'
                                    f'/days_NY - знаю, сколько дней до Нового года; \n'
                                    f'/prophecy - расскажу, что ждет в Новом году; \n'
                                    f'/moon_phase - покажу фазу Луны; \n'
                                    f'/sum - умею считать сумму 2 чисел.')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/days_NY\n/prophecy\n/moon_phase')


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


async def prophecy_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(get_prophecy_text())


async def moon_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pos = position()

    await update.message.reply_text(f'{phase(pos)} ({round(float(pos), 3)})')
