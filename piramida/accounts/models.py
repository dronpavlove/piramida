from django.core.validators import RegexValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# from timestamps.models import models, SoftDeletes


class Client(models.Model):  # SoftDeletes):
    """Основная модель пользователя"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("пользователь")
    )
    postcode = models.IntegerField(_("почтовый индекс"), blank=True, null=True)
    photo = models.ImageField(_("фотография"), upload_to='accounts/', null=True, blank=True)
    phoneNumberRegex = RegexValidator(
        regex=r"^\+?7?\d{8,15}$",
        message='Введите корректный номер, без пробелов (+79999999999)'
    )
    phone = models.CharField(unique=True, null=True,
                             verbose_name=_('контактный номер'),
                             validators=[phoneNumberRegex],
                             max_length=16,
                             )
    city = models.CharField(_('город'), max_length=256, blank=True, null=True)
    street = models.CharField(_("улица"), max_length=256, blank=True, null=True)
    house_number = models.IntegerField(_("номер дома"), blank=True, null=True)
    full_address = models.TextField('Полный адрес', blank=True, null=True)
    apartment_number = models.IntegerField(
        _("номер квартиры"),
        blank=True, null=True
    )
    spent_money = models.DecimalField(
        _("потратил денег"),
        max_digits=9,
        decimal_places=2,
        default=0
    )
    is_seller = models.BooleanField(_("продавец"), default=False)

    patronymic = models.CharField(default='', max_length=50,
                                  error_messages={'max_length': 'Слишком длинное Отчество!'},
                                  verbose_name=_('Отчество'))

    item_view = models.ManyToManyField('catalog.Product', verbose_name=_('Товары, которые смотрел пользователь'),
                                       blank=True,
                                       through="ClientProductView",
                                       )

    limit_items_views = models.IntegerField(verbose_name=_('Сколько максимум показывать товаров'),
                                            help_text=_('Тут можно изменить это значение, по умолчанию 20 минимум 4.'),
                                            default=20, validators=[MinValueValidator(4)],
                                            blank=True,
                                            )
    item_in_page_views = models.IntegerField(verbose_name=_('По сколько товаров выводить на странице'),
                                             default=8,
                                             help_text=_('По сколько товаров будет добавляться при нажатии на кнопку '
                                                         '"показать еще", но не больше чем разрешено'),
                                             validators=[MinValueValidator(2)],
                                             error_messages={'min_length': 'Не стоит устанавливать меньше 2!'},
                                             blank=True,
                                             )

    # Проверяем, не больше ли чем позволено
    def item_in_page_views_check(self):
        if self.item_in_page_views >= self.limit_items_views:
            self.item_in_page_views = self.limit_items_views
        return self.item_in_page_views

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        db_table = 'Client'


class ClientProductView(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE,
                               related_name='client_products_view',
                               related_query_name='client_products_views')
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE,
                                related_name='client_products_view',
                                related_query_name='client_products_views')

    created_dt = models.DateField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'просмотренный товар'
        verbose_name_plural = 'просмотренные товары'
        ordering = ("-created_dt",)


class Order(models.Model):  # SoftDeletes):
    """
    Модель заказа товаров
    """
    CHOICES_DELIVERY = [('Обычная доставка', _('Обычная доставка')),
                        ('Экспресс доставка', _('Экспресс доставка (+500 руб.)'))]

    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               related_name='client_order_view',
                               related_query_name='client_order_views')
    clients_check = models.FileField(_("чек"), upload_to='check/', null=True, blank=True)
    created_dt = models.DateField(auto_now_add=True)
    delivery = models.CharField(max_length=50, choices=CHOICES_DELIVERY, db_index=True, default='Обычная доставка',
                                verbose_name=_('Способ доставки'))
    status_pay = models.BooleanField(default=False, verbose_name=_('Статус оплаты'))
    number_order = models.TextField('Номер заказа', blank=True, null=True)
    delivery_price = models.DecimalField(verbose_name=_("цена доставки"),
                                         max_digits=9,
                                         decimal_places=2,
                                         default=0)

    def __str__(self):
        return _('Заказ_№') + str(self.number_order)

    class Meta:
        verbose_name = _('заказ')
        verbose_name_plural = _('заказы')
        db_table = 'Orders'
        ordering = ['-number_order']


class Photo(models.Model):
    photo = models.ImageField(_("фотография"), upload_to='accounts/', null=True, blank=True)
