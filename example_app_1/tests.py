"""
Tests for Example App 1.
"""

from django.test import TestCase
from django.urls import reverse

from . import models


class CategoryModelTests(TestCase):
    """
    Tests to ensure valid Category Model creation/logic.

    Note that testing the model like this is mostly redundant unless you have specific model logic to test.
    Otherwise, you're essentially testing that the Django framework does what it promises to do.
    This can still be useful sometimes, such as to test string representations to make sure you didn't make silly typos.
    """
    def setUp(self):
        self.test_category = models.Category.objects.create(title='Test Category')

    def test_model_creation(self):
        self.assertEqual(self.test_category.title, 'Test Category')


class ViewTests(TestCase):
    """
    Tests to ensure valid Example App 1 views.
    """
    @classmethod
    def setUpTestData(cls):
        cls.category = models.Category.objects.create(title='Category')

    def test_index(self):
        response = self.client.get(reverse('example_app_1:index'))
        self.assertEqual(response.status_code, 200)

    def test_category_detail(self):
        response = self.client.get(reverse('example_app_1:category_detail', kwargs={
            'category_id': self.category.id
        }))
        self.assertEqual(response.status_code, 200)

    def test_category_create(self):
        response = self.client.get(reverse('example_app_1:category_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_category_edit(self):
        response = self.client.get(reverse('example_app_1:category_edit', kwargs={
            'category_id': self.category.id
        }))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
