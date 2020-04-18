from rest_framework import serializers

from personal.models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    # urls = UrlListSerializer(many=True)
    # groups = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Goods
        # fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        # fields = '__all__'
        exclude = ('is_delete','is_sale','user')
        # allow_null = False
        # depth = 2

class Goods2Serializer(serializers.ModelSerializer):
    # urls = UrlListSerializer(many=True)
    # groups = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Goods
        # fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        # fields = '__all__'
        exclude = ('is_delete','is_sale','user','all_pics')
        # allow_null = False