from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

t = threading.Thread(target=run)
t.start()

import telebot
from telebot import types

TOKEN = "8237720592:AAFBGoTBvFnduKD5E9Qo3PQtHD4IU63H2Zw"
bot = telebot.TeleBot(TOKEN)

# آیدی عددی خودت
ADMIN_ID = 7741371216

WELCOME_TEXT = """به نام سیروس بخشنده مهربان

اینجا یه چیزی شبیه اون چاهه توی قم هستش، نامه هاتو به دستم میرسونه و من تصمیم میگیرم به..رم بگیرم یا نگیرم
میتونی یجوری بفرستی که بشناسمت میتونی هم بی خایه بازی در بیاری ناشناس بفرستی
واسه خدا اصلا اهمیت نداره

گزینه‌های این پایینم کوفتت بشه
"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📌 گزینه اول")
    btn2 = types.KeyboardButton("ℹ️ گزینه دوم")
    btn3 = types.KeyboardButton("📞 گزینه سوم")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, WELCOME_TEXT, reply_markup=markup)

@bot.message_handler(content_types=['text', 'photo', 'video', 'voice', 'sticker', 'document', 'audio'])
def forward_to_admin(message):
    try:
        # مشخصات کاربر
        user_info = f"📩 پیام از: {message.from_user.first_name or ''} @{message.from_user.username or ''} (ID:{message.from_user.id})"
        bot.send_message(ADMIN_ID, user_info)

        # فوروارد پیام در همان قالب اصلی
        bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    except Exception as e:
        print("Error:", e)

bot.infinity_polling()
