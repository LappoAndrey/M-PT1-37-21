from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

User = get_user_model()


class ProductsForMainPage:

    @staticmethod
    def get_products_for_main_page(*args):
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)

        return products


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="category name")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name="category",
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="title product")
    slug = models.SlugField(unique=True)
    image = models.ImageField()
    description = models.TextField(verbose_name="description", null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2,
                                verbose_name="price")

    def __str__(self):
        return self.title

    # def get_model_name(self):
    #     return self.__class__.__name__.lower()


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name="user",
                             on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, verbose_name="phone")
    address = models.CharField(max_length=255, verbose_name="address")

    def __str__(self):
        return f"Покупатель: {self.user.first_name} {self.user.last_name}"


class Cart(models.Model):
    owner = models.ForeignKey(Customer, verbose_name="owner",
                              on_delete=models.CASCADE)
    products = models.ManyToManyField('CartProduct', blank=True,
                                      related_name='related_cart')
    total_product = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=12, decimal_places=2,
                                      default=0, verbose_name="final_price")

    def __str__(self):
        return str(self.id)


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='user',
                             on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='cart',
                             on_delete=models.CASCADE,
                             related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=12, decimal_places=2,
                                      verbose_name="final_price")

    def __str__(self):
        return f"Товар {self.content_object.title} для корзины"


class Notebook(Product):
    make = models.CharField(max_length=255, verbose_name='make')
    diagonal = models.CharField(max_length=255, verbose_name='diagonal')
    display_type = models.CharField(max_length=255,
                                    verbose_name='display_type')
    processor_freq = models.CharField(max_length=255,
                                      verbose_name='processor_freq')
    ram = models.CharField(max_length=255, verbose_name='ram')
    graphics = models.CharField(max_length=255, verbose_name='graphics')

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return reverse('notebooks_detail', args=[self.slug])

    # def get_model_name(self):
    #     return self.__class__.__name__.lower()


class Smartphone(Product):
    make = models.CharField(max_length=255, verbose_name='make')
    diagonal = models.CharField(max_length=255, verbose_name='diagonal')
    display_type = models.CharField(max_length=255,
                                    verbose_name='display type')
    ram = models.CharField(max_length=255, verbose_name='ram')
    sd = models.BooleanField(default=True, verbose_name='sd')
    main_cam = models.CharField(max_length=255,
                                verbose_name='main cam')
    frontal_cam = models.CharField(max_length=255,
                                   verbose_name='frontal cam')

    def get_absolute_url(self):
        return reverse('smartphones_detail', args=[self.slug])

    # def get_model_name(self):
    #     return self.__class__.__name__.lower()
