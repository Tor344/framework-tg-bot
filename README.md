# **framework-tg-bot**
![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/512px-Telegram_logo.svg.png)



## **framework-tg-bot** 
  Это фраемворк на основе библиотеке `aiogram3` с архитектурой модульного монолита

## **Стек технологий**
1. ```aiogram3``` 
2. ```tortoise```
3. ```docker```

## **Запуск сервиса** 
### Самостоятельная настройка
Создайте в config файл под названием `.env` и впишите `BOT_TOKEN="ваш токен"`
1. ```git clone https://github.com/Tor344/framework-tg-bot.git```
2. ```python -m venv venv```
3. ```source venv/bin/activate```
4. ```pip install -r requirements.txt```
5. ```python main.py```
### Запуск докер через докер 
1. ```docker build -t my-bot-framework .```
2. ```docker run -d --name my_bot_run -e BOT_TOKEN="ваш_токен_от_BotFather" my-bot-framework ```
