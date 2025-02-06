# Required Variables
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# API_ID: Your API ID from telegram.org.
API_ID = int(getenv("API_ID", ""))

# API_HASH: Your API Hash from telegram.org.
API_HASH = getenv("API_HASH", "")

# BOT_TOKEN: Get your bot token from @BotFather.
BOT_TOKEN = getenv("BOT_TOKEN", "")

# OWNER_ID: Use @missrose_bot to get your user ID by sending /info.
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))

# MONGO_DB: A MongoDB URL for storing session data (recommended for security).
MONGO_DB = getenv("MONGO_DB", "")

# LOG_GROUP: A group or channel where the bot logs messages. Forward a message to @userinfobot to get your channel/group ID.
LOG_GROUP = getenv("LOG_GROUP", "")

# CHANNEL_ID: The ID of the channel for forced subscription.
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))

# FREEMIUM_LIMIT: Default is 0. Set this to any value you want to allow free users to extract content. If set to 0, free users will not have access to any extraction features.
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))

# PREMIUM_LIMIT: Default is 500. This is the batch limit for premium users. You can customize this to allow premium users to process more links/files in one batch.
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))

# WEBSITE_URL: (Optional) This is the domain for your monetization short link service. Provide the shortener's domain name, for example: upshrink.com. Do not include www or https://. The default link shortener is already set.
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")

# AD_API: (Optional) The API key from your link shortener service (e.g., Upshrink, AdFly, etc.) to monetize links. Enter the API provided by your shortener.
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")

# STRING: (Optional) Add your premium account session string here to allow 4GB file uploads. This is optional and can be left empty if not used.
STRING = getenv("STRING", None)

# YT_COOKIES: Yt cookies for downloading yt videos
YT_COOKIES = getenv("YT_COOKIES", None)

# INSTA_COOKIES: If you want to enable instagram downloading fill cookiesn
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
