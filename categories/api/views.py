from rest_framework.viewsets import ModelViewSet



from categories.models import Category
from categories.api.permissions import IsAdminOrReadOnly
from categories.api.serializers import CategorySerializer

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()