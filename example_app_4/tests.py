"""
Tests for Example App 4.
"""


from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from . import models


class AddressModelTests(TestCase):
    """
    Tests to ensure valid Address Model creation/logic.
    """
    def setUp(self):
        self.test_topping = models.Topping.objects.create(name='Test Topping')

    def test_model_creation(self):
        self.assertEqual(self.test_topping.name, 'Test Topping')

    def test_string_representation(self):
        self.assertEqual(str(self.test_topping), self.test_topping.name)

    def test_plural_representation(self):
        self.assertEqual(str(self.test_topping._meta.verbose_name), 'Topping')
        self.assertEqual(str(self.test_topping._meta.verbose_name_plural), 'Toppings')

    def test_unique(self):
        models.Topping.objects.create(name='Test Topping 2')
        models.Topping.objects.create(name='Test Topping 3')
        with self.assertRaises(ValidationError):
            models.Topping.objects.create(name='Test Topping 3')


class PizzaModelTests(TestCase):
    """
    Tests to ensure valid Pizza Model creation/logic.
    """
    @classmethod
    def setUpTestData(cls):
        cls.topping = models.Topping.objects.create(name='Test Topping')

    def setUp(self):
        self.test_pizza = models.Pizza.objects.create(name='Test Pizza')
        models.PizzaToppingRelationship.objects.create(
            pizza=self.test_pizza,
            topping=self.topping,
        )
        # These are just standard model queries using the above Many-to-Many relationship.
        # First, we get all doppings on the indicated pizza, which should just be "Test Topping" in this instance.
        # Then, we get all pizzas which use the indicated topping, which should just be "Test Pizza".
        self.toppings_on_pizza = self.test_pizza.toppings.all()
        self.pizzas_with_topping = self.topping.pizza_set.all() # This is the reverse query, hence the "_set".

    def test_model_creation(self):
        self.assertEqual(self.test_pizza.name, 'Test Pizza')
        self.assertEqual(self.test_pizza.price, 9.25)
        # Here, we test the Many-to-Many relationship through both the standard and reverse querysets.
        self.assertEqual(self.toppings_on_pizza[0], self.topping)
        self.assertEqual(self.pizzas_with_topping[0], self.test_pizza)

    def test_string_representation(self):
        self.assertEqual(str(self.test_pizza), self.test_pizza.name + ': ' + str(list(self.toppings_on_pizza)))

    def test_plural_representation(self):
        self.assertEqual(str(self.test_pizza._meta.verbose_name), 'Pizza')
        self.assertEqual(str(self.test_pizza._meta.verbose_name_plural), 'Pizzas')

    def test_price(self):
        # Test with no toppings.
        cheese_pizza = models.Pizza.objects.create()
        self.assertEqual(cheese_pizza.price, 8)

        # Test with two toppings.
        two_topping_pizza = models.Pizza.objects.create()
        second_topping = models.Topping.objects.create(name='Topping 2')
        models.PizzaToppingRelationship.objects.create(
            pizza=two_topping_pizza,
            topping=self.topping,
        )
        self.assertEqual(two_topping_pizza.price, 9.25)
        models.PizzaToppingRelationship.objects.create(
            pizza=two_topping_pizza,
            topping=second_topping,
        )
        self.assertEqual(two_topping_pizza.price, 10.50)

        # Test with extra topping.
        extra_topping_pizza = models.Pizza.objects.create()
        models.PizzaToppingRelationship.objects.create(
            pizza=extra_topping_pizza,
            topping=self.topping,
            extra=True,
        )
        self.assertEqual(extra_topping_pizza.price, 9.75)
