from rest_framework import serializers
from .models import websites, systems, applications, logo, s37, posts, interface, address, footer, intro, poster, associations


class poster_serializer(serializers.ModelSerializer):
    class Meta:
        model = poster
        fields = '__all__'

class applications_serializer(serializers.ModelSerializer):
    class Meta:
        model = applications
        fields = '__all__'

class intro_serializer(serializers.ModelSerializer):
    class Meta:
        model = intro
        fields = '__all__'

class systems_serializer(serializers.ModelSerializer):
    class Meta:
        model = systems
        fields = '__all__'

class logo_serializer(serializers.ModelSerializer):
    class Meta:
        model = logo
        fields = '__all__'

class websites_serializer(serializers.ModelSerializer):
    class Meta:
        model = websites
        fields = '__all__'

class s37_serializer(serializers.ModelSerializer):
    class Meta:
        model = s37
        fields = '__all__'


class interface_serializer(serializers.ModelSerializer):
    class Meta:
        model = interface
        fields = '__all__'

class posts_serializer(serializers.ModelSerializer):
    class Meta:
        model = posts
        fields = '__all__'

class associations_serializer(serializers.ModelSerializer):
    class Meta:
        model = associations
        fields = '__all__'

class address_serializer(serializers.ModelSerializer):
    class Meta:
        model = address
        fields = '__all__'

class footer_serializer(serializers.ModelSerializer):
    class Meta:
        model = footer
        fields = '__all__'
