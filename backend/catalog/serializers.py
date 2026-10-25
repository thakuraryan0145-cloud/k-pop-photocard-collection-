from rest_framework import serializers

from catalog.models import Group, Idol


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_id', 'name', 'agency', 'debut_date']


class IdolSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.name', read_only=True)

    class Meta:
        model = Idol
        fields = ['idol_id', 'stage_name', 'group', 'group_name', 'birth_date', 'position']
