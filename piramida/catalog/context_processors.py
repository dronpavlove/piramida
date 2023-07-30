from django.http import HttpRequest
from django.core.cache import cache

from .models import Category


def main_menu_categories(request: HttpRequest) -> dict:
    """
    Добавляет активные категории каталога в контекст шаблона.
    """
    active_categories = Category.objects.only("category_name", "icon_photo") \
        .filter(activity=True).order_by("category_name")
    return {
        "active_categories": active_categories,
    }


def getting_compare_info(request):
    """Возвращаут все данные этой функции"""
    session_key = request.session.session_key
    count_product_compare = 0
    if not session_key:
        request.session.cycle_key()
    if cache.get(str(session_key) + '_compare_count'):
        count_product_compare = cache.get(str(session_key) + '_compare_count')

    return locals()


def basket_client_info(request):
    """
    При помощи этого контекст процессора на странице всегда есть инфа о корзине
    """
    count_product_in_basket = 0
    session_key = request.session.session_key
    full_sum = 0
    basket = ()
    if not session_key:
        request.session.cycle_key()
    # try:
    #     basket = BasketClient.objects.select_related('product', 'client').filter(
    #         client=request.user.client, flag_paid='n'
    #     )
    # except:
    #     basket = BasketClient.objects.select_related('product').filter(
    #         session=session_key, flag_paid='n'
    #     )
    if len(basket) != 0:
        count_product_in_basket += sum([i.product_amount for i in basket])
        full_sum += sum([i.total_cost for i in basket])

    return {'basket':  basket, 'count_product_in_basket': count_product_in_basket, 'full_sum': full_sum}