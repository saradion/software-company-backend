
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import websites, posts, systems, applications, logo, poster, interface, intro, footer, address, s37, associations
from rest_framework import generics
from .serializers import websites_serializer, interface_serializer, posts_serializer, applications_serializer, logo_serializer, footer_serializer, systems_serializer, address_serializer, intro_serializer, s37_serializer, poster_serializer, associations_serializer
from rest_framework.response import Response
from django.http import request
# Create your views here.

class websites_view(ListAPIView):
    queryset = websites.objects.all() 
    serializer_class = websites_serializer

    def get(self, request, *args, **kwargs):
        websites_list = self.get_queryset()
        websites_data = self.get_serializer(websites_list, many=True, context={'request': request}).data
        return Response(websites_data)

class poster_view(ListAPIView):
    queryset = poster.objects.all() 
    serializer_class = poster_serializer

    def get(self, request, *args, **kwargs):
        poster_list = self.get_queryset()
        poster_data = self.get_serializer(poster_list, many=True, context={'request': request}).data
        return Response(poster_data)


class intro_view(ListAPIView):
    queryset = intro.objects.all() 
    serializer_class = intro_serializer

    def get(self, request, *args, **kwargs):
        intro_list = self.get_queryset()
        intro_data = self.get_serializer(intro_list, many=True, context={'request': request}).data
        return Response(intro_data)


class applications_view(ListAPIView):
    queryset = applications.objects.all() 
    serializer_class = applications_serializer

    def get(self, request, *args, **kwargs):
        applications_list = self.get_queryset()
        applications_data = self.get_serializer(applications_list, many=True, context={'request': request}).data
        return Response(applications_data)


class interface_view(ListAPIView):
    queryset = interface.objects.all() 
    serializer_class = interface_serializer

    def get(self, request, *args, **kwargs):
        interface_list = self.get_queryset()
        interface_data = self.get_serializer(interface_list, many=True, context={'request': request}).data
        return Response(interface_data)


class systems_view(ListAPIView):
    queryset = systems.objects.all() 
    serializer_class = systems_serializer

    def get(self, request, *args, **kwargs):
        systems_list = self.get_queryset()
        systems_data = self.get_serializer(systems_list, many=True, context={'request': request}).data
        return Response(systems_data)


class posts_view(ListAPIView):
    queryset = posts.objects.all() 
    serializer_class = posts_serializer

    def get(self, request, *args, **kwargs):
        posts_list = self.get_queryset()
        posts_data = self.get_serializer(posts_list, many=True, context={'request': request}).data
        return Response(posts_data)



class logo_view(ListAPIView):
    queryset = logo.objects.all() 
    serializer_class = logo_serializer

    def get(self, request, *args, **kwargs):
        logo_list = self.get_queryset()
        logo_data = self.get_serializer(logo_list, many=True, context={'request': request}).data
        return Response(logo_data)

class s37_view(ListAPIView):
    queryset = s37.objects.all() 
    serializer_class = s37_serializer

    def get(self, request, *args, **kwargs):
        s37_list = self.get_queryset()
        s37_data = self.get_serializer(s37_list, many=True, context={'request': request}).data
        return Response(s37_data)

class associations_view(ListAPIView):
    queryset = associations.objects.all()
    serializer_class = associations_serializer

    def get(self, request, *args, **kwargs):
        associations_list = self.get_queryset()
        associations_data = self.get_serializer(associations_list, many=True, context={'request': request}).data
        return Response(associations_data)

class address_view(ListAPIView):
    queryset = address.objects.all() 
    serializer_class = address_serializer

    def get(self, request, *args, **kwargs):
        address_list = self.get_queryset()
        address_data = self.get_serializer(address_list, many=True, context={'request': request}).data
        return Response(address_data)


class footer_view(ListAPIView):
    queryset = footer.objects.all() 
    serializer_class = footer_serializer

    def get(self, request, *args, **kwargs):
        footer_list = self.get_queryset()
        footer_data = self.get_serializer(footer_list, many=True, context={'request': request}).data
        return Response(footer_data)
