import click
from pizza import Margherita, Pepperoni, Hawaiian
from logic import bake, to_delivery, pickup


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery",
              default=False,
              help='Do you want delivery?',
              is_flag=True)
@click.option("--size",
              default="L",
              prompt='size',
              help='Choose pizza size',
              type=click.Choice(["L", "XL"], case_sensitive=False))
@click.argument("pizza",
                nargs=1,
                type=click.Choice(["Margherita", "Pepperoni", "Hawaiian"],
                                  case_sensitive=False))
def order(pizza: str, delivery: bool, size: str) -> None:
    """Returns the order infrormation and place an order"""
    pizza = pizza.lower().title()
    obj_pizza = eval(pizza)(size)
    click.echo(bake(obj_pizza),
               to_delivery(obj_pizza) if delivery else pickup(obj_pizza))


@cli.command()
def menu() -> None:
    """Returns a list of menu items"""
    for pizza in ["Margherita", "Pepperoni", "Hawaiian"]:
        pizza_object = eval(pizza)()
        ingredients = ", ".join(pizza_object.dict().keys())
        click.echo(f'- {pizza_object.name_}: {ingredients}')


if __name__ == "__main__":
    cli()
