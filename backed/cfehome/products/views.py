from rest_framework import generics, mixins

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from api.mixin import (
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    )
from .serializers import ProductSerializer

class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
        # send a Django signal
    
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     # print(request.user)
    #     return qs.filter(user=request.user)


product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin, 
    generics.RetrieveAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # lookup_field ??
    
product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin, 
    generics.UpdateAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.DjangoModelPermissions]
    
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        ##    
        

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin, 
    generics.DestroyAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        # intansce
        super().perform_destroy(instance)   
        

product_delete_view = ProductDestroyAPIView.as_view()

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin, # cung cấp pt list() => danh sách đối tượng model, 1 queryset, có thể phân trang 
    mixins.RetrieveModelMixin, # trả về 1 đối tượng cụ thể 
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs): # HTTP -> get
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        print(args, kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # print(serializer)
        # serializer.save()
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)
    
product_mixin_view = ProductMixinView.as_view()
# Ghi đè 2 pt api_view GET và POST
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    # lấy phương thức được truyền vào
    method = request.method
    
    # Kiểm tra
    if method == 'GET':
        # Kiểm tra khóa chính
        if pk is not None: # nếu khóa chính tồn tại thì sẽ tìm và xuất sản phẩm tương ứng
            # detail view
            obj = get_object_or_404(Product, pk=pk) # get_object_or_404 => nó sẽ có 2 trường trả về 1 là có dữ liệu và 2 là Not Found 
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # nếu không có khóa chính được truyền vào thì sẽ xuất ra danh sách sản phẩm
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == 'POST':
        #create an item
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"}, status=400)