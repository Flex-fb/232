import os
import asyncio
from flask import Flask
from threading import Thread
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Токен бота (вставь напрямую или через переменную окружения)
BOT_TOKEN = "8120669890:AAGRiXQ8Vf6HonUbNZKakZhCBEHipEwKSro"
# Или, если из переменной окружения:
# BOT_TOKEN = os.getenv("8120669890:AAGRiXQ8Vf6HonUbNZKakZhCBEHipEwKSro")

# Инициализация Flask
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Новая версия бота работает!"

def run_web():
    port = int(os.environ.get('PORT', 5000))
    flask_app.run(host='0.0.0.0', port=port)

# Обработчик команды /start
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Написать менеджеру ✍️", url="https://t.me/finance_creditt")],
        [InlineKeyboardButton("Подписаться на канал 🧑‍💻", url="https://t.me/financ_credit")]
    ])
    await update.message.reply_text(
        "Здравствуйте! Добро пожаловать в новый бот Finance Credit 👇",
        reply_markup=keyboard
    )

async def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_handler))
    await app.run_polling()

if __name__ == "__main__":
    Thread(target=run_web).start()
    asyncio.run(run_bot())