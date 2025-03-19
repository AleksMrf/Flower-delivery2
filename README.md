# Flower Delivery Project

Проект для заказа доставки цветов через веб-сайт и Telegram бота.

## Описание проекта

Проект включает:
- Веб-сайт для заказа цветов с возможностью регистрации, авторизации и просмотра истории заказов.
- Telegram бота для оформления заказов и получения уведомлений о статусе заказа.

## Основные функции

### Веб-сайт
- Регистрация и авторизация пользователей.
- Просмотр каталога цветов.
- Оформление заказов.
- Просмотр истории заказов.

### Telegram бот
- Оформление заказов через бота.
- Уведомления о статусе заказа.

## Технологии

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **База данных**: SQLite (или PostgreSQL для production)
- **Telegram бот**: `python-telegram-bot`

## Установка и настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/AlexMrf/Flower-delivery2.git
cd Flower-delivery2
2. Создание виртуального окружения
Для Windows:

bash
Copy
python -m venv venv
venv\Scripts\activate
Для macOS/Linux:

bash
Copy
python3 -m venv venv
source venv/bin/activate
3. Установка зависимостей
bash
Copy
pip install -r requirements.txt
4. Настройка базы данных
Примените миграции:

bash
Copy
python manage.py migrate
Создайте суперпользователя:

bash
Copy
python manage.py createsuperuser
5. Настройка Telegram бота
Создайте бота через BotFather и получите токен.

Создайте файл config.py в корне проекта и добавьте токен:

python
Copy
TELEGRAM_BOT_TOKEN = 'ВАШ_ТОКЕН_БОТА'
6. Запуск проекта
Запустите сервер Django:

bash
Copy
pyt
hon manage.py runserver
Запустите Telegram бота:

bash
Copy
python bot.py
Использование
Веб-сайт
Перейдите по адресу: http://127.0.0.1:8000/

Зарегистрируйтесь или войдите в систему.

Просмотрите каталог цветов и оформите заказ.

Telegram бот
Найдите вашего бота в Telegram.

Используйте команды:

/start — начать работу с ботом.

/order — оформить заказ.

/status — узнать статус заказа.

Тестирование
Для запуска тестов выполните:

bash
Copy
python manage.py test
Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.

Авторы
Ваше имя

Copy

---

### Как использовать `README.md`

1. **Заполните информацию**:
   - Замените `ваш-username` на ваш GitHub username.
   - Укажите реальный токен бота в `config.py`.
   - Добавьте имена авторов и ссылки на их профили.

2. **Добавьте файл в репозиторий**:
   - Сохраните файл в корневой директории вашего проекта.
   - Загрузите его в репозиторий на GitHub.

3. **Обновляйте файл**:
   - Если вы добавляете новые функции или изменяете проект, обновляйте `README.md`.

---

### Пример структуры репозитория с `README.md`
Flower-delivery2/
├── flower_delivery/
├── accounts/
├── catalog/
├── orders/
├── templates/
├── static/
├── bot.py
├── config.py
├── manage.py
├── requirements.txt
├── README.md # Файл с описанием проекта
└── LICENSE # Файл с лицензией (опционально)

Copy

---

Если у вас возникнут вопросы или потребуется помощь, пишите! 😊
 
