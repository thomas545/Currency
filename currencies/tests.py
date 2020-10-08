from datetime import datetime, timedelta
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Reference


class TestCurrencyView(APITestCase):
    """
    Test Cases for CurrencyView
    """

    def url(self, date, from_currency, to_currency):
        return "%s?date=%s&from_currency=%s&to_currency=%s" % (
            reverse("get_currency"),
            str(date),
            from_currency,
            to_currency,
        )

    def test_get_currencies_from_frankfurter(self):
        # test with success senario
        url = self.url("2020-10-2", "usd", "eur")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("base"), "USD")
        self.assertEqual(response.data.get("date"), "2020-10-02")

    def test_get_currencies_from_reference(self):
        # test if data there in our database
        url = self.url("2020-10-2", "usd", "eur")
        response = self.client.get(url)
        reference = Reference.objects.filter(
            date=response.data.get("date"),
            from_currency=response.data.get("base"),
            to_currency=list(response.data.get("rates").keys())[0],
        )
        self.assertNotEqual(reference, [])
        self.assertEqual(
            reference.first().date,
            datetime.strptime(response.data.get("date"), "%Y-%m-%d").date(),
        )
        self.assertEqual(reference.first().from_currency, response.data.get("base"))
        self.assertEqual(
            reference.first().to_currency, list(response.data.get("rates").keys())[0]
        )

    def test_get_currencies_with_future_date(self):
        # test with date from the future
        url = self.url((datetime.now() + timedelta(days=10)).date(), "usd", "eur")
        response = self.client.get(url)
        self.assertEqual(response.data.get("detail"), "Date in the future.")

    def test_get_currencies_with_wrong_currency(self):
        # test with wrong currency
        url = self.url((datetime.now() - timedelta(days=10)).date(), "usd", "egp")
        response = self.client.get(url)
        self.assertEqual(response.data.get("detail"), "No Data Found")
