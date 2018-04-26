"""
Tests for Example App 3.
"""


from django.test import TestCase

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



#endregion View Tests
