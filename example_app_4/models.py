"""
Models for Example App 4.
"""

from django.db import models


MAX_LENGTH = 200


class PizzaToppingRelationship(models.Model):
    """
    The Many-to-Many intermediary between a Pizza and a Topping.

    Note that you can avoid defining the "through"field in the Pizza model, and Django will auto-create this for you.
    However, when Django auto-creates the intermediary table, you cannot add custom fields, such as "extra" seen here.
    But Django's auto-created table does let you use add(), create(), set(), and remove().
    """
    # Relationship keys.
    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE)
    topping = models.ForeignKey('Topping', on_delete=models.CASCADE)
    # Additional Many-to-Many fields.
    extra = models.BooleanField(default=False)
    # Self-setting/Non-user-editable fields.
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Modify model save behavior.
        """
        # Save model.
        self.full_clean()
        super(PizzaToppingRelationship, self).save(*args, **kwargs)

        # Update related pizza price via saving related model.
        related_pizza = self.pizza
        related_pizza.save()


class Topping(models.Model):
    """
    A pizza topping model.
    """
    # Model fields
    name = models.CharField(max_length=MAX_LENGTH, unique=True)
    # Self-setting/Non-user-editable fields.
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Topping'
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return '{0}'.format(self.name)

    def clean(self, *args, **kwargs):
        """
        Custom cleaning implementation. Includes validation, setting fields, etc.
        """

    def save(self, *args, **kwargs):
        """
        Modify model save behavior.
        """
        # Save model.
        self.full_clean()
        super(Topping, self).save(*args, **kwargs)


class Pizza(models.Model):
    """
    A pizza model.
    """
    # Relational fields.
    toppings = models.ManyToManyField('Topping', through='PizzaToppingRelationship')
    # Model fields.
    name = models.CharField(max_length=MAX_LENGTH, default='Custom')
    # Self-setting/Non-user-editable fields.
    price = models.DecimalField(max_digits=6, decimal_places=2, default=8)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'

    def __str__(self):
        toppings_on_pizza = self.toppings.all()
        return '{0}: {1}'.format(self.name, list(toppings_on_pizza))

    def clean(self, *args, **kwargs):
        """
        Custom cleaning implementation. Includes validation, setting fields, etc.
        """
        # Automatically calculate pizza price on save.
        # Note: To ensure consistency, that means that pizza.save() should always be called whenever a topping
        # many-to-many relationship is created.
        self.get_price()

    def save(self, *args, **kwargs):
        """
        Modify model save behavior.
        """
        # Save model.
        self.full_clean()
        super(Pizza, self).save(*args, **kwargs)

    def get_price(self):
        """
        Determines price. Will be $8 base plus $1.25 per standard topping and another $0.50 for extra topping.
        """
        # Cannot call a relationship query if self is not saved in database first (aka, pk is not defined).
        # Check for this first. If no pk, then it's impossible to have associated toppings yet so default to base price.
        if self.pk is not None:
            self.price = 8
            # Grab the full Many-to-Many relationship model so we can access the additional fields.
            toppings_on_pizza = PizzaToppingRelationship.objects.filter(pizza=self)
            # Iterate through the returned queryset. Each one is a single topping for this pizza.
            for relationship in toppings_on_pizza:
                if relationship.extra:
                    self.price += 1.75
                else:
                    self.price += 1.25
        else:
            self.price = 8
