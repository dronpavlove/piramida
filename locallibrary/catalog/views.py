from django.shortcuts import render


# Create your views here.
def proba_page(request):
    # return render(request, 'base_templates/index.html')
    return render(request, 'catalog/product_list.html', {'num': [i for i in range(16)]})
