import asyncio
import re
from aiogram import Bot, Dispatcher, types, Router, F, html
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.filters import Command, CommandObject
from flask import current_app, session
from config import config
from src.repository import user_rep

router = Router()

user = {}


@router.message(Command(commands=["start"]))
async def process_start_command(message: types.Message):
    """
    Handler will forward to the sender invitation message
    """
    msg = text(bold(f"Hello, {message.from_user.full_name}!"),
               f"Please input next data:",
               '/username', '/email', '/birth', '/registry', sep='\n')
    await message.answer(msg)


# @router.message(Command(commands=["start"]))
# async def cmd_start(message: types.Message):
#     kb = [
#         [types.KeyboardButton(text="Username")],
#         [types.KeyboardButton(text="Email")],
#         [types.KeyboardButton(text="Birth")]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
#     msg = f"Hello, {message.from_user.full_name}\!\n" \
#           f"Please choose data for registry:"
#     await message.answer(msg, reply_markup=keyboard)


@router.message(Command(commands=["help"]))
async def process_help_command(message: types.Message):
    """
    Handler will forward to the sender help message
    """
    msg = text(bold('Use next commands:'),
               '/username', '/email', '/birth', '/registry', sep='\n')
    await message.answer(msg)


@router.message(Command(commands=["username"]))
async def process_username_command(message: types.Message,
                                command: CommandObject):
    """
    Handler will save username in the global var user or return error message
    """
    if command.args:
        user['username'] = command.args
        await message.answer(f"Your username is "
                             f"{bold(user['username'])}")
    else:
        await message.answer("Please input your name after the command "
                             "/username\!")


@router.message(Command(commands=["email"]))
async def process_email_command(message: types.Message,
                                command: CommandObject):
    """
    Handler will save email in the global var user or return error message
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if command.args:
        if re.match(email_pattern, command.args):
            user['email'] = command.args
            await message.answer(f"Your email is {bold(user['email'])}")
        else:
            await message.answer("Email does not correct\!")
    else:
        await message.answer("Please input your email after the command "
                         "/email\!")


@router.message(Command(commands=["birth"]))
async def process_birth_command(message: types.Message,
                                command: CommandObject):
    """
    Handler will save birthday in the global var user or return error message
    """
    date_pattern = r'\b\d{1,2}-\d{1,2}-\d{4}\b'
    if command.args:
        if re.match(date_pattern, command.args):
            user['birth'] = command.args
            await message.answer(f"Your birthday is {bold(user['birth'])}")
        else:
            await message.answer("Birthday format does not correct\!")
    else:
        await message.answer("Please input your birthday after the command "
                         "/birth in format day\-month\-year\!")


@router.message(Command(commands=["registry"]))
async def process_registry_command(message: types.Message):
    """
    Handler will create new record in the database with info from global var
    user using CRUD operation and put username to the current session
    """
    new_user = user_rep.create_user(user.get('username'),
                                    user.get('email'),
                                    '123456')
    session['user'] = {'email': new_user.email, 'id': new_user.id}
    await message.answer(f"User {new_user.username} added to database")


@router.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward received message back to the sender
    By default, message handler will handle all message types
    (like text, photo, sticker and etc.)
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try\!")


async def main() -> None:
    bot = Bot(token=config.TOKEN, parse_mode="MarkdownV2")
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
