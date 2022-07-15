from rest_framework import serializers
from .models import BasicSock
from .models import Stash

class SockSerializer(serializers.HyperlinkedModelSerializer):
    # songs = serializers.HyperlinkedRelatedField(
    #     view_name='song_detail',
    #     many=True,
    #     read_only=True
    # )
    sock_url = serializers.ModelSerializer.serializer_url_field(
        view_name='sock_detail'
    )

    class Meta:
        model = BasicSock
        fields = ('id', 'sock_url', 'name', 'toeColor','ankleColor', 'heelColor', 'footColor', 'ribColor','foot_stripe','in_progress','completed','knitStatus','user_photo')


class StashSerializer(serializers.HyperlinkedModelSerializer):
    # songs = serializers.HyperlinkedRelatedField(
    #     view_name='song_detail',
    #     many=True,
    #     read_only=True
    # )
    stash_url = serializers.ModelSerializer.serializer_url_field(
        view_name='stash_detail'
    )

    class Meta:
        model = Stash
        fields = ('id','stash_url','brand','colorName','colorCode','yardage','grams','nickname','description')