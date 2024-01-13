from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler, filters
import requests as r
from flask import Flask
import threading

def aaa():
  pass


def abx():
  async def st(u,c):
    u.reply_text("Hello")
  

  async def ur(u,c):
  
    a = r.get('https://ulvis.net/api.php?url='+u.message.text)
    if "Error" in a.text:
      u.reply_text("Enter Valid Url")
    else:
      u.reply_text(a.text)



  app = ApplicationBuilder().token("6361126109:AAFWJkbNucxUejdyxP3pt8Gn2hEncCcLjHI").build()

  app.add_handler(CommandHandler("start", st))
  app.add_handler(MessageHandler(filters.TEXT,ur))
  app.run_polling()


def aby():


  ap = Flask(__name__)

  @ap.route('/')
  def hm():
    return 'hi'



x = threading.Thread(target=abx)
y = threading.Thread(target=aby)


x.start()
y.start()

x.join()
y.join()
