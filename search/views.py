from django.http import Http404
from django.shortcuts import render
from django.views import View

from offers.models import Offer
from search.forms import SearchForm


class HomeView(View):
    def get(self, request, **kwargs):
        form = SearchForm()
        return render(request, 'search/home.html', {
            'form': form
        })

    def post(self, request, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            offers = Offer.objects.all()
            return render(request, 'search/search.html', {
                'offers': offers,
            })
        raise Http404
