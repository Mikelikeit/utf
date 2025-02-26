from django.contrib import admin
from .models import FoodCategory, Food


# Регистрация модели FoodCategory
@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id')  # Поля, отображаемые в списке
    list_filter = ('order_id',)  # Фильтры справа
    search_fields = ('name_ru', 'name_en', 'name_ch')  # Поиск по полям
    ordering = ('order_id', 'name_ru')  # Сортировка по умолчанию


# Регистрация модели Food
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'category', 'is_publish', 'cost')  # Поля, отображаемые в списке
    list_filter = ('category', 'is_publish', 'is_vegan', 'is_special')  # Фильтры справа
    search_fields = ('name_ru', 'description_ru', 'internal_code')  # Поиск по полям
    list_editable = ('is_publish', 'cost')  # Поля, которые можно редактировать прямо в списке
    raw_id_fields = ('category',)  # Поле для выбора категории (удобно для больших списков)
    filter_horizontal = ('additional',)  # Виджет для выбора дополнительных товаров