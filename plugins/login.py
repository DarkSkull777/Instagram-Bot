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
from utils import *
import os
from instaloader import Profile, TwoFactorAuthRequiredException, BadCredentialsException
from asyncio.exceptions import TimeoutError

USER=Config.USER
STATUS=Config.STATUS
OWNER=Config.OWNER
HOME_TEXT=Config.HOME_TEXT

insta = Config.L


@Client.on_message(filters.command("login") & filters.private)
async def login(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER), 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Creator", url='https://t.me/xskull7'),
						InlineKeyboardButton("🤖Bot lainnya", url="https://t.me/botdimasdoang")
					],
                    [
                        InlineKeyboardButton("🔗Website", url="https://darkskull7.my.to"),
						InlineKeyboardButton("🧩Blog", url="https://darkskull7.blogspot.com")
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯Bagaimana caranya?", callback_data="help#subin")

                    ]
					
				]
			)
		)
        return
    username=USER
    if 1 in STATUS:
        m=await bot.send_message(message.from_user.id, "Mengambil detail dari Instagram")
        profile = Profile.own_profile(insta.context)
        mediacount = profile.mediacount
        name = profile.full_name
        bio = profile.biography
        profilepic = profile.profile_pic_url
        igtvcount = profile.igtvcount
        followers = profile.followers
        following = profile.followees
        await m.delete()
        await bot.send_photo(
            chat_id=message.from_user.id,
            caption=f"Anda sudah Masuk sebagai {name}\n\n**Detail Akun Anda**\n\n🏷 **Name**: {name}\n🔖 **Username**: {profile.username}\n📝 **Bio**: {bio}\n📍 **Account Type**: {acc_type(profile.is_private)}\n🏭 **Is Business Account?**: {yes_or_no(profile.is_business_account)}\n👥 **Total Followers**: {followers}\n👥 **Total Following**: {following}\n📸 **Total Posts**: {mediacount}\n📺 **IGTV Videos**: {igtvcount}",
            photo=profilepic
            )
        return
    while True:
        try:
            password = await bot.ask(text = f"Helo {USER} Masukkan Kata Sandi Instagram Anda untuk masuk ke akun Anda 🙈", chat_id = message.from_user.id, filters=filters.text, timeout=30)
        except TimeoutError:
            await bot.send_message(message.from_user.id, "Error!!\n\nWaktu permintaan habis.\nMulai ulang dengan menggunakan /login")
            return
        passw=password.text
        break
    try:
        insta.login(username, passw)
        insta.save_session_to_file(filename=f"./{username}")
        f=await bot.send_document(
            chat_id=message.from_user.id,
            document=f"./{username}",
            file_name=str(message.from_user.id),
            caption="⚠️ TETAPKAN FILE SESI INI AMAN DAN JANGAN DIBAGIKAN DENGAN SIAPA PUN"
            )
        file_id=f.document.file_id
        await bot.send_message(message.from_user.id, f"Now go to [Heroku](https://dashboard.heroku.com/apps) and set Environment variable.\n\n\n**KEY**: <code>INSTA_SESSIONFILE_ID</code>\n\n**VALUE**: <code>{file_id}</code>\n\nIf you do not set this you may need to Login again When Heroku restarts.", disable_web_page_preview=True)
        STATUS.add(1)
        m=await bot.send_message(message.from_user.id, "Fetching details from Instagram")
        profile = Profile.from_username(insta.context, username)
        mediacount = profile.mediacount
        name = profile.full_name
        bio = profile.biography
        profilepic = profile.profile_pic_url
        igtvcount = profile.igtvcount
        followers = profile.followers
        following = profile.followees
        await m.delete()
        await bot.send_photo(
            chat_id=message.from_user.id,
            caption=f"🔓Berhasil Masuk sebagai {name}\n\n**Detail Akun Anda**\n\n🏷 **Name**: {name}\n🔖 **Username**: {profile.username}\n📝 **Bio**: {bio}\n📍 **Account Type**: {acc_type(profile.is_private)}\n🏭 **Is Business Account?**: {yes_or_no(profile.is_business_account)}\n👥 **Total Followers**: {followers}\n👥 **Total Following**: {following}\n📸 **Total Posts**: {mediacount}\n📺 **IGTV Videos**: {igtvcount}",
            photo=profilepic
            )
    except TwoFactorAuthRequiredException:
        while True:
            try:
                code = await bot.ask(text = "Oh!!\nAkun Instagram Anda mengaktifkan Otentikasi Dua Faktor🔐\n\nOTP telah dikirim ke ponsel Anda\nEnter the OTP", chat_id = message.from_user.id, filters=filters.text, timeout=30)
            except TimeoutError:
                await bot.send_message(message.from_user.id, "Error!!\n\nWaktu permintaan habis.\nMulai ulang dengan menggunakan /login")
                return
            codei=code.text
            try:
                codei=int(codei)
                break
            except:
                await bot.send_message(message.from_user.id, "OTP Should be Integer")
                continue
        try:
            insta.two_factor_login(codei)
            insta.save_session_to_file(filename=f"./{username}")
            f=await bot.send_document(
                chat_id=message.from_user.id,
                document=f"./{username}",
                file_name=str(message.from_user.id),
                caption="⚠️ KEEP THIS SESSION FILE SAFE AND DO NOT SHARE WITH ANYBODY"
                )
            file_id=f.document.file_id
            await bot.send_message(message.from_user.id, f"Now go to [Heroku](https://dashboard.heroku.com/apps) and set Environment variable.\n\n\n**KEY**: <code>INSTA_SESSIONFILE_ID</code>\n\n**VALUE**: <code>{file_id}</code>\n\nIf you do not set this you may need to Login again When Heroku restarts.", disable_web_page_preview=True)
            STATUS.add(1)
            m=await bot.send_message(message.from_user.id, "Fetching details from Instagram")
            profile = Profile.from_username(insta.context, username)
            mediacount = profile.mediacount
            name = profile.full_name
            bio = profile.biography
            profilepic = profile.profile_pic_url
            igtvcount = profile.igtvcount
            followers = profile.followers
            following = profile.followees
            await m.delete()
            await bot.send_photo(
                chat_id=message.from_user.id,
                caption=f"🔓Succesfully Logged In as {name}\n\n**Your Account Details**\n\n🏷 **Name**: {name}\n🔖 **Username**: {profile.username}\n📝**Bio**: {bio}\n📍**Account Type**: {acc_type(profile.is_private)}\n🏭**Is Business Account?**: {yes_or_no(profile.is_business_account)}\n👥**Total Followers**: {followers}\n👥**Total Following**: {following}\n📸**Total Posts**: {mediacount}\n📺**IGTV Videos**: {igtvcount}",
                photo=profilepic
                )
        except BadCredentialsException:
            await bot.send_message(message.from_user.id, "Wrong Credentials\n\n/login again")
            pass
        except Exception as e:
            await bot.send_message(message.from_user.id, f"{e}\nTry /login again")
        print("Logged in")
    except Exception as e:
        await bot.send_message(message.from_user.id, f"{e}\nCoba lagi atau Laporkan Masalah ini ke [Creator](tg://user?id=626664225)")

@Client.on_message(filters.command("logout") & filters.private)
async def logout(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER), 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Creator", url='https://t.me/xskull7'),
						InlineKeyboardButton("🤖Bot lainnya", url="https://t.me/botdimasdoang")
					],
                    [
                        InlineKeyboardButton("🔗Website", url="https://darkskull7.my.to"),
						InlineKeyboardButton("🧩Blog", url="https://darkskull7.blogspot.com")
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯Bagaimana caranya?", callback_data="help#subin")

                    ]
					
				]
			)
		)
        return
    if 1 in STATUS:
        await message.reply_text("Berhasil Logout")
        STATUS.remove(1)
        os.remove(f"./{USER}")
    else:
        await message.reply_text("Anda belum Masuk\n pakai /login terlebih dahulu")
