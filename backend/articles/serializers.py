from rest_framework import serializers
from .models import Article
from likes import services as likes_services

class ArticleSerializer(serializers.ModelSerializer):

    is_estimated = serializers.SerializerMethodField()

    class Meta:
        
        model = Article
        fields = (
            'title',
            'body',
            'date_pub',
            'teacher',
            'total_likes',
            'is_estimated',
        )

    def get_is_estimated(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_estimated(obj, user)

