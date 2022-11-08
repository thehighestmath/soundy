from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from offers.forms import OfferForm
from offers.models import Offer


# Create your views here.
class OffersView(View):
    def get(self, request, **kwargs):
        offers = Offer.objects.filter(user_id=request.user.pk)
        return render(request, 'offers/offers.html', {
            'offers': offers
        })


class OfferCreateView(View):
    def get(self, request, **kwargs):
        form = OfferForm()
        return render(request, 'offers/offer_create.html', {
            'form': form
        })

    def post(self, request, **kwargs):
        form = OfferForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            Offer.objects.create(
                price=form.price,
                user=request.user,
            )
            return redirect('offers')
        raise Http404
