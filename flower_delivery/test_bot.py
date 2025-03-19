import unittest
from unittest.mock import AsyncMock, patch, MagicMock
from telegram import Update, Message, User, Chat
from telegram.ext import CallbackContext
import bot
from config import TELEGRAM_BOT_TOKEN

class TestBot(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.application = bot.ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
        self.update = AsyncMock(spec=Update)
        self.context = AsyncMock(spec=CallbackContext)

    async def test_start_command(self):
        self.update.message = AsyncMock(spec=Message)
        self.update.message.reply_text = AsyncMock()

        await bot.start(self.update, self.context)

        self.update.message.reply_text.assert_called_with(
            "Привет! Я бот для заказа цветов. Используй команду /order, чтобы оформить заказ."
        )

    async def test_order_command(self):
        self.update.message = AsyncMock(spec=Message)
        self.update.message.reply_text = AsyncMock()

        await bot.order(self.update, self.context)

        self.update.message.reply_text.assert_called_with(
            "Пожалуйста, введите ваш заказ в формате: 'Название цветка, количество, адрес доставки'."
        )

    async def test_process_order(self):
        self.update.message = AsyncMock(spec=Message)
        self.update.message.text = "Розы, 5, Криптон"
        self.update.message.from_user = AsyncMock(spec=User)
        self.update.message.from_user.id = 123
        self.update.message.from_user.username = "test_user"
        self.update.message.reply_text = AsyncMock()

        # Моки для Django ORM
        mock_flower = MagicMock()
        mock_flower.name = "Розы"
        mock_user = MagicMock()
        mock_user.telegram_id = 123
        mock_order = MagicMock()
        mock_order.id = 1
        mock_order.status = 'P'
        mock_order.address = "Криптон"

        # Используем MagicMock вместо AsyncMock для синхронных методов Django ORM
        with patch('bot.Flower.objects.get', new_callable=MagicMock) as mock_flower_get, \
                patch('bot.User.objects.get_or_create', new_callable=MagicMock) as mock_user_get_or_create, \
                patch('bot.Order.objects.create', new_callable=MagicMock) as mock_order_create, \
                patch('bot.OrderItem.objects.create', new_callable=MagicMock) as mock_order_item_create:
            mock_flower_get.return_value = mock_flower
            mock_user_get_or_create.return_value = (mock_user, True)
            mock_order_create.return_value = mock_order
            mock_order_item_create.return_value = MagicMock()

            await bot.process_order(self.update, self.context)

    async def test_status_command(self):
        self.update.message = AsyncMock(spec=Message)
        self.update.message.from_user = AsyncMock(spec=User)
        self.update.message.from_user.id = 123
        self.update.message.reply_text = AsyncMock()

        # Моки для Django ORM
        mock_user = MagicMock()
        mock_user.telegram_id = 123
        mock_order = MagicMock()
        mock_order.id = 1
        mock_order.status = 'P'
        mock_order.get_status_display = MagicMock(return_value="В обработке")

        # Используем синхронные моки для Django ORM
        with patch('bot.User.objects.get', new_callable=MagicMock) as mock_user_get, \
                patch('bot.Order.objects.filter', new_callable=MagicMock) as mock_order_filter:
            mock_user_get.return_value = mock_user
            mock_order_filter.return_value.latest.return_value = mock_order

            await bot.status(self.update, self.context)

            self.update.message.reply_text.assert_called_with(
                "Статус вашего заказа №1: В обработке"
            )

if __name__ == '__main__':
    unittest.main()