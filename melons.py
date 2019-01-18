"""Classes for melon orders."""


class AbstractMelonOrder:

    def __init__(self, species, qty, country_code=None):
        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        # base_price = 5 
        base_price = 5 * 1.5
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
          total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    
    passed_inspection = False

    tax = 0.00

    def mark_inspection(self, passed):

        self.passed_inspection = passed