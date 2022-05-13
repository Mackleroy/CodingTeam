from rest_framework import generics
from django.db.models import Prefetch

from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodCategoryAPIView(generics.ListAPIView):
    queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
        Prefetch(
            'food',
            queryset=Food.objects.filter(is_publish=True),
        )
    ).order_by('id').distinct()
    serializer_class = FoodListSerializer

