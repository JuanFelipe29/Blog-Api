from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


from categories.models import Category
from categories.api.permissions import IsAdminOrReadOnly
from categories.api.serializers import CategorySerializer

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published']