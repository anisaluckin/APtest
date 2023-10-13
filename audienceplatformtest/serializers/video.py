from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from audienceplatformtest.models.video import Video


class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'name')


class VideoDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'name', 'url')


class AdminVideoSerializer(serializers.ModelSerializer):
    url = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    class Meta:
        model = Video
        fields = ('name', 'url')
