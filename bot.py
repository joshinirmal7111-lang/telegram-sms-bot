import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("8704320688:AAHbHBciBJP503v31waZTLsGfAPoNGXQEb4")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
