from rest_framework import serializers
from .models import Users,Shipment

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=['username','role','email','password']
    def create(self, validated_data):
        password=validated_data.pop('password')
        user=Users(**validated_data)
        if password:
            user.set_password(password)
            user.save()
            return user


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shipment
        fields='__all__'
