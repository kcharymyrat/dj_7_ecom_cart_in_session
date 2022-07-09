from .models import Category, Product


def categories(request):
    return {"cp_categories": Category.objects.all()}


def active_products(request):
    return {"cp_actives": Product.actives.all()}
