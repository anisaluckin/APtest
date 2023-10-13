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

