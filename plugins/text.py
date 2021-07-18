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

import re
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import *
from instaloader import Profile

USER=Config.USER
OWNER=Config.OWNER
HOME_TEXT=Config.HOME_TEXT
HELP=Config.HELP
session=f"./{USER}"

STATUS=Config.STATUS

insta = Config.L


@Client.on_message(filters.command("account") & filters.private)
async def account(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, int(OWNER)), 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Creator", url='https://t.me/xskull7'),
						InlineKeyboardButton("🤖Bot lainnya", url="https://t.me/botdimasdoang"),
                        
					],
                    [
                        InlineKeyboardButton("🔗Website", url="https://darkskull7.my.to"),
						InlineKeyboardButton("🧩Blog", url="https://darkskull7.blogspot.com")
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯Bagaimana caranya?", callback_data="help#subin"),
                        InlineKeyboardButton("⚙️Channel", url="https://t.me/botdimasdoang")

                    ]
					
				]
			)
		)
        return
    if 1 in STATUS:
        m=await message.reply_text("Mendapatkan data Anda")
        try:
            profile = Profile.own_profile(insta.context)
            mediacount = profile.mediacount
            name = profile.full_name
            bio = profile.biography
            profilepic = profile.profile_pic_url
            username = profile.username
            igtvcount = profile.igtvcount
            followers = profile.followers
            following = profile.followees
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Unduh Foto Profil Saya", callback_data=f"ppic#{username}")
                        
                    ],
                    [
                        InlineKeyboardButton("Unduh Semua Postingan Saya", callback_data=f"post#{username}"),
                        InlineKeyboardButton("Unduh Semua Posting Bertag", callback_data=f"tagged#{username}")
                    ],
                    [
                        InlineKeyboardButton("Unduh Postingan di Umpan Saya", callback_data=f"feed#{username}"),
                        InlineKeyboardButton("Unduh Postingan Ku Yg Tersimpan", callback_data=f"saved#{username}")
                    ],
                    [
                        InlineKeyboardButton("Unduh Postingan IGTV Saya", callback_data=f"igtv#{username}"),
                        InlineKeyboardButton("Unduh Sorotan Saya", callback_data=f"highlights#{username}")
                    ],
                    [
                        InlineKeyboardButton("Unduh Cerita Saya ", callback_data=f"stories#{username}"),
                        InlineKeyboardButton("Unduh Cerita Pengikut Saya", callback_data=f"fstories#{username}")
                    ],
                    [
                        InlineKeyboardButton("Dapatkan Daftar Pengikut Saya", callback_data=f"followers#{username}"),
                        InlineKeyboardButton("Dapatkan Daftar Pengikut Saya", callback_data=f"followees#{username}")
                    ]

                ]
                )
            await m.delete()
            await bot.send_photo(
                        chat_id=message.from_user.id,
                        photo=profilepic,
                        caption=f"🏷 **Name**: {name}\n🔖 **Username**: {profile.username}\n📝**Bio**: {bio}\n📍 **Account Type**: {acc_type(profile.is_private)}\n🏭 **Is Business Account?**: {yes_or_no(profile.is_business_account)}\n👥 **Total Followers**: {followers}\n👥 **Total Following**: {following}\n📸 **Total Posts**: {mediacount}\n📺 **IGTV Videos**: {igtvcount}",
                        reply_markup=reply_markup
                    )
        except Exception as e:
            await m.edit(e)

    else:
        await message.reply_text("Anda harus login terlebih dahulu dengan /login")


@Client.on_message(filters.text & filters.private & filters.incoming)
async def _insta_post_batch(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, int(OWNER)),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Creator", url='https://t.me/xskull7'),
						InlineKeyboardButton("🤖Bot lainnya", url="https://t.me/botdimasdoang"),
                        
					],
                    [
                        InlineKeyboardButton("🔗Website", url="https://darkskull7.my.to"),
						InlineKeyboardButton("🧩Blog", url="https://darkskull7.blogspot.com")
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯Bagaimana caranya?", callback_data="help#subin"),
                        InlineKeyboardButton("⚙️Channel", url="https://t.me/botdimasdoang")

                    ]
					
				]
			)
		)
        return
    if 1 not in STATUS:
        await message.reply_text("Anda Harus Masuk Dulu /login ")
        return
    m = await message.reply_text("Mengambil data dari Instagram🔗")
    chat_id= message.from_user.id
    username=message.text
    if "https://instagram.com/stories/" in username:
        await m.edit("Cerita dari tautan belum didukung🥴\n\nAnda dapat mengunduh cerita dari Nama Pengguna.")
        return

    link = r'^https:\/\/www\.instagram\.com\/(p|tv|reel)\/([A-Za-z0-9\-_]*)'
    result = re.search(link, username)
    
    if result:
        Post_type = {
            'p': 'POST',
            'tv': 'IGTV',
            'reel': 'REELS'
        }
        supported = Post_type.get(result.group(1))
        if not supported:
            await m.edit('Format tidak didukung')
            return
        sent = await m.edit(f'`Mengambil Konten yang {supported} dari Instagram.`')
        shortcode = result.group(2)
        try:
            userid=str(message.from_user.id)
            dir=f"{userid}/{shortcode}"
            chat_id=message.from_user.id
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-captions",
                "--no-video-thumbnails",
                "--login", USER,
                "-f", session,
                "--dirname-pattern", dir,
                "--", f"-{shortcode}"
                ]
            await download_insta(command, sent, dir)
            await upload(sent, bot, chat_id, dir)
        except Exception as e:
            print(e)
            await bot.send_message(chat_id=message.from_user.id, text=e)
            pass
    elif "https://" in username:
        await m.edit('Format tidak didukung')
        return

    else:
        await m.edit(f"Mengambil detail untuk <code>@{username}</code>")
        try:
            profile = Profile.from_username(insta.context, username)
            mediacount = profile.mediacount
            name = profile.full_name
            profilepic = profile.profile_pic_url
            igtvcount = profile.igtvcount
            bio = profile.biography
            followers = profile.followers
            following = profile.followees
            is_followed = yes_or_no(profile.followed_by_viewer) 
            is_following = yes_or_no(profile.follows_viewer)
            type = acc_type(profile.is_private)
            if type == "🔒Pribadi🔒" and is_followed == "No":
                print("reached")
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Unduh Foto Profil", callback_data=f"ppic#{username}"),
                        ]
                    ]
                )
            else:
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Foto Profil", callback_data=f"ppic#{username}")
                        ],
                        [
                            InlineKeyboardButton("Semua Posting", callback_data=f"post#{username}"),
                            InlineKeyboardButton("Semua Posting yang Ditandai", callback_data=f"tagged#{username}")
                        ],
                        [
                            InlineKeyboardButton("Semua IGTV", callback_data=f"igtv#{username}"),
                            InlineKeyboardButton("Cerita ", callback_data=f"stories#{username}"),
                            InlineKeyboardButton("Highlight", callback_data=f"highlights#{username}")
                        ],
                        [
                            InlineKeyboardButton(f"{name}'s Followers", callback_data=f"followers#{username}"),
                            InlineKeyboardButton(f"{name}'s Followees", callback_data=f"followees#{username}")
                        ]
                    ]
                )
            await m.delete()
            try:
                await bot.send_photo(
                    chat_id=chat_id,
                    photo=profilepic,
                    caption=f"🏷 **Name**: {name}\n🔖 **Username**: {profile.username}\n📝 **Bio**: {bio}\n📍 **Account Type**: {acc_type(profile.is_private)}\n🏭 **Is Business Account?**: {yes_or_no(profile.is_business_account)}\n👥 **Total Followers**: {followers}\n👥 **Total Following**: {following}\n**👤 Is {name} Following You?**: {is_following}\n**👤 Is You Following {name} **: {is_followed}\n📸 **Total Posts**: {mediacount}\n📺 **IGTV Videos**: {igtvcount}",
                    reply_markup=reply_markup
                    )
            except Exception as e:
                print(e)
                await bot.send_message(chat_id, e)
        except Exception as e:
            print(e)
            await m.edit(e)
            pass#MIT License

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

import re
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import *
from instaloader import Profile

USER=Config.USER
OWNER=Config.OWNER
HOME_TEXT=Config.HOME_TEXT
HELP=Config.HELP
session=f"./{USER}"

STATUS=Config.STATUS

insta = Config.L


@Client.on_message(filters.command("account") & filters.private)
async def account(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, int(OWNER)), 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Creator", url='https://t.me/xskull7'),
						InlineKeyboardButton("🤖Bot lainnya", url="https://t.me/botdimasdoang"),
                        
					],
                    [
                        InlineKeyboardButton("🔗Website", url="https://darkskull7.my.to"),
						InlineKeyboardButton("🧩Blog", url="https://darkskull7.blogspot.com")
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯Bagaimana caranya?", callback_data="help#subin"),
                        InlineKeyboardButton("⚙️Channel", url="https://t.me/botdimasdoang")

                    ]
					
				]
			)
		)
        return
    if 1 in STATUS:
        m=await message.reply_text("Mendapatkan data Anda")
        try:
            profile = Profile.own_profile(insta.context)
            mediacount = profile.mediacount
            name = profile.full_name
            bio = profile.biography
            profilepic = profile.profile_pic_url
            username = profile.username
            igtvcount = profile.igtvcount
            followers = profile.followers
            following = profile.followees
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Unduh Foto Profil Saya", callback_data=f"ppic#{username}")
                        
                    ],
                    [
                        InlineKeyboardButton("Unduh Semua Postingan Saya", callback_data=f"post#{username}"),
                        InlineKeyboardButton("Unduh Semua Posting Bertag", callback_data=f"tagged#{username}")
                    ],
                    [
                        InlineKeyboardButton("Unduh Postingan di Umpan Saya", callback_data=f"feed#{username}"),
                        InlineKeyboardButton("Unduh Postingan Ku Yg Tersimpan", callback_data=f"saved#{username}")
                    ],
                    [
                        InlineKeyboardButton("Unduh Postingan IGTV Saya", callback_data=f"igtv#{username}"),
                        InlineKeyboardButton("Unduh Sorotan Saya", callback_data=f"highlights#{username}")
                    ],
                    [
                        InlineKeyboardButton("Unduh Cerita Saya ", callback_data=f"stories#{username}"),
                        InlineKeyboardButton("Unduh Cerita Pengikut Saya", callback_data=f"fstories#{username}")
                    ],
                    [
                        InlineKeyboardButton("Dapatkan Daftar Pengikut Saya", callback_data=f"followers#{username}"),
                        InlineKeyboardButton("Dapatkan Daftar Pengikut Saya", callback_data=f"followees#{username}")
                    ]

                ]
                )
            await m.delete()
            await bot.send_photo(
                        chat_id=message.from_user.id,
                        photo=profilepic,
                        caption=f"🏷 **Name**: {name}\n🔖 **Username**: {profile.username}\n📝**Bio**: {bio}\n📍 **Account Type**: {acc_type(profile.is_private)}\n🏭 **Is Business Account?**: {yes_or_no(profile.is_business_account)}\n👥 **Total Followers**: {followers}\n👥 **Total Following**: {following}\n📸 **Total Posts**: {mediacount}\n📺 **IGTV Videos**: {igtvcount}",
                        reply_markup=reply_markup
                    )
        except Exception as e:
            await m.edit(e)

    else:
        await message.reply_text("Anda harus login terlebih dahulu dengan /login")


@Client.on_message(filters.text & filters.private & filters.incoming)
async def _insta_post_batch(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, int(OWNER)),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Creator", url='https://t.me/xskull7'),
						InlineKeyboardButton("🤖Bot lainnya", url="https://t.me/botdimasdoang"),
                        
					],
                    [
                        InlineKeyboardButton("🔗Website", url="https://darkskull7.my.to"),
						InlineKeyboardButton("🧩Blog", url="https://darkskull7.blogspot.com")
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯Bagaimana caranya?", callback_data="help#subin"),
                        InlineKeyboardButton("⚙️Channel", url="https://t.me/botdimasdoang")

                    ]
					
				]
			)
		)
        return
    if 1 not in STATUS:
        await message.reply_text("Anda Harus Masuk Dulu /login ")
        return
    m = await message.reply_text("Mengambil data dari Instagram🔗")
    chat_id= message.from_user.id
    username=message.text
    if "https://instagram.com/stories/" in username:
        await m.edit("Cerita dari tautan belum didukung🥴\n\nAnda dapat mengunduh cerita dari Nama Pengguna.")
        return

    link = r'^https:\/\/www\.instagram\.com\/(p|tv|reel)\/([A-Za-z0-9\-_]*)'
    result = re.search(link, username)
    
    if result:
        Post_type = {
            'p': 'POST',
            'tv': 'IGTV',
            'reel': 'REELS'
        }
        supported = Post_type.get(result.group(1))
        if not supported:
            await m.edit('Format tidak didukung')
            return
        sent = await m.edit(f'`Mengambil Konten yang {supported} dari Instagram.`')
        shortcode = result.group(2)
        try:
            userid=str(message.from_user.id)
            dir=f"{userid}/{shortcode}"
            chat_id=message.from_user.id
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-captions",
                "--no-video-thumbnails",
                "--login", USER,
                "-f", session,
                "--dirname-pattern", dir,
                "--", f"-{shortcode}"
                ]
            await download_insta(command, sent, dir)
            await upload(sent, bot, chat_id, dir)
        except Exception as e:
            print(e)
            await bot.send_message(chat_id=message.from_user.id, text=e)
            pass
    elif "https://" in username:
        await m.edit('Format tidak didukung')
        return

    else:
        await m.edit(f"Mengambil detail untuk <code>@{username}</code>")
        try:
            profile = Profile.from_username(insta.context, username)
            mediacount = profile.mediacount
            name = profile.full_name
            profilepic = profile.profile_pic_url
            igtvcount = profile.igtvcount
            bio = profile.biography
            followers = profile.followers
            following = profile.followees
            is_followed = yes_or_no(profile.followed_by_viewer) 
            is_following = yes_or_no(profile.follows_viewer)
            type = acc_type(profile.is_private)
            if type == "🔒Pribadi🔒" and is_followed == "No":
                print("reached")
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Unduh Foto Profil", callback_data=f"ppic#{username}"),
                        ]
                    ]
                )
            else:
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Foto Profil", callback_data=f"ppic#{username}")
                        ],
                        [
                            InlineKeyboardButton("Semua Posting", callback_data=f"post#{username}"),
                            InlineKeyboardButton("Semua Posting yang Ditandai", callback_data=f"tagged#{username}")
                        ],
                        [
                            InlineKeyboardButton("Semua IGTV", callback_data=f"igtv#{username}"),
                            InlineKeyboardButton("Cerita ", callback_data=f"stories#{username}"),
                            InlineKeyboardButton("Highlight", callback_data=f"highlights#{username}")
                        ],
                        [
                            InlineKeyboardButton(f"{name}'s Followers", callback_data=f"followers#{username}"),
                            InlineKeyboardButton(f"{name}'s Followees", callback_data=f"followees#{username}")
                        ]
                    ]
                )
            await m.delete()
            try:
                await bot.send_photo(
                    chat_id=chat_id,
                    photo=profilepic,
                    caption=f"🏷 **Name**: {name}\n🔖 **Username**: {profile.username}\n📝 **Bio**: {bio}\n📍 **Account Type**: {acc_type(profile.is_private)}\n🏭 **Is Business Account?**: {yes_or_no(profile.is_business_account)}\n👥 **Total Followers**: {followers}\n👥 **Total Following**: {following}\n**👤 Is {name} Following You?**: {is_following}\n**👤 Is You Following {name} **: {is_followed}\n📸 **Total Posts**: {mediacount}\n📺 **IGTV Videos**: {igtvcount}",
                    reply_markup=reply_markup
                    )
            except Exception as e:
                print(e)
                await bot.send_message(chat_id, e)
        except Exception as e:
            print(e)
            await m.edit(e)
            pass
shall