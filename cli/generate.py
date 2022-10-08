import click
from pathlib import Path


@click.command()
@click.option('--name', '-n')
def generate(name: str):
    file_name = f'{name.lower()}.py'
    tools = Path(f"{str(Path('.').parent.absolute())}/tools/")
    new = Path(f'{tools}/{file_name}')

    if new.exists():
        click.echo(f'Template {file_name} already exists!')
        return

    with open(file=new, mode='w') as tool:
        tool.write(f'class {name.capitalize()}:\n\tpass\n')

    with open(Path(f'{tools}/__init__.py'), mode='a') as package:
        package.write(f'from .{name} import *\n')


if __name__ == '__main__':
    generate()
