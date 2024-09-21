# Загрузка комиксов в telegram
## Описание
Создан для загрузки комиксов в telegram.
# Установка
Скачайте необходимые файлы, затем используйте `pip` ( или `pip3`, если есть конфликт с Python2 ) для установки зависимостей и установить зависимости. Установите зависимости командой:
```
pip install -r requirements.txt
```
# Пример запуска скрипта
Для запуска у вас должен установлен Python3.
Для публикации комикса надо написать:
```
python main.py
```
# Переменые окружения
 Часть настроек проекта берется из переменных окружения. Чтоб определить переменые окружения необходимо создать файл `.env` рядом с `main.py` и запишите данные туда в таком формате: переменная = значение.
 Пример содержания файла `.env`:
 ```
 TG_TOKEN = "bot_Token"
 TG_CHAT_ID = "@название вашего телеграмм канала"
 ```
  # Цель проекта
 Проект был написан в образовательных целях