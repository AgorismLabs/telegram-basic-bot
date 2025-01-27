import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: reply text generated by LLM here
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: link to connect wallet
    # TODO: reply text generated by LLM here
    await update.message.reply_text(f'Under construction {update.effective_user.first_name}')


async def do(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: reply text generated by LLM here
    await update.message.reply_text(f'Under construction {update.effective_user.first_name}')


async def dont(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: reply text generated by LLM here
    await update.message.reply_text(f'Under construction {update.effective_user.first_name}')


async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: reply text generated by LLM here
    await update.message.reply_text(f'Under construction {update.effective_user.first_name}')

async def help_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: reply text generated by LLM here
    await update.message.reply_text('\n'.join((
        'commands overview:',
        '',
        '/help - this',
        '/hello - greetings',
        '/connect - connect your wallet',
        '/do - request stuff',
        '/dont - second placeholder',
        '/bye - good bye and see you again!',
    )))

app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()

app.add_handler(CommandHandler("help", help_text))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("connect", connect))
app.add_handler(CommandHandler("do", do_stuff))
app.add_handler(CommandHandler("dont", do_not_do_stuff))
app.add_handler(CommandHandler("bye", bye))

app.run_polling()
