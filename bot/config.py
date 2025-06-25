from bot.get_cfg import get_config

class Config(object):
    # You can keep this default
    SESSION_NAME = get_config("SESSION_NAME", "EncoderX") 
    # EncoderX_bot....
    # sucks Dude
    APP_ID = int(get_config("APP_ID", "20793620"))
    API_HASH = get_config("API_HASH", "a712d2b8486f26c4dee5127cc9ae0615")
    LOG_CHANNEL = get_config("LOG_CHANNEL", "logencoder")
    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None) # Without `@` LOL
    AUTH_USERS = [1047253913]
    USER_SESSION = get_config("USER_SESSION","BQAO83IAcjM8qkEXaikoZwkn8iWi94nr29TNTZpbjMI3KPlGAq-0CuA8idOxYur5HgYPIhMr4ayPr9_8Clj3Brk_ye-xq81RpnizkaLyHLGkh83tW3AmWy3Mc_GhuvyIUblf0yaK5Xti2GGT2KezRqKA408kKIUHacBqfY4TCMOeA85ve0bMR5vKHqD3-6wgBezxKnowXyF6KXXIxB4TQZP5PJh5OWp_yi_wX3e4gVnOWL2iE8LdI7UFKZ-0atI0gNGbi4Hbxg2GZgJMzMvJQkZMeifgj1R2UtZSRy0sp8uNl1sg8rccU1vbqvroFSACZB2EAAAAABAEDjEA")  

# array , simplest method was AUTH_USERS = [] ; AUTH_USERS.append(your telegram id) 🌹
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "8102040984:AAEQ9J8FFA_uneRT6cHbkoPMM7u5eItm-0I")
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "/app/downloads")
    # Telegram maximum file upload size
    BOT_USERNAME = get_config("BOT_USERNAME", "Encoder720pRBot")
    MAX_FILE_SIZE = 4194304000
    TG_MAX_FILE_SIZE = 4194304000
    FREE_USER_MAX_FILE_SIZE = 4194304000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://envs.sh/CQU.jpg")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "🟨")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "⬛")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
