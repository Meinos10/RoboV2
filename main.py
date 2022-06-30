from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
from config import *


Bot = Client("Button", api_id=api_id, api_hash=api_hash, bot_token=token)

with Bot:
	print("Bot çalışıyor!")
	while True:
		Bot.send_message(ids, text="**`Kanal Adı: Robobase V.I.P\nAksiyon: Sinyal paylaşıldı`**",
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👉Tek tıkla sinyale katıl👈", url="t.me/robobase_bot?start=true")
					],
					[
						InlineKeyboardButton("🤖Otomatik Al-Sat’ı Etkinleştir🤖", url="t.me/robobase_bot?start=buton")
					]
				]
			)
		)
		time.sleep(sure)