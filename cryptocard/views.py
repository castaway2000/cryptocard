from django.shortcuts import render
from .models import PageContent, Orders
from cryptocard import settings
import stripe


#loaded via code
def home(request):
    stripe.key = settings.STRIPE_PUBLIC_KEY
    new_order = Orders(
        email='',
        description='',
        amount='',
        charge_id=''
    )

    cost = {
        '1': 100,
        '2': 20,
        '3': 50,
        '4': 250,
        '5': 500,
    }
    product = {
        'eth': ['Etherium GiftWallet', '', ''],
        'btc': ['BitCoin GiftWallet', '', ''],
        'ltc': ['LiteCoin GiftWallet', '', ''],
    }

    if request.method == "POST":
        token = request.POST.get("stripeToken")
        id = request.POST.get("id")
        prod = request.POST.get("name")
        try:
            charge = stripe.Charge.create(
                amount=cost[id],
                currency="usd",
                source=token,
                description='$%s %s' % (cost[id], product[prod][0])
            )
            new_order.charge_id = charge.id
            new_order.description = charge.description
            new_order.amount = charge.amount

        except stripe.error.CardError as ce:
            return False, ce
    else:
        new_order.save()
    return render(request, 'landing.html', locals())


# loaded via django pagecontnet
def tos(request):
    terms = PageContent.objects.get(id=1, is_active=True)
    return render(request, 'tos.html', locals())


def contact(request):
    return render(request, 'contact.html', locals())


def faq(request):
    frequent_questions = PageContent.objects.get(id=2, is_active=True)
    return render(request, 'faq.html', locals())