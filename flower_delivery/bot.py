import logging
import os
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters
from config import TELEGRAM_BOT_TOKEN
from asgiref.sync import sync_to_async

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower_delivery.settings')
django.setup()

from orders.models import Order, OrderItem
from catalog.models import Flower
from accounts.models import User

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Команда /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Привет! Я бот для заказа цветов. Используй команду /order, чтобы оформить заказ."
    )

# Команда /order
async def order(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Пожалуйста, введите ваш заказ в формате: 'Название цветка, количество, адрес доставки'."
    )

# Обработка текстовых сообщений (для получения заказа)
async def process_order(update: Update, context: CallbackContext):
    order_text = update.message.text
    user_id = update.message.from_user.id
    username = update.message.from_user.username

    try:
        # Парсинг заказа (пример: "Розы, 5, ул. Пушкина, д. 10")
        flower_name, quantity, address = order_text.split(', ')
        quantity = int(quantity)

        # Поиск цветка в базе данных
        flower = await sync_to_async(Flower.objects.get)(name=flower_name)

        # Поиск или создание пользователя
        user, created = await sync_to_async(User.objects.get_or_create)(
            username=username,
            defaults={'telegram_id': user_id}
        )

        # Создание заказа
        order = await sync_to_async(Order.objects.create)(
            user=user,
            status='P',  # Статус "В обработке"
            address=address
        )

        # Создание элемента заказа
        await sync_to_async(OrderItem.objects.create)(
            order=order,
            flower=flower,
            quantity=quantity
        )

        # Уведомление пользователя
        await update.message.reply_text(f"Ваш заказ принят: {flower_name} (x{quantity}), адрес: {address}")

    except Exception as e:
        # Обработка ошибок
        await update.message.reply_text(f"Ошибка при оформлении заказа: {str(e)}")

# Команда /status
async def status(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id

    try:
        # Поиск пользователя
        user = await sync_to_async(User.objects.get)(telegram_id=user_id)

        # Поиск последнего заказа
        order = await sync_to_async(Order.objects.filter(user=user).latest)('created_at')
        await update.message.reply_text(f"Статус вашего заказа №{order.id}: {order.get_status_display()}")

    except User.DoesNotExist:
        await update.message.reply_text("Вы еще не оформляли заказов.")
    except Order.DoesNotExist:
        await update.message.reply_text("У вас нет заказов.")

# Запуск бота
def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("order", order))
    application.add_handler(CommandHandler("status", status))

    # Регистрация обработчика текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_order))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()