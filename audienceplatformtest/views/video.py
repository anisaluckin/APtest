import uuid

from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from audienceplatformtest.HybridStorage import default_hybrid_storage
from audienceplatformtest.models.video import Video
from audienceplatformtest.serializers.video import VideoDetailsSerializer, VideoListSerializer, AdminVideoSerializer


class VideoListView(ListAPIView):
    """
    Get list of all videos
    """
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = VideoListSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Video.objects.all()


class VideoView(GenericAPIView):
    """
    Create, update or get specific video
    """
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = VideoDetailsSerializer
    pagination_class = LimitOffsetPagination

    def get(self, request, id):
        video = Video.objects.get(pk=id)
        return Response(VideoDetailsSerializer(video).data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = Video.objects.get(id=id)
        serializer = VideoDetailsSerializer(data=request.data, instance=instance, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer_data = serializer.validated_data
            serializer.update(instance=instance, validated_data=serializer_data)

        return Response(VideoDetailsSerializer(instance).data, status=status.HTTP_200_OK)


class CreateVideoView(GenericAPIView):
    def post(self, request):
        serializer = VideoDetailsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        video = Video.objects.create(**serializer.validated_data)

        return Response(VideoDetailsSerializer(video).data, status=status.HTTP_201_CREATED)


class AdminVideoView(GenericAPIView):
    """
    Admin create video
    """
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = VideoDetailsSerializer
    pagination_class = LimitOffsetPagination

    def post(self, request):
        serializer = AdminVideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            file_name = str(uuid.uuid4().hex)

            file = request.FILES['url']

            file_path = '{}.{}'.format(file_name, 'mp4')

            path = default_hybrid_storage.save(file_path, file)

            url = default_hybrid_storage.url(path)

            serializer.validated_data['url'] = url.replace('localstack', 'localhost')

            video = Video.objects.create(**serializer.validated_data)

            return Response(VideoDetailsSerializer(video).data, status=status.HTTP_200_OK)