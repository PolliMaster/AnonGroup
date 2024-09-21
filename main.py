import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import asyncio

API_TOKEN = '7432672679:AAEGB-pO2w_xlWRFCiLBtm7WMlLtyv79dhY'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

INTERESTS = ["Мемы", "Игры", "Музыка", "Путешествия", "Аниме", "Фильмы", "Питомцы", "Книги", "Спорт", "Программирование", "Дорамы"]

waiting_users = {}
active_chats = {}

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    buttons = []
    for i in range(0, len(INTERESTS), 2):
        row = []
        row.append(InlineKeyboardButton(text=INTERESTS[i], callback_data=INTERESTS[i]))
        if i + 1 < len(INTERESTS):
            row.append(InlineKeyboardButton(text=INTERESTS[i + 1], callback_data=INTERESTS[i + 1]))
        buttons.append(row)

    buttons.append([InlineKeyboardButton(text="Завершить диалог", callback_data="end_chat")])
    buttons.append([InlineKeyboardButton(text="Сведения", callback_data="info")])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer("Привет! Выбери свои интересы, и мы найдем тебе собеседника:", reply_markup=keyboard)

@dp.callback_query()
async def process_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data

    if data in INTERESTS:
        if data in waiting_users and waiting_users[data] != user_id:
            other_user_id = waiting_users.pop(data)
            await bot.send_message(other_user_id, "Мы нашли тебе собеседника!")
            await bot.send_message(user_id, "Мы нашли тебе собеседника!")

            active_chats[user_id] = other_user_id
            active_chats[other_user_id] = user_id

            await bot.send_message(user_id, f"Чат по интересу: {data}. Начните общение.")
            await bot.send_message(other_user_id, f"Чат по интересу: {data}. Начните общение.")
        else:
            waiting_users[data] = user_id
            await bot.send_message(user_id, f"Ожидаем собеседника по интересу: {data}...")

    elif data == "end_chat":
        partner_id = active_chats.pop(user_id, None)
        if partner_id:
            
            buttons = []
            for i in range(0, len(INTERESTS), 2):
                row = []
                row.append(InlineKeyboardButton(text=INTERESTS[i], callback_data=INTERESTS[i]))
                if i + 1 < len(INTERESTS):
                    row.append(InlineKeyboardButton(text=INTERESTS[i + 1], callback_data=INTERESTS[i + 1]))
                buttons.append(row)

            buttons.append([InlineKeyboardButton(text="Сведения", callback_data="info")])

            keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
            
            active_chats.pop(partner_id, None)
            await bot.send_message(partner_id, "Ваш собеседник покинул чат.", reply_markup=keyboard)
            
        buttons = []
        for i in range(0, len(INTERESTS), 2):
            row = []
            row.append(InlineKeyboardButton(text=INTERESTS[i], callback_data=INTERESTS[i]))
            if i + 1 < len(INTERESTS):
                row.append(InlineKeyboardButton(text=INTERESTS[i + 1], callback_data=INTERESTS[i + 1]))
            buttons.append(row)
        buttons.append([InlineKeyboardButton(text="Сведения", callback_data="info")])

        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await bot.send_message(user_id, "Вы завершили диалог. Выберите интерес заново.", reply_markup=keyboard)


    elif data == "info":
        active_users_count = len(active_chats) // 2
        await bot.send_message(user_id, f"Количество действующих пользователей: {active_users_count}")

@dp.message(lambda message: message.from_user.id in active_chats)
async def relay_message(message: types.Message):
    user_id = message.from_user.id
    partner_id = active_chats.get(user_id)

    if partner_id:
        await bot.send_message(partner_id, message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



# Проблема бота в том что он отправляет inline кнопки при вызове команды "/start", 
# после выбора интереса он ждет собеседника , но перевыбор интереса не работает, 
# также после как пользователь найдет собеседника нужно возращаться к первому сообщению и выбрать
# завершение диалога, т.к Reply кнопки не работают, 
# а просто отправляют текст пользователю, также необходимо, чтобы при создании чата , 
# в reply появилась только 1 кнопка "Завершение диалога" по которой мы можем Покинуть чат и выбрать 
# другие интересы.

