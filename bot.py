import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not configured")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🤖 AHEAD AI Bot-এ স্বাগতম!\n\n"
        "আপনি আমাকে যেকোনো মেসেজ পাঠাতে পারেন।"
    )


@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(
        message,
        "✅ আপনার মেসেজ পেয়েছি!\n\n"
        "🧠 AI এখনো সংযুক্ত করা হয়নি। পরের ধাপে AI যুক্ত করব।"
    )


print("AHEAD AI Bot is running...")

bot.infinity_polling()
