import telegram


class BotTelegram(object):
    def __init__(self):
        self.bot = telegram.Bot("1961152091:AAEE_c0eGBDP-W7GjOwPa__TNmDAiEvcIDM")

    def send_message(self, text):
        self.bot.send_message(
            chat_id=-564615985,
            text=text,
            parse_mode=telegram.ParseMode.MARKDOWN
        )