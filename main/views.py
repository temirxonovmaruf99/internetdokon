from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django_filters.views import FilterView

from main.filters import ProductFilter
from main.models import Product


def Index_main(request):
    q = request.GET.get('q', '')
    queryset = Product.objects.order_by('-id').all()
    if q is not None:
        queryset = queryset.filter(name__icontains=q)

    return render(request, 'main/index.html', {
        'products': queryset,
        'q': q
    })

    # template_name = 'main/index.html'
    # filterset_class = ProductFilter

    # def get_context_data(self, **kwargs):
    #
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = Product.objects.order_by('-id').all()
    #     return context


class About_main(TemplateView):
     template_name = 'main/about.html'


class ProductWiew(FilterView):
    template_name = 'main/product.html'
    filterset_class = ProductFilter


class ProductInfo(DetailView):
    model = Product
    template_name = 'main/product_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = self.request.session.get('cart')
        pid = str(self.object.id)
        context['cart_p'] = cart[pid] if cart and pid in cart else 0
        return context


class Testimonial_main(TemplateView):
    template_name = 'main/testimonial.html'


class Why_main(TemplateView):
    template_name = 'main/why.html'











