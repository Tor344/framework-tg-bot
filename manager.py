import shutil
import pathlib
from pathlib import Path
import click

PATH_APS = "bot/apps/"

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
