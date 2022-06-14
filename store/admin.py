
from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.http import HttpRequest
from django.utils.html import format_html, urlencode
from django.db.models import QuerySet
from django.urls import reverse

from tags.models import TaggedItem
from . import models
# constant values 
INVENTORY_LOW = '<10'
INVENTORY_OK = '>=10'
INVENTORY_LOW_CHOICES={
    INVENTORY_LOW: 10,
    INVENTORY_OK : 10
}

# custom filters
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self,  request: HttpRequest, model_admin):
        return [
            (INVENTORY_LOW, 'Low'),
            (INVENTORY_OK, 'Ok')
        ]

    def queryset(self,  request: HttpRequest, queryset: QuerySet):
        if self.value() == INVENTORY_LOW:
            return queryset.filter(inventory__lt =INVENTORY_LOW_CHOICES[INVENTORY_LOW])
        elif self.value() == INVENTORY_OK:
            return queryset.filter(inventory__gte =INVENTORY_LOW_CHOICES[INVENTORY_OK])

# product images
class ProductImageInline(admin.TabularInline):
    model =models.ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''
# product class
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):    
    autocomplete_fields = ['collection']
    prepopulated_fields ={
        'slug' : ['title']
    }
    actions = ['clear_inventory']   
    inlines = [ProductImageInline]
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    ordering = ['title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']
    search_fields = ['title']

    @admin.display(ordering = 'inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'

        return 'Ok'

    def collection_title(self,product):
        return product.collection.title

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request: HttpRequest, queryset:QuerySet):
        updated_count = queryset.update(inventory = 0)
        self.message_user(
            request,
            f'{updated_count} products were sucessfully updated',
            messages.ERROR
        )

    class Media:
        css = {
            'all':['store/styles.css']
        }
    
# customer class 
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']   
    list_editable = ['membership']
    list_per_page = 10 
    list_select_related= ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    def get_queryset(self,  request: HttpRequest):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )
    

# collection class 
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    ordering = ['title']    
    list_per_page = 10
    search_fields = ['title']

    @admin.display(ordering= 'products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist') 
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return  format_html('<a href="{}">{}</a>', url, collection.products_count)
        

    def get_queryset(self,  request: HttpRequest):
        return super().get_queryset(request).annotate(
            products_count = Count('products')
        )


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']

    



