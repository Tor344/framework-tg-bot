import shutil
import pathlib
from pathlib import Path
import click

PATH_APS = "bot/apps/"


HANDLERS = """from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("{name}"))
async def {name}(message: Message):
    await message.answer("{name}")
"""

KEYBOARD_HANDLERS = """from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

start_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="{name}",callback_data='{name}_inline_keyboard')]])

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text="{name}",callback_data='{name}_keyboard')]])
"""

STATE_FMS = """from aiogram.fsm.state import State,StatesGroup

class {name_capitalize}(StatesGroup):
    {name} = State()
    """
IMPORT_ROUTER = "from bot.apps.{name}.handlers import router as {name}_router"
INCLUDE_ROUTER = "dp.include_router({name}_router)"

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name', type=str)
def add_app(name:str):
    path = pathlib.Path(PATH_APS + name)
    if path.exists():
        click.echo("Файл уже существует")
        return
    path.mkdir(parents=True, exist_ok=True)

    Path(path / "handlers.py").write_text(HANDLERS.format(name=name))
    Path(path / "keyboards.py").write_text(KEYBOARD_HANDLERS.format(name=name))
    Path(path / "state_fms.py").write_text(STATE_FMS.format(name_capitalize=name.capitalize(),name=name))

    main_strings = Path("main.py").read_text(encoding='utf-8').splitlines()
    main_strings.insert(4, IMPORT_ROUTER.format(name=name))
    main_strings.insert(15,INCLUDE_ROUTER.format(name=name))

    Path("main.py").write_text('\n'.join(main_strings), encoding='utf-8')


@cli.command()
@click.argument('name', type=str)
def del_app(name:str):
    path = pathlib.Path(PATH_APS + name)
    if not path.exists():
        click.echo("Файл не найден")
        return
    shutil.rmtree(path)

    main_strings = Path("main.py").read_text(encoding='utf-8').splitlines()
    for i, line in enumerate(main_strings):
        if IMPORT_ROUTER.format(name=name) == line:
            del main_strings[i]
        if INCLUDE_ROUTER.format(name=name) == line:
            del main_strings[i]
            break


    Path("main.py").write_text('\n'.join(main_strings), encoding='utf-8')



if __name__ == '__main__':
    cli()
