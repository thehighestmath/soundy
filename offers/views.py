from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from account_service.decorators import blogger_required
from account_service.models import Blogger
from offers.forms import OfferForm
from offers.models import Offer


# Create your views here.
class OffersView(View):
    @method_decorator(login_required())
    def get(self, request, **kwargs):
        offers = Offer.objects.filter(blogger__user_id=request.user.pk)
        return render(request, 'offers/offers.html', {
            'offers': offers
        })


class OfferCreateView(View):
    @method_decorator(login_required())
    @method_decorator(blogger_required())
    def get(self, request, **kwargs):
        form = OfferForm()
        return render(request, 'offers/offer_create.html', {
            'form': form
        })

    def post(self, request, **kwargs):
        form = OfferForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            blogger = Blogger.objects.get(user_id=request.user.id)
            Offer.objects.create(
                price=form.price,
                description=form.description,
                blogger=blogger,
            )
            return redirect('offers')
        raise Http404
