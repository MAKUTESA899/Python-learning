from instabot import Bot

# Initialize the bot
bot = Bot()

# Login to your Instagram account
username = 'your_username'
password = 'your_password'
bot.login(username=username, password=password)

# Hashtag to search for
hashtag = 'pythonprogramming'

# Get media from the hashtag
media = bot.get_hashtag_medias(hashtag)

# Like each media
for media_id in media:
    bot.like(media_id)

# Logout from the account
bot.logout()
