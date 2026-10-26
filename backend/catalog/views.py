from rest_framework import viewsets

from catalog.models import Group, Idol
from catalog.serializers import GroupSerializer, IdolSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class IdolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Idol.objects.select_related('group')
    serializer_class = IdolSerializer
    filterset_fields = ['group']
