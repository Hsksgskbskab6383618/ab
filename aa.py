from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes,MessageHandler, filters
import requests as r
from flask import Flask
import threading




async def st(u,c):
    await u.message.reply_text("Hello")
  

async def ur(u,c):
  
    a = r.get('https://ulvis.net/api.php?url='+u.message.text)
    if "Error" in a.text:
      await u.message.reply_text("Enter Valid Url")
    else:
      await u.message.reply_text(a.text)



app = Application.builder().token("6361126109:AAEQlzSP16lM8GQdRclWYscLa8hBn1blvZ4").build()

app.add_handler(CommandHandler("start", st))
app.add_handler(MessageHandler(filters.TEXT,ur))






ap = Flask(__name__)

@ap.route('/')
def hm():
  return 'hi'





app.run_polling()
ap.run()














