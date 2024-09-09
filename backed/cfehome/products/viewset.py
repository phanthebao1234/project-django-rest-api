from rest_framework import viewsets, mixins 

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
        get -> list -> Queryset
        get -> retrieve -> Product Instance Detail View
        post -> create -> New Instance
        put -> update
        patch -> Partical update
        delete -> destroy 
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ProductGenericViewSet(
    viewsets.GenericViewSet, 
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    '''
        get -> list -> Queryset
        get -> retrieve -> Product Instance Detail View
        
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
# product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
# product_list_detail = ProductGenericViewSet.as_view({'get': 'retrieve'})

class ProductGenericViewSetv2(
    viewsets.ReadOnlyModelViewSet, 
):
    '''
        get -> list -> Queryset
        get -> retrieve -> Product Instance Detail View
        
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
