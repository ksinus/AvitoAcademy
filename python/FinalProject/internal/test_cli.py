from cli import order, menu
from click.testing import CliRunner
from pizza import Margherita, Pepperoni, Hawaiian
from logic import bake, to_delivery, pickup
from unittest.mock import patch
import random
import unittest
import decorators


class MyTestCase(unittest.TestCase):

    def test_dict(self) -> None:
        """Testing dict method from Pizza class"""
        hawaiian_dict = {'tomato sauce': 75, 'mozzarella': 8, 'pineapples': 2,
                         'chicken': 1}
        pepperoni_dict = {'tomato sauce': 75, 'mozzarella': 8, 'pepperoni': 10}
        margaherita = {'tomato sauce': 75, 'mozzarella': 8, 'tomatoes': 10}
        self.assertDictEqual(Hawaiian().dict(), hawaiian_dict)
        self.assertDictEqual(Pepperoni().dict(), pepperoni_dict)
        self.assertDictEqual(Margherita().dict(), margaherita)

    def test_equal_pizza(self) -> None:
        """Testing equal operator from Pizza class"""
        xlh = Hawaiian(size='XL')
        xlh2 = Hawaiian(size='XL')
        lh = Hawaiian(size='L')
        xlm = Margherita(size='XL')
        lm = Margherita(size='L')

        self.assertFalse(xlh == lh)
        self.assertFalse(xlh == xlm)
        self.assertFalse(lh == lm)
        self.assertTrue(xlh == xlh2)

    def test_menu(self):
        """Testing menu method"""
        runner = CliRunner()
        result = runner.invoke(menu)
        target_output = (
                "- Margherita🧀: tomato sauce, mozzarella, tomatoes\n" +
                "- Pepperoni🍕: tomato sauce, mozzarella, pepperoni\n" +
                "- Hawaiian🍍: tomato sauce, mozzarella, pineapples, chicken\n"
        )
        self.assertEqual(result.output, target_output)

    def test_order_delivery(self):
        with patch.object(decorators, "randint", return_value=0):
            runner = CliRunner()
            result = runner.invoke(order,
                                   ["margherita", "--delivery", "--size=XL"])
        target_output = '🍕\u200dПриготовили за 0с!\n🛵 Доставили за 0с!\n\n'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, target_output)

    def test_order_pickup(self):
        with patch.object(decorators, "randint", return_value=0):
            runner = CliRunner()
            result = runner.invoke(order,
                                   ["margherita", "--size=XL"])
        target_output = '🍕\u200dПриготовили за 0с!\n🏠 Забрали за 0с!\n\n'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, target_output)
