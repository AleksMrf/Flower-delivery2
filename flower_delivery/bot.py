import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters
from config import TELEGRAM_BOT_TOKEN

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
    # Логика обработки заказа и сохранения в базу данных
    await update.message.reply_text(f"Ваш заказ принят: {order_text}")

# Команда /status
async def status(update: Update, context: CallbackContext):
    await update.message.reply_text("Статус вашего заказа: Доставка запланирована на 15:00.")

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