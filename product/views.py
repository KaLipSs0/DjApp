from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *


class GeneralProductView(CreateModelMixin, ListModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, **kwargs):
        return self.list(request, **kwargs)

    def post(self, request, **kwargs):
        return self.create(request, **kwargs)


class DetailProductView(
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
):
    queryset = Product.objects.filter()
    lookup_field = 'name'
    serializer_class = ProductSerializer

    def get(self, request, **kwargs):
        instance = self.get_object()  # self.queryset.get(id=kwargs['id'])
        serializer = self.get_serializer(instance)  # GeneralUsersSerializer(instance)
        return Response(serializer.data)

    def patch(self, request, **kwargs):
        return self.partial_update(request, **kwargs)

    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)
