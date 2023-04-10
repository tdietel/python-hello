import click

@click.command()
@click.option('--name', default='world', help='The person to greet.')
def hello(name):
    print(f"Hello, {name}!")