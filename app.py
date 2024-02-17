import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather
TOKEN = '6106990052:AAE3lgYrCSvTlvbqVgr-h7nqIIEhPcwWjek'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi sir")

def PerformUserCommand(text: str) -> str:
    if text == "hi":
        return "Hi too"
def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update: {update} caused an error which is : {context.error}")
def main():
    print("Your bot has been started")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    print("Polling...")
    app.run_polling(poll_interval=3)
    
if __name__ == '__main__':
    main()
