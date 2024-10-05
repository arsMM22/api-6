import requests
import telegram
import random
import os
from dotenv import load_dotenv


def get_comic_num():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    all_number_comics = response.json()["num"]
    return all_number_comics


def get_comic_parametr(number):
    url = f"https://xkcd.com/{number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comic = response.json()
    alt = comic["alt"]
    image = comic["img"]
    name = comic["title"]
    return alt, image, name


def download_comic(image, filename):
    response = requests.get(image)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def upload_comic(tg_token, filename, tg_chat_id, alt):
    bot = telegram.Bot(token=tg_token)
    with open(filename, "rb") as f:
        bot.send_photo(chat_id=tg_chat_id, photo=f, caption=alt)


def main():
    load_dotenv()
    tg_chat_id = os.environ['TG_CHAT_ID']
    tg_token = os.environ['TELEGRAM_TOKEN']
    try:
        total_num_of_comics = get_num_comics()
        random_number = random.randint(1,total_num_of_comics)
        alt, image, name = get_parametr_comics(random_number)
        filename = f"{name}.png"
        download_comics(image, filename)
        upload_comics(tg_token, filename, tg_chat_id, alt)
    finally:
        os.remove(filename)


if __name__ == "__main__":
    main()
