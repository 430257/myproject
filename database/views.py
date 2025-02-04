from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
from .models import Database


class IndexView(View):
    def get(self, request):
        return render(request, "database/index.html")


index = IndexView.as_view()
