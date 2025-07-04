import os
import asyncio
import nest_asyncio  # добавляем

from flask import Flask
from threading import Thread

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ Применяем обход ограничения с event loop
nest_asyncio.apply()

# Токен Telegram-бота
BOT_TOKEN = os.getenv("8120669890:AAHnEgED5Ehacuwr1QgOIh7ISBpM9Uc6sms")

# Flask-приложение
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Бот работает!"

# Запускаем Flask-сервер
def run_web():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)

# /start обработчик
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Написать менеджеру ✍️", url="https://t.me/finance_creditt")],
        [InlineKeyboardButton("Подписаться на канал 🧑‍💻", url="https://t.me/financ_credit")]
    ])
    await update.message.reply_text(
        "Здравствуйте! Добро пожаловать в новый бот Finance Credit 👇",
        reply_markup=keyboard
    )

# Основной бот
async def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_handler))
    await app.run_polling()

# Запуск Flask и бота
if __name__ == "__main__":
    Thread(target=run_web).start()
    asyncio.run(run_bot())