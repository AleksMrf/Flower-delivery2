import unittest
from unittest.mock import patch, MagicMock
from bot import start, order, process_order, status

class TestBot(unittest.TestCase):
    # Тест команды /start
    @patch('telegram.Update')
    @patch('telegram.ext.CallbackContext')
    async def test_start(self, mock_update, mock_context):
        mock_update.message = MagicMock()
        mock_update.message.reply_text = MagicMock()

        await start(mock_update, mock_context)
        mock_update.message.reply_text.assert_called_with(
            "Привет! Я бот для заказа цветов. Используй команду /order, чтобы оформить заказ."
        )

    # Тест команды /order
    @patch('telegram.Update')
    @patch('telegram.ext.CallbackContext')
    async def test_order(self, mock_update, mock_context):
        mock_update.message = MagicMock()
        mock_update.message.reply_text = MagicMock()

        await order(mock_update, mock_context)
        mock_update.message.reply_text.assert_called_with(
            "Пожалуйста, введите ваш заказ в формате: 'Название цветка, количество, адрес доставки'."
        )

    # Тест обработки текстового сообщения
    @patch('telegram.Update')
    @patch('telegram.ext.CallbackContext')
    async def test_process_order(self, mock_update, mock_context):
        mock_update.message = MagicMock()
        mock_update.message.text = "Розы, 5, ул. Пушкина, д. 10"
        mock_update.message.reply_text = MagicMock()

        await process_order(mock_update, mock_context)
        mock_update.message.reply_text.assert_called_with(
            "Ваш заказ принят: Розы, 5, ул. Пушкина, д. 10"
        )

    # Тест команды /status
    @patch('telegram.Update')
    @patch('telegram.ext.CallbackContext')
    async def test_status(self, mock_update, mock_context):
        mock_update.message = MagicMock()
        mock_update.message.reply_text = MagicMock()

        await status(mock_update, mock_context)
        mock_update.message.reply_text.assert_called_with(
            "Статус вашего заказа: Доставка запланирована на 15:00."
        )

if __name__ == '__main__':
    unittest.main()