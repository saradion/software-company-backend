from django.urls import path
from . import views

urlpatterns = [
    path('poster', views.poster_view.as_view(), name='poster'),
    path('websites', views.websites_view.as_view(), name = 'websites'),
    path('systems', views.systems_view.as_view(), name = 'systems'),
    path('applications', views.applications_view.as_view(), name = 'applications'),
    path('logo', views.logo_view.as_view(), name = 'logo'),
    path('interface', views.interface_view.as_view(), name = 'interface'),
    path('address', views.address_view.as_view(), name = 'address'),
    path('posts', views.posts_view.as_view(), name = 'posts'),
    path('s37', views.s37_view.as_view(), name = 's37'),
    path('associations', views.associations_view.as_view(), name = 'associations'),
    path('footer', views.footer_view.as_view(), name = 'footer'),
    path('intro', views.intro_view.as_view(), name='intro'),
]
