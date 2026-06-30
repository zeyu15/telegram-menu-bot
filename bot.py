from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🙎 客服人员", url="https://t.me/foreverbai"),
            InlineKeyboardButton("🤖 启动机器人", url="https://t.me/fovererlong/26")
        ],
        [
            InlineKeyboardButton("🤷‍♂️ 频道上粉", url="https://t.me/fovererlong/25"),
            InlineKeyboardButton("🌟 星星购买", url="https://t.me/fovererlong/24")
        ],
        [
            InlineKeyboardButton("💳 会员助力", url="https://t.me/fovererlong/22"),
            InlineKeyboardButton("🛒 代开会员", url="https://t.me/fovererlong/19")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📌 ForeverLong 官方菜单\n\n请选择需要的服务：",
        reply_markup=reply_markup
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
