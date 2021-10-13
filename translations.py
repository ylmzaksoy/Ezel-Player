from config import ASSISTANT_NAME
from helpers.bot_utils import BOT_NAME, USERNAME


START_TEXT = f"👋🏻 **Merhaba**, \n\n**{BOT_NAME}** \nTelegram Gruplarının Sesli Sohbetinde Canlıları, Radyoları, YouTube Videolarını ve Telegram Ses / Video Dosyalarını Yayınlayabilirim. Arkadaşlarınızla Grup Video Oynatıcısının Sinematik Görünümünün Tadını Çıkaralım 😉! \n\n**Teşekkürler❤️ By @TheEzelBoss!** 👑"
HELP_TEXT = f"""
🛠-- **Bot Kurulumu**:--

\u2022 Grubunuzda Sesli Sohbet Başlatın!
\u2022 Beni (@{USERNAME}) Ve Asistanım (@{ASSISTANT_NAME}) Grubunuza Ekleyin !
\u2022 Bana (@{USERNAME}) Ve Asistanım (@{ASSISTANT_NAME}) Adminlik Ver !

⚔️-- **Available Commands**:--

\u2022 `/play` - Ses Akışı Başlatır
\u2022 `/stream` - Video Akışı Başlatır
\u2022 `/pause` - Geçerli Akışı Duraklatır
\u2022 `/resume` - Duraklatılmış Akışı Sürdürür
\u2022 `/endstream` - Yayını Bitir
\u2022 `/restart` - Botu Yeniden Başlat
"""
ABOUT_TEXT = f"💡-- **Information**:-- \n\nThis bot is created for streaming videos in telegram group video chats using several methods from WebRTC. Powered by pytgcalls the async client API for the Telegram Group Calls and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots. \n\n**This bot licensed under GNU-GPL 3.0 License!**"
