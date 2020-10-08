import requests
from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import views, exceptions, status, renderers
from rest_framework.response import Response
from .models import Reference


class CurrencyAPIView(views.APIView):
    """
    Get exchange rate between the two currencies on particular date
    """

    def get(self, request, *args, **kwargs):
        # Receive date, from and to in params to get data from frankfurter API
        date = request.query_params.get("date", None)
        from_curr = request.query_params.get("from_currency", None)
        to_curr = request.query_params.get("to_currency", None)

        # Add validation if user missing any parameter
        if not date or not from_curr or not to_curr:
            raise exceptions.NotFound("There is a parameter is missing")

        # convert date to python date and currencies to upper
        param_date = datetime.strptime(date, "%Y-%m-%d").date()
        from_currency = str(from_curr).upper()
        to_currency = str(to_curr).upper()

        if param_date > datetime.now().date():
            raise exceptions.NotAcceptable("Date in the future.")

        # Call frankfurter API to get data
        url = "https://api.frankfurter.app/%s?from=%s&to=%s" % (
            param_date,
            from_currency,
            to_currency,
        )

        # Get data from our database.
        reference = Reference.objects.filter(
            date=param_date, from_currency=from_currency, to_currency=to_currency
        )

        if reference:
            # Get response from our database if there.
            response = reference.first().response
        else:
            # The response from frankfurter API and convert it to json to save and display it.
            response = requests.get(url)

            # Check status code.
            if response.status_code != status.HTTP_200_OK:
                raise exceptions.NotFound("No Data Found")

            response = response.json()
            Reference.objects.create(
                date=param_date,
                from_currency=from_currency,
                to_currency=to_currency,
                response=response,
            )
        return Response(response)


class CurrencyView(CurrencyAPIView):
    renderer_classes = (renderers.TemplateHTMLRenderer,)
    template_name = "currency.html"

    def get(self, request, *args, **kwargs):
        res = super(CurrencyView, self).get(request, *args, **kwargs)

        return Response(
            {
                "date": res.data.get("date"),
                "from": res.data.get("base"),
                "to": list(res.data.get("rates").keys())[0],
                "rate": list(res.data.get("rates").values())[0]
            }
        )
