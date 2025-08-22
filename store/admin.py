from django.contrib import admin


from .models import Product

# Register your models here.

class ProductAdmin (admin.ModelAdmin):

 list_display = ('product_name', 'price', 'stock', 'Category', 
                 'created_date', 'updated_date', 'is_available')
prepopulated_fields = {'slug': ('product_name',)}
search_fields = ('product_name', 'description','category__category_name')
# list_filter = ('category', 'is_available')
# list_editable = ('price', 'stock', 'is_available')


admin.site.register(Product, ProductAdmin)