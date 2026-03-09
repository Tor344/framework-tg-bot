import os
import shutil
import pathlib
from pathlib import Path
import click
import subprocess

PATH_APS = "bot/apps/"

IMPORT_ROUTER = "from bot.apps.{name}.handlers import router as {name}_router"
INCLUDE_ROUTER = "dp.include_router({name}_router)"


@click.group()
def cli():
    pass


@cli.command()
@click.option('--token', help='Имя пользователя')
def start(token):
    env_file = "config/.env"

    # Читаем существующие переменные
    env_vars = {}
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    env_vars[key] = value

    # Обновляем токен
    env_vars['BOT_TOKEN'] = f'"{token}"'

    # Записываем все обратно
    with open(env_file, 'w') as f:
        for key, value in env_vars.items():
            f.write(f'{key}={value}\n')

    print(f"✅ Токен обновлен в {env_file}")

    venv_python = os.path.join(".venv", "bin", "python")
    venv_uvicorn = os.path.join(".venv", "bin", "uvicorn")

    # Запуск обоих процессов в фоне
    process1 = subprocess.Popen([venv_python, "main.py"])
    process2 = subprocess.Popen([venv_uvicorn, "admin.app:app", "--host", "0.0.0.0", "--port", "8000"])

    # Ожидание завершения обоих процессов (опционально)
    process1.wait()
    process2.wait()


@cli.command()
@click.argument('name', type=str)
def add_app(name:str):
    path = pathlib.Path(PATH_APS + name)
    if path.exists():
        click.echo("Файл уже существует")
        return
    path.mkdir(parents=True, exist_ok=True)

    with open("templates/hendlers.txt","r") as hendlers_templates:
        hendler_text = hendlers_templates.read()
    with open("templates/keyboards.txt","r") as keyboards_templates:
        keyboards = keyboards_templates.read()
    with open("templates/state_fms.txt","r") as state_fms_templates:
        state_fms = state_fms_templates.read()
        
    Path(path / "handlers.py").write_text(hendler_text.format(name=name))
    Path(path / "keyboards.py").write_text(keyboards.format(name=name))
    Path(path / "state_fms.py").write_text(state_fms.format(name_capitalize=name.capitalize(),name=name))

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
