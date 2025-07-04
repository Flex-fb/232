import os
import asyncio
import nest_asyncio
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

nest_asyncio.apply()

TOKEN = "8120669890:AAGRiXQ8Vf6HonUbNZKakZhCBEHipEwKSro"

app = Flask(__name__)

@app.route("/")
def home():
    return "Бот работает!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Написать менеджеру ✍️", url="https://t.me/finance_creditt")],
        [InlineKeyboardButton("Подписаться на канал 🧑‍💻", url="https://t.me/financ_credit")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Здравствуйте, уважаемый клиент! Вы попали в бот компании Finance Credit 👇👇👇",
        reply_markup=reply_markup
    )

async def main():
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    await app_bot.run_polling()

if __name__ == "__main__":
    Thread(target=run_flask).start()
    asyncio.run(main())