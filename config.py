from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 1545981
    API_HASH = "bd213c7f45c8d1490c4b4bdcf1e8c32c"
    # the name to display in your alive message
    ALIVE_NAME = "Amnap"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://amnap:T9p9Gk4u0MyoEovXPEFMhSGBHXZIRBQk@dpg-cb7ek9bvog4s8f204eag-a.singapore-postgres.render.com/catuserbot_4ter"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOGoBuzwVkageLqWxbBthDfHQH68jBVl_jNmzchAdEHdv1Ld0Sm-GvD8a_gsES9oRrPtz4uJmTk0eEbzKHv2uA1MLX1uZntOdxLuU7o0Z9HTM6kdKLu5PyjdTAzw-1M-UE0L3ZYA8XrjDIs0-Y-mV40tEOgD4WL6AvuBvdLP69asj7edQqsTngNkGp8FOJiWZoEt9LshfnVrf50vHk8MaapM_W_lXvAJOi16SX58Urs7C2wKZLObIu8GbhO6aiBi191nrLeGqI5IZE1ExTxaCT-j-_4cQil4WvdU_hrguOGho8iTeam_sg3GwHRFVb_RARZgYDPC2z7u2HxPz1PWaGkirUqM="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "1615021162:AAFB8TtIVL-iQRc5cdcySvZapI8b5wIbL90"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -100
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
