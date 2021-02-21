from django.contrib import admin

# Register your models here.


from books.models import Category,Product

admin.site.register(Category)
admin.site.register(Product)