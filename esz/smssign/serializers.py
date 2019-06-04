from rest_framework import serializers

class ContractSerializer(serializers.Serializer):
    Date = serializers.DateField()
    Number = serializers.CharField()
