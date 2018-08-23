"""
Tests for Example App 5.
"""

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from . import models


class ToppingModelTests(TestCase):
    """
    Tests to ensure valid Topping Model creation/logic.
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
        # First, we get all toppings on the indicated pizza, which should just be "Test Topping" in this instance.
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


class ToppingViewTests(TestCase):
    """
    Tests to ensure valid Topping model views.
    """
    @classmethod
    def setUpTestData(cls):
        cls.topping = models.Topping.objects.create(name='Test Topping')

    def test_index(self):
        response = self.client.get(reverse('example_app_5:index'))
        self.assertEqual(response.status_code, 200)

    def test_overview(self):
        response = self.client.get(reverse('example_app_5:topping_overview'))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(reverse('example_app_5:topping_detail', kwargs={
            'pk': self.topping.pk,
        }))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.get(reverse('example_app_5:topping_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_edit(self):
        response = self.client.get(reverse('example_app_5:topping_edit', kwargs={
            'pk': self.topping.pk,
        }))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)


class PizzaViewTests(TestCase):
    """
    Tests to ensure valid Topping model views.
    """
    @classmethod
    def setUpTestData(cls):
        cls.pizza = models.Pizza.objects.create(name='Test Pizza')

    def test_index(self):
        response = self.client.get(reverse('example_app_5:index'))
        self.assertEqual(response.status_code, 200)

    def test_overview(self):
        response = self.client.get(reverse('example_app_5:pizza_overview'))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(reverse('example_app_5:pizza_detail', kwargs={
            'pk': self.pizza.pk,
        }))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.get(reverse('example_app_5:pizza_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_edit(self):
        response = self.client.get(reverse('example_app_5:pizza_edit', kwargs={
            'pk': self.pizza.pk,
        }))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
