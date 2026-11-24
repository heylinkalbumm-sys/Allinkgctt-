from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import yt_dlp
import os

TOKEN = os.environ.get("TOKEN", "9295567284:AAEoZgffKDCDiEfef6u0lkS4m0_5tnFE0Ds")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Kirim /dl + link TikTok\n\nContoh:\n/dl https://vt.tiktok.com/xxxx/")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 MENU BOT:\n\n/start - Mulai bot\n/dl + link - Download video TikTok\n/menu - Lihat menu ini\n\nContoh download:\n/dl https://vt.tiktok.com/xxxx/")

async def dl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Caranya: /dl + link\nContoh: /dl https://vt.tiktok.com/xxxx/")
        return
    
    url = context.args[0]
    await update.message.reply_text("Lagi download, tunggu ya... ⏳")
    
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'video_tiktok.mp4',
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        await update.message.reply_video(video=open('video_tiktok.mp4', 'rb'), caption="Nih videonya ✅")
        os.remove('video_tiktok.mp4')
        
    except Exception as e:
        await update.message.reply_text(f"Gagal download 😢\nCoba link lain.\nError: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("dl", dl))
    print("Bot jalan...")
    app.run_polling()
