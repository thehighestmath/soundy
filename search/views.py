from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View

from search.forms import SearchForm


class HomeView(View):
    def get(self, request, **kwargs):
        form = SearchForm()
        return render(request, 'hh/home.html', {
            'form': form
        })

    def post(self, request, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            print(form.data)
            return render(request, 'hh/search.html')
        raise Http404
