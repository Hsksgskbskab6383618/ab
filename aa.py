from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests as r



async def st(u,c):
  u.reply_text("Hello")
  

async def ur(u,c):
  
  a = r.get('https://ulvis.net/api.php?url='+u.message.text)
  if "Error" in a.text:
    u.reply_text("Enter Valid Url")
  else:
    u.reply_text(a.text)



app = ApplicationBuilder().token("YOUR TOKEN HERE").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
