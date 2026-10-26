
from rest_framework import serializers

from catalog.models import Group, Idol, Photocard


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_id', 'name', 'agency', 'debut_date']


class IdolSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.name', read_only=True)

    class Meta:
        model = Idol
        fields = [
            'idol_id',
            'stage_name',
            'group',
            'group_name',
            'birth_date',
            'position',
        ]



class PhotocardSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.name', read_only=True)
    idol_names = serializers.StringRelatedField(
        source='idols',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Photocard
        fields = [
            'photocard_id',
            'group',
            'group_name',
            'idols',
            'idol_names',
            'card_type',
            'album_name',
            'version',
            'rarity',
            'image_url',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['photocard_id', 'created_at', 'updated_at']

    def validate(self, attrs):
        # Get submitted values, or existing values when updating.
        group = attrs.get(
            'group',
            self.instance.group if self.instance else None
        )
        card_type = attrs.get(
            'card_type',
            self.instance.card_type if self.instance else 'member'
        )

        if 'idols' in attrs:
            idols = list(attrs['idols'])
        elif self.instance:
            idols = list(self.instance.idols.all())
        else:
            idols = []

        # A member photocard must have exactly one idol.
        if card_type == 'member' and len(idols) != 1:
            raise serializers.ValidationError({
                'idols': 'A member photocard must have exactly one idol.'
            })

        # All selected idols must belong to the selected group.
        for idol in idols:
            if group and idol.group_id != group.group_id:
                raise serializers.ValidationError({
                    'idols': (
                        f'{idol.stage_name} does not belong to '
                        f'{group.name}.'
                    )
                })

        return attrs