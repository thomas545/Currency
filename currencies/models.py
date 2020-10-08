from django.db import models
from .fields import JSONField


class Reference(models.Model):
    # Store data from API to our database.
    date = models.DateField()
    from_currency = models.CharField(max_length=5)
    to_currency = models.CharField(max_length=5)
    response = JSONField(blank=True)

    def __str__(self):
        return "Date: %s- From: %s- To: %s" % (
            str(self.date),
            self.from_currency,
            self.to_currency,
        )
