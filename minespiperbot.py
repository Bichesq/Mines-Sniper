from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.effective_user.first_name
    await update.message.reply_text(f"Hello {username}! Welcome to Mines Siper bot. \nNow we just have to figure out the algorithm to strategise playing Mines.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Here are the commands you can use: \n/start, \n/help")


if __name__ == "__main__":
    app = ApplicationBuilder().token("8526525399:AAEG60TT31QLBJfadxNJ8kRnfpvNw6m7LLs").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()
