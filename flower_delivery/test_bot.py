import unittest
from unittest.mock import AsyncMock, patch, MagicMock
from telegram import Update, Message, User as TelegramUser
from telegram.ext import CallbackContext
from bot import start, order  # Импортируем только рабочие функции
from accounts.models import User  # Исправлено с accaunts на accounts
from orders.models import Order  # Импортируем модель Order для исключения
from catalog.models import Flower  # Импортируем модель Flower для исключения


class TestBotCommands(unittest.IsolatedAsyncioTestCase):
    @patch('bot.Update')
    @patch('bot.CallbackContext')
    async def test_start_command(self, mock_context, mock_update):
        mock_message = AsyncMock(Message)
        mock_update.message = mock_message

        await start(mock_update, mock_context)

        mock_message.reply_text.assert_called_once_with(
            "Привет! Я бот для заказа цветов. Используй команду /order, чтобы оформить заказ."
        )

    @patch('bot.Update')
    @patch('bot.CallbackContext')
    async def test_order_command(self, mock_context, mock_update):
        mock_message = AsyncMock(Message)
        mock_update.message = mock_message

        await order(mock_update, mock_context)

        mock_message.reply_text.assert_called_once_with(
            "Пожалуйста, введите ваш заказ в формате: 'Название цветка, количество, адрес доставки'."
        )


if __name__ == '__main__':
    unittest.main()