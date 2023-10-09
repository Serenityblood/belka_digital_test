from django.conf import settings
from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from .models import RawModel


class RawSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = RawModel
        fields = '__all__'


class ReportSerizlier(serializers.ModelSerializer):
    month = serializers.ChoiceField(
        choices=settings.MONTHES
    )

    class Meta:
        model = RawModel
        fields = (
            'month',
        )


class RawExcelSerializer(serializers.Serializer):
    file = serializers.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['xlsx'])]
    )
