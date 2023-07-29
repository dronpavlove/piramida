from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Category


# Create your views here.
def proba_page(request):
    # return render(request, 'base_templates/index.html')
    return render(request, 'catalog/product_list.html', {'num': [i for i in range(16)]})


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/product_list.html'
    context_object_name = 'categories'
    #
    # def get_context_data(self, **kwargs):
    #     """ Показывает список товаров по get запросу """
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = Tag.objects.get(id=self.kwargs['pk']).products.all()
    #     return context
