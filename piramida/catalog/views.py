from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Category, Product


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.sort_params = self._get_sort_params()

    def get_queryset(self, **kwargs):
        products = self.model.objects.prefetch_related(
            "product_photo", "category"
        ).filter(category=self.kwargs['pk'])
        if (order := self.sort_params["order_by"]) is not None:
            products = products.order_by(order)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        # параметры сортировки
        ctx["sort_params"] = self.sort_params
        # ctx["categories"] = [i for i in Category.objects.all()]
        ctx["category"] = ctx['products'][0].category.category_name
        # пагинатор
        # ctx.update(self.get_paginated_range(ctx["page_obj"], ctx["paginator"]))

        return ctx

    def _get_sort_params(self):
        # sorts
        price_asc = "price_asc"
        price_desc = "price_desc"
        rating_asc = "rating_asc"
        rating_desc = "rating_desc"

        # CSS classes
        sort_asc_class = "Sort-sortBy_inc"
        sort_desc_class = "Sort-sortBy_dec"

        # defaults
        sort_params = {
            "price": {
                "sort": price_asc,
                "class": None,
            },
            "rating": {
                "sort": rating_asc,
                "class": None,
            },
            "order_by": None,  # field name for model sorting
        }

        if sort_kind := self.request.GET.get("sort"):
            if sort_kind == price_asc:
                sort_params["price"].update({
                    "sort": price_desc,
                    "class": sort_desc_class,
                })
                sort_params["order_by"] = "price"
            elif sort_kind == price_desc:
                sort_params["price"].update({
                    "sort": price_asc,
                    "class": sort_asc_class,
                })
                sort_params["order_by"] = "-price"
            elif sort_kind == rating_asc:
                sort_params["rating"].update({
                    "sort": rating_desc,
                    "class": sort_desc_class,
                })
                sort_params["order_by"] = "rating"
            elif sort_kind == rating_desc:
                sort_params["rating"].update({
                    "sort": rating_asc,
                    "class": sort_asc_class,
                })
                sort_params["order_by"] = "-rating"

        return sort_params
