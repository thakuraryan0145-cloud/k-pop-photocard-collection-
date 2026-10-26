
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from catalog.models import Group, Idol, Photocard
from catalog.serializers import (
    GroupSerializer,
    IdolSerializer,
    PhotocardSerializer,
)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class IdolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Idol.objects.select_related('group')
    serializer_class = IdolSerializer
    filterset_fields = ['group']
    permission_classes = [AllowAny]


class PhotocardViewSet(viewsets.ModelViewSet):
    queryset = Photocard.objects.select_related('group').prefetch_related('idols')
    serializer_class = PhotocardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
