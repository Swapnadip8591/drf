from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    '''
    We can change field name here also
    '''
    actual_price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'actual_price',
            'sale_price'    #unlike normal method mentioning in api/views, serializer can access func. returns
        ]
    
    def get_actual_price(self, obj):
        return obj.price