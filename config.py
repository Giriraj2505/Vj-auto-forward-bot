from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "469e3f62b54f83f9839216aefab5136f")
      API_ID = int(getenv("API_ID", "13687927"))
      AS_COPY = True if getenv("AS_COPY") == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6856438628:AAHayttF5x7gXC2qTkZF_oqN2jP5UuRWwzc")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002061087529:-1002020998850").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
