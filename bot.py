import os
import telebot
from google import genai

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

bot = telebot.TeleBot(BOT_TOKEN)

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL = "gemini-2.5-flash"


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🤖 AHEAD AI-তে স্বাগতম!\n\n"
        "আপনি আমাকে যেকোনো প্রশ্ন করতে পারেন।"
    )


@bot.message_handler(func=lambda message: True)
def ai_reply(message):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=message.text
        )

        answer = response.text

        if not answer:
            answer = "দুঃখিত, এখন কোনো উত্তর তৈরি করা যায়নি।"

        bot.reply_to(message, answer)

    except Exception as e:
        print("AI ERROR:", e)
        bot.reply_to(
            message,
            "⚠️ এই মুহূর্তে AI উত্তর দিতে পারছে না। একটু পরে আবার চেষ্টা করুন।"
        )


print("AHEAD AI is running...")
bot.infinity_polling()
