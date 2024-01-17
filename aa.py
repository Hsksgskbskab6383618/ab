from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes,MessageHandler, filters
import requests as r
from flask import Flask
import threading
import asyncio
from asgiref.wsgi import WsgiToAsgi
import uvicorn


async def st(u,c):
    await u.message.reply_text("Hello")
  

async def ur(u,c):
  
    a = r.get('https://ulvis.net/api.php?url='+u.message.text)
    if "Error" in a.text:
      await u.message.reply_text("Enter Valid Url")
    else:
      await u.message.reply_text(a.text)



app = Application.builder().token("6361126109:AAHNbJyQT73COU0qJbUKXSce8nhtZyDnhzw").build()

app.add_handler(CommandHandler("start", st))
app.add_handler(MessageHandler(filters.TEXT,ur))






ap = Flask(__name__)

@ap.route('/')
def hm():
  return 'hi'

aaa = uvicorn.Server(uvicorn.Config(WsgiToAsgi(ap)))




async def main():
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await aaa.serve()
    await app.stop()
    









asyncio.run(main())






