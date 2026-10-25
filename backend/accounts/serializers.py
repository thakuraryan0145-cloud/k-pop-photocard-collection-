from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from catalog.models import Group

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
    )
    favorite_group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = User
        fields = ["id", "email", "password", "display_name", "favorite_group"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        return User.objects.create_user(password=password, **validated_data)