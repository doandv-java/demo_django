from django.contrib import admin
from .models import Category, Store, Book


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Name', {'fields': ['name']}),
    #     ('Name Stores', {'fields': ['store_names']})
    # ]
    list_display = ('name', 'name_store')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book)
admin.site.register(Store)
