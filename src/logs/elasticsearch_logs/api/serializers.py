from rest_framework import serializers

from logs.elasticsearch_logs.models import Logs

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = "__all__"