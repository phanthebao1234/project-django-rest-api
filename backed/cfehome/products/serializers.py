from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators
from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name= 'product-detail',
        lookup_field= 'pk',
        read_only= True
    )
    title = serializers.CharField(read_only= True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    # url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field='pk')
    # edit_url = serializers.SerializerMethodField(read_only=True)
    user_flied = 'owner'
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # isStatus = serializers.SerializerMethodField(read_only=True)
    # related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    # email = serializers.EmailField(source='user.email', read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            'owner',
            # 'edit_url',
            # 'url',
            'pk',
            'title',
            'body',
            'price',
            'sale_price',
            'public',
            'path',
            'endpoint',
            # 'email',
            # 'isStatus',
            # 'my_discount',
            # 'my_user_data',
            # 'related_products',
        ]
        
    # def get_my_user_data(self, obj):
    #     return {"'username": obj.user.username,}
    # def validate_title(self, value): 
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user ,title_iexact=value)
    #     if qs.exists(): 
    #         raise serializers.ValidationError(f'{value} is already product name')
    #     return value
    
    
    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email, obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)
    #     # instance.title = validated_data.get('title')
    #     # return instance
    
    # def get_isStatus(self, obj):
    #     if obj.price == 0:
    #         return False
    #     return True
    def get_edit_url(self, obj):
        # return f"/api/product/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={'pk': obj.pk}, request = request)
    def get_url(self, obj):
        # return f"/api/product/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={'pk': obj.pk}, request = request)
        
    # def get_my_discount(self, obj):
    #     return obj.get_discount()

class PrimaryProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
        
    def get_my_discount(self, obj):
        print(obj.id)
        return obj.get_discount()

class SecondaryProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
        
    def get_my_discount(self, obj):
        print(obj.id)
        return obj.get_discount()