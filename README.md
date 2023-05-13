# Пульт охраны банка

Веб-сервис создан для контроля и мониторинга доступа сотрудников к хранилищу в банке

## active_passcards_view.py

Содержит в себе функцию `active_passcards_view`, принимающую `request` и возвращающая `active_passcards.html` страницу со всеми активными картами доступа.

## passcard_info_view.py

Содержит в себе функцию `passcard_info_view`, принимающую `request` и `passcode`, где `passcode` - это код пропуска. Скрипт возвращает историю посещений сотрудника с полями:

- Дату и время посещения;
- Продолжительность посещения;
- Подозрительность визита (True, если более часа).

## storage_information_view.py

Содержит в себе функцию `storage_information_view`, принимающую `request`. Возвращает всех сотрудников, которые в данный момент находятся в хранилище с полями:

- Имя посетителя;
- Время входа;
- Длительность пребывания;
- Подозрительность.

### Как установить

Для корректной работы программы вам необходимо создать файл .env и записать в него следующие переменные:

- HOST - Хост базы данных;
- PORT - Порт базы данных;
- NAME - Имя базы данных;
- USER - Логин от базы данных;
- PASSWORD - Пароль от базы данных;
- SECRET_KEY - Секретный ключ;
- LANGUAGE_CODE - язык;
- TIME_ZONE - часовой пояс;
- DEBUG - Режим отладки. По стандарту - True;
- ALLOWED_HOSTS - Допустимые хосты. По стандарту - *.

Пример .env:

-export HOST=checkpoint.devman.org;
-export PORT=5434;
-export NAME=checkpoint;
-export USER=guard;
-export PASSWORD=osim5;
-export SECRET_KEY=REPLACE_ME;
-export LANGUAGE_CODE=ru-ru;
-export TIME_ZONE=Europe/Moscow;
-export DEBUG=false;
-export ALLOWED_HOSTS=*.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для запуска программы необходимо выполнить команду:

```
python3 manage.py runserver 0.0.0.0:8000
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
