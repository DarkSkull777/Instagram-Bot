#MIT License

#Copyright (c) 2021 subinps

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from config import Config
import asyncio
import sys
import os

USER=Config.USER
OWNER=Config.OWNER
HOME_TEXT=Config.HOME_TEXT
HOME_TEXT_OWNER=Config.HOME_TEXT_OWNER
HELP=Config.HELP


@Client.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
	if str(cmd.from_user.id) != OWNER:	
		await cmd.reply_text(
			HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id, USER, USER, USER, OWNER), 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Creator", url='https://t.me/xskull7'),
						InlineKeyboardButton("🤖Bot lain", url="https://t.me/botdimasdoang")
					],
                    [
                        InlineKeyboardButton("🔗Website", url="https://darkskull7.my.to"),
						InlineKeyboardButton("🧩Blog", url="https://darkskull7.blogspot.com")
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯Gmn Caranya??", callback_data="help#subin"),
						InlineKeyboardButton("⚙️Channel", url="https://t.me/botdimasdoang")

                    ]
					
				]
			)
		)
	else:
		await cmd.reply_text(
			HOME_TEXT_OWNER.format(cmd.from_user.first_name, cmd.from_user.id), 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Creator", url='https://t.me/xskull7'),
						InlineKeyboardButton("🤖Bot lain", url="https://t.me/botdimasdoang"),
					],
                    [
                        InlineKeyboardButton("🔗Website", url="https://darkskull7.my.to")
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯Gmn Caranya??", callback_data="help#subin"),
						InlineKeyboardButton("⚙️Channel", url="https://t.me/botdimasdoang")

                    ]
					
				]
			)
		)


@Client.on_message(filters.command("help") & filters.private)
async def help(bot, cmd):
	await cmd.reply_text(
		HELP,
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton("👨🏼‍💻Creator", url='https://t.me/xskull7'),
					InlineKeyboardButton("🤖Bot lain", url="https://t.me/botdimasdoang"),
					InlineKeyboardButton("⚙️Channel", url="https://t.me/botdimasdoang")
					
				],
				[
					InlineKeyboardButton("🔗Website", url="https://darkskull7.my.to"),
					InlineKeyboardButton("🧩Blog", url="https://darkskull7.blogspot.com")
				]
			]
			)
		)

@Client.on_message(filters.command("restart") & filters.private)
async def stop(bot, cmd):
	if str(cmd.from_user.id) != OWNER:	
		await cmd.reply_text(
			HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id, USER, USER, USER, OWNER), 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Creator", url='https://t.me/xskull7'),
						InlineKeyboardButton("🤖Bot lain", url="https://t.me/botdimasdoang")	
					],
                    [
                        InlineKeyboardButton("🔗Website", url="https://#MIT License")

#Copyright (c) 2021 subinps

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from config import Config
from utils import *
import os
from instaloader import Profile
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong

HELP=Config.HELP
session=f"./{USER}"

STATUS=Config.STATUS

insta = Config.L

@Client.on_callback_query()
async def cb_handler(bot: Client, query: CallbackQuery):
    cmd, username = query.data.split("#")
    profile = Profile.from_username(insta.context, username)
    mediacount = profile.mediacount
    name = profile.full_name
    profilepic = profile.profile_pic_url
    igtvcount = profile.igtvcount
    followers = profile.followers
    folllowing = profile.followees
    
    if query.data.startswith("help"):
        await query.message.edit_text(
            HELP,
            reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton("👨🏼‍💻Creator", url='https://t.me/xskull7'),
					InlineKeyboardButton("🤖Bot lain", url="https://t.me/botdimasdoang/5"),
                    InlineKeyboardButton("⚙️Channel", url="https://t.me/botdimasdoang" )
				],
				[
					InlineKeyboardButton("🔗Website", url="https://darkskull7.my.to"),
					InlineKeyboardButton("🧩Blog", url="https://darkskull7.blogspot.com")
				]
			]
			)
		)
    
    
    elif query.data.startswith("ppic"):
        profile = Profile.from_username(insta.context, username)
        profilepichd = profile.profile_pic_url
        await query.answer()
        await bot.send_document(chat_id=query.from_user.id, document=profilepichd, file_name=f"{username}.jpg", force_document=True)
    
    
   
    elif query.data.startswith("post"):
        await query.message.delete()
        await bot.send_message(
            query.from_user.id,
            f"Jenis posting apa yang ingin Anda unduh??.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Photos", callback_data=f"photos#{username}"),
                        InlineKeyboardButton("Videos", callback_data=f"video#{username}")
                    ]
                ]
            )
        )
    

    

    elif query.data.startswith("photo"):
        if mediacount==0:
            await query.edit_message_text("Tidak ada posting oleh pengguna")
            return
        m= await query.edit_message_text("Mulai Mengunduh..\n mungkin memerlukan waktu tergantung pada jumlah Posting.")      
        dir=f"{query.from_user.id}/{username}"
        command = [
            "instaloader",
            "--no-metadata-json",
            "--no-compress-json",
            "--no-profile-pic",
            "--no-videos",
            "--no-captions",
            "--no-video-thumbnails",
            "--login", USER,
            "-f", session,
            "--dirname-pattern", dir,
            "--", username
            ]
        await download_insta(command, m, dir)
        chat_id=query.from_user.id
        await upload(m, bot, chat_id, dir)
    


    elif query.data.startswith("video"):
        if mediacount==0:
            await query.edit_message_text("Tidak ada postingan berdasarkan penggunaanr")
            return
        m= await query.edit_message_text("Mulai Mengunduh..\nIni mungkin memakan waktu lebih lama Tergantung pada jumlah posting.")    
        dir=f"{query.from_user.id}/{username}"
        command = [
            "instaloader",
            "--no-metadata-json",
            "--no-compress-json",
            "--no-profile-pic",
            "--no-pictures",
            "--no-captions",
            "--no-video-thumbnails",
            "--login", USER,
            "-f", session,
            "--dirname-pattern", dir,
            "--", username
            ]
        await download_insta(command, m, dir)
        chat_id=query.from_user.id
        await upload(m, bot, chat_id, dir)

    elif query.data.startswith("igtv"):
        await query.message.delete()
        await bot.send_message(
            query.from_user.id,
            f"Apakah Anda Ingin mengunduh semua posting IGTV??\nAda {igtvcount} Post.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Yes", callback_data=f"yesigtv#{username}"),
                        InlineKeyboardButton("No", callback_data=f"no#{username}")
                    ]
                ]
            )
        )
    elif query.data.startswith("yesigtv"):
        if igtvcount==0:
            await query.edit_message_text("Tidak ada postingan IGTV oleh pengguna")
            return
        m= await query.edit_message_text("Mulai Mengunduh..\nIni mungkin memakan waktu lebih lama Tergantung pada jumlah posting.")
        dir=f"{query.from_user.id}/{username}"

        command = [
            "instaloader",
            "--no-metadata-json",
            "--no-compress-json",
            "--no-profile-pic",
            "--no-posts",
            "--igtv",
            "--no-captions",
            "--no-video-thumbnails",
            "--login", USER,
            "-f", session,
            "--dirname-pattern", dir,
            "--", username
            ]
        await download_insta(command, m, dir)
        chat_id=query.from_user.id
        await upload(m, bot, chat_id, dir)



    elif query.data.startswith("followers"):
        await query.message.delete()
        chat_id=query.from_user.id
        m=await bot.send_message(chat_id, f"Mengambil Daftar Pengikut {name}")
        f = profile.get_followers()
        followers=f"**Daftar Pengikut untuk {name}**\n\n"
        for p in f:
            followers += f"\n[{p.username}](www.instagram.com/{p.username})"
        try:
            await m.delete()
            await bot.send_message(chat_id=chat_id, text=followers)
        except MessageTooLong:
            followers=f"**Followers List for {name}**\n\n"
            f = profile.get_followers()
            for p in f:
                followers += f"\nName: {p.username} :     Link ke profil:www.instagram.com/{p.username}"
            text_file = open(f"{username}'s followers.txt", "w")
            text_file.write(followers)
            text_file.close()
            await bot.send_document(chat_id=chat_id, document=f"./{username}'s followers.txt", caption=f"{name}'s followers\n\nA Project By [XTZ_Bots](https://t.me/subin_works)")
            os.remove(f"./{username}'s followers.txt")
    



    
    elif query.data.startswith("followees"):
        await query.message.delete()
        chat_id=query.from_user.id
        m=await bot.send_message(chat_id, f"Mengambil Pengikut dari {name}")
        
        f = profile.get_followees()
        followees=f"**Daftar Pengikut untuk {name}**\n\n"
        for p in f:
            followees += f"\n[{p.username}](www.instagram.com/{p.username})"
        try:
            await m.delete()
            await bot.send_message(chat_id=chat_id, text=followees)
        except MessageTooLong:
            followees=f"**Followees List for {name}**\n\n"
            f = profile.get_followees()
            for p in f:
                followees += f"\nNama: {p.username} :     Link ke Profil: www.instagram.com/{p.username}"
            text_file = open(f"{username}'s followees.txt", "w")
            text_file.write(followees)
            text_file.close()
            await bot.send_document(chat_id=chat_id, document=f"./{username}'s followees.txt", caption=f"{name}'s followees\n\nA Project By [XTZ_Bots](https://t.me/subin_works)")
            os.remove(f"./{username}'s followees.txt")





    elif query.data.startswith("no"):
        await query.message.delete()
    


    else:
        dir=f"{query.from_user.id}/{username}"
        chat_id=query.from_user.id   
        await query.message.delete()
        m= await bot.send_message(chat_id, "Mulai Mengunduh..\nIni mungkin memakan waktu lebih lama Tergantung pada jumlah posting.") 
        cmd, username = query.data.split("#")   
        if cmd == "feed":
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-profile-pic",
                "--no-posts",
                "--no-captions",
                "--no-video-thumbnails",
                "--login", USER,
                "--sessionfile", session,
                "--dirname-pattern", dir,
                ":feed"
                ]
            await download_insta(command, m, dir)
        elif cmd=="saved":
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-profile-pic",
                "--no-posts",
                "--no-captions",
                "--no-video-thumbnails",
                "--login", USER,
                "-f", session,
                "--dirname-pattern", dir,
                ":saved"
                ]
            await download_insta(command, m, dir)
        elif cmd=="tagged":
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-profile-pic",
                "--no-posts",
                "--tagged",
                "--no-captions",
                "--no-video-thumbnails",
                "--login", USER,
                "-f", session,
                "--dirname-pattern", dir,
                "--", username
                ]
            await download_insta(command, m, dir)
        elif cmd=="stories":
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-profile-pic",
                "--no-posts",
                "--stories",
                "--no-captions",
                "--no-video-thumbnails",
                "--login", USER,
                "-f", session,
                "--dirname-pattern", dir,
                "--", username
                ]
            await download_insta(command, m, dir)
        elif cmd=="fstories":
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-profile-pic",
                "--no-captions",
                "--no-posts",
                "--no-video-thumbnails",
                "--login", USER,
                "-f", session,
                "--dirname-pattern", dir,
                ":stories"
                ]
            await download_insta(command, m, dir)
        elif cmd=="highlights":
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-profile-pic",
                "--no-posts",
                "--highlights",
                "--no-captions",
                "--no-video-thumbnails",
                "--login", USER,
                "-f", session,
                "--dirname-pattern", dir,
                "--", username
                ]
            await download_insta(command, m, dir)
        await upload(m, bot, chat_id, dir)
"),
						InlineKeyboardButton("🧩Blog", url="https://darkskull7.blogspot.com)
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯Gmn Caranya??", callback_data="help#subin"),
						InlineKeyboardButton("⚙️Channel", url="https://t.me/botdimasdoang")

                    ]
					
				]
			)
		)
		return
	msg = await bot.send_message(
		text="Memulai ulang bot kamu..",
		chat_id=cmd.from_user.id
		)
	await asyncio.sleep(2)
	await msg.edit("Semua Proses Berhenti dan Mulai Ulang")
	os.execl(sys.executable, sys.executable, *sys.argv)