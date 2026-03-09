import shutil
from pathlib import Path
import click


PATH_APS = "bot/apps/"
PATH_SYSYEMCTL = "/etc/systemd/system/"


IMPORT_ROUTER = "from bot.apps.{name}.handlers import router as {name}_router"
INCLUDE_ROUTER = "dp.include_router({name}_router)"


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name', type=str)
def add_app(name:str):
    path = Path(PATH_APS + name)
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
    path = Path(PATH_APS + name)
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


@cli.command()
def install():
    name_project = str(Path(__file__).resolve().parent.name)
    path_bot = Path(PATH_SYSYEMCTL + name_project + "_bot" + ".service" )
    path_fast_api = Path(PATH_SYSYEMCTL + name_project + "_fast_api" + ".service" )

    
    with open("templates/project_bot.service.txt","r") as project_bot:
        project_bot_text = project_bot.read()
    with open("templates/project_fast_api.service.txt","r") as project_fast_api:
        project_fast_api_text = project_fast_api.read()
    
    path_bot.write_text(project_bot_text.format(name_project=name_project))
    path_fast_api.write_text(project_fast_api_text.format(name_project=name_project))
    
    click.echo("Установка systemctl выполнена")


@cli.command()
def uninstall():
    name_project = str(Path(__file__).resolve().parent.name)
    path_bot = Path(PATH_SYSYEMCTL + name_project + "_bot" + ".service" )
    path_fast_api = Path(PATH_SYSYEMCTL + name_project + "_fast_api" + ".service" )
    if not path_bot.exists():
        click.echo(f"Файл {path_bot} ненайден")
    else:    
        shutil.rmtree(path_bot)

    if not path_fast_api.exists():
        click.echo(f"Файл {path_fast_api} ненайден")
        return
    else:
        shutil.rmtree(path_fast_api)

    click.echo("Удаление выполнено")


if __name__ == '__main__':
    cli()
