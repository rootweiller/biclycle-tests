from rest_framework import serializers

from bicycle.models import Bicycle


class BicycleSerializers(serializers.ModelSerializer):

    class Meta:

        model = Bicycle
        fields = '__all__'
