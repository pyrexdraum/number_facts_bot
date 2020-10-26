# standard library
import os
import requests
import time

# third-party library
import telegram
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')


def get_number_fact():
    return requests.get('http://numbersapi.com/random').text


def send_message(message):
    bot = telegram.Bot(TELEGRAM_TOKEN)
    return bot.send_message(chat_id=CHAT_ID, text=message)


def main():
    while True:
        try:
            send_message(get_number_fact())
            time.sleep(300)
        except Exception as e:
            print(f'Something happened: {e}')
            time.sleep(5)
            continue


if __name__ == '__main__':
    main()
