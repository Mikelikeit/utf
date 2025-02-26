from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodListView(APIView):
    def get(self, request):
        # Фильтруем категории, у которых есть хотя бы одно опубликованное блюдо
        categories = FoodCategory.objects.prefetch_related(
            Prefetch(
                'food',
                queryset=Food.objects.filter(is_publish=True),
                to_attr='published_foods'
            )
        ).filter(food__is_publish=True).distinct()

        # Сериализуем данные.q
        serializer = FoodListSerializer(categories, many=True)

        # Возвращаем JSON-ответ
        return Response(serializer.data, content_type='application/json')
