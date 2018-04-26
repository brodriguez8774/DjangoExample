"""
Models for Example App 3.
"""


from django.db import models


MAX_LENGTH = 200


class Address(models.Model):
    """
    An address model for a customer.
    """
    # Model Fields.
    address = models.CharField(max_length=MAX_LENGTH)
    # Self-setting/Non-user-editable fields.
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return '{0}'.format(self.address)

    def clean(self, *args, **kwargs):
        """
        Custom cleaning implementation. Includes validation, setting fields, etc.
        """
        # Nothing to put here for the moment.

    def save(self, *args, **kwargs):
        """
        Modify model save behavior.
        """
        # Save model.
        self.full_clean()
        super(Address, self).save(*args, **kwargs)


class Customer(models.Model):
    """
    A customer model.
    """
    # Relational fields.
    address = models.ForeignKey('Address', on_delete=models.CASCADE, blank=True, null=True)
    # Model Fields.
    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)
    # Self-setting/Non-user-editable fields.
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return '{0} {1}, {2}'.format(self.first_name, self.last_name, self.address)

    def clean(self, *args, **kwargs):
        """
        Custom cleaning implementation. Includes validation, setting fields, etc.
        """
        # Nothing to put here for the moment.

    def save(self, *args, **kwargs):
        """
        Modify model save behavior.
        """
        # Save model.
        self.full_clean()
        super(Customer, self).save(*args, **kwargs)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
