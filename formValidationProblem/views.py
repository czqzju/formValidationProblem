#########################
# Author:      Nate Cao
# Version:     1.0
# since:       2020-07-24
# last-modify: 2020-07-24
#########################
from django.shortcuts import HttpResponse, render
from django.views import View
from formValidationProblem.my_forms import IndexForm

class Index(View):
    """
    Class Index handles the route 'index/' with get and post methods
    """
    def get(self, request):
        """
        Handles the get method of 'index/'

        @param request: get request
        @type request: django.core.handlers.wsgi.WSGIRequest
        @return: HttpResponse for the http request
        @rtype: HttpResponse
        """
        form = IndexForm()
        return render(request, "index.html", {"form": form})

    def post(self, request):
        """
        Handles the post method of 'index/'. Before handling the form, the validation of form
        is processed.

        @param request: post request
        @type request: request: django.core.handlers.wsgi.WSGIRequest
        @return: HttpResponse
        @rtype: HttpResponse
        """
        form = IndexForm(request.POST)
        if form.is_valid():
            # Handle the form
            return HttpResponse("Form submitted successfully")
        else:
            clean_errors = form.errors.get("__all__")
            return render(request, "index.html", {"form": form, "clean_errors": clean_errors})

