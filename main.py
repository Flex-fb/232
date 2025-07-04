import os
import nest_asyncio
import asyncio
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ Применяем патч для event loop
nest_asyncio.apply()

# ✅ Токен лучше вытянуть из переменной окружения, но можно напрямую
BOT_TOKEN = "8120669890:AAGRiXQ8Vf6HonUbNZKakZhCBEHipEwKSro"

# ✅ Flask-сервер
app = Flask(__name__)

@app.route("/")
def home():
    return "Бот работает!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# ✅ Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Написать менеджеру ✍️", url="https://t.me/finance_creditt")],
        [InlineKeyboardButton("Подписаться на канал 🧑‍💻", url="https://t.me/financ_credit")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Здравствуйте! Добро пожаловать в бот Finance Credit 👇",
        reply_markup=reply_markup
    )

# ✅ Асинхронный запуск бота
async def main():
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    await app_bot.run_polling()

# ✅ Запуск Flask и бота параллельно
if __name__ == "__main__":
    Thread(target=run_flask).start()
    asyncio.run(main())