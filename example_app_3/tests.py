"""
Tests for Example App 3.
"""

from django.test import TestCase
from django.urls import reverse

from . import models


#region Model Tests

class AddressModelTests(TestCase):
    """
    Tests to ensure valid Address Model creation/logic.
    """
    def setUp(self):
        self.test_address = models.Address.objects.create(address='1234 Test Address')

    def test_model_creation(self):
        self.assertEqual(self.test_address.address, '1234 Test Address')

    def test_string_representation(self):
        self.assertEqual(str(self.test_address), self.test_address.address)

    def test_plural_representation(self):
        self.assertEqual(str(self.test_address._meta.verbose_name), 'Address')
        self.assertEqual(str(self.test_address._meta.verbose_name_plural), 'Addresses')


class CustomerModelTests(TestCase):
    """
    Tests to ensure valid Customer Model creation/logic.
    """
    @classmethod
    def setUpTestData(cls):
        cls.address = models.Address.objects.create(address='1234 Test Address')

    def setUp(self):
        self.test_customer = models.Customer.objects.create(
            first_name='Test First',
            last_name='Test Last',
            address = self.address,
        )

    def test_model_creation(self):
        self.assertEqual(self.test_customer.first_name, 'Test First')
        self.assertEqual(self.test_customer.last_name, 'Test Last')
        self.assertEqual(str(self.test_customer.address), '1234 Test Address')

    def test_string_representation(self):
        self.assertEqual(str(self.test_customer), self.test_customer.first_name + ' ' + self.test_customer.last_name +
                         ', ' + str(self.test_customer.address))

    def test_plural_representation(self):
        self.assertEqual(str(self.test_customer._meta.verbose_name), 'Customer')
        self.assertEqual(str(self.test_customer._meta.verbose_name_plural), 'Customers')

#endregion Model Tests



#region View Tests

class AddressViewTests(TestCase):
    """
    Tests to ensure valid Example App 3 views.
    """
    @classmethod
    def setUpTestData(cls):
        cls.address = models.Address.objects.create(address='1234 Test Address')

    def test_index(self):
        response = self.client.get(reverse('example_app_3:index'))
        self.assertEqual(response.status_code, 200)

    def test_address_overview(self):
        response = self.client.get(reverse('example_app_3:address_overview'))
        self.assertEqual(response.status_code, 200)

    def test_address_detail(self):
        response = self.client.get(reverse('example_app_3:address_detail', kwargs={
            'address_id': self.address.pk
        }))
        self.assertEqual(response.status_code, 200)

    def test_address_create(self):
        response = self.client.get(reverse('example_app_3:address_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_address_edit(self):
        response = self.client.get(reverse('example_app_3:address_edit', kwargs={
            'address_id': self.address.pk
        }))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)


class CustomerViewTests(TestCase):
    """
    Tests to ensure valid Example App 3 views.
    """
    @classmethod
    def setUpTestData(cls):
        cls.customer = models.Customer.objects.create(first_name='Test First', last_name='Test Last')

    def test_index(self):
        response = self.client.get(reverse('example_app_3:index'))
        self.assertEqual(response.status_code, 200)

    def test_customer_detail(self):
        response = self.client.get(reverse('example_app_3:customer_detail', kwargs={
            'customer_id': self.customer.pk
        }))
        self.assertEqual(response.status_code, 200)

    def test_customer_create(self):
        response = self.client.get(reverse('example_app_3:customer_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_customer_edit(self):
        response = self.client.get(reverse('example_app_3:customer_edit', kwargs={
            'customer_id': self.customer.pk
        }))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

#endregion View Tests
