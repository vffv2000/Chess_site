from rest_framework import serializers
from .models import *


class MastersSerializer(serializers.ModelSerializer):
    class Meta():
        model = Masters
        fields = ('title', 'cat_id')