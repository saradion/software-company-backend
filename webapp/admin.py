from django.contrib import admin
from .models import interface, posts, systems, applications, websites, logo, footer, s37, address, intro, poster, associations
# Register your models here.


@admin.register(poster)
class poster_admin(admin.ModelAdmin):
    list_display = ('poster',)

@admin.register(interface)
class interface_admin(admin.ModelAdmin):
    list_display = ('title', 'file1', 'file2', 'file3', 'description')
    search_fields = ('title',)

@admin.register(systems)
class systems_admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'file1', 'file2', 'file3')
    search_fields = ('title',)

@admin.register(intro)
class start_admin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(applications)
class applications_admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'file1', 'file2', 'file3')
    search_fields = ('title',)

@admin.register(websites)
class websites_admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'file1', 'file2', 'file3')
    search_fields = ('title',)

@admin.register(logo)
class logo_admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'file1', 'file2', 'file3')
    search_fields = ('title',)


@admin.register(s37)
class s37_admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'image')

@admin.register(posts)
class posts_admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'file1', 'file2', 'file3')
    search_fields = ('title',)

@admin.register(associations)
class associations_admin(admin.ModelAdmin):
        list_display = ('title', 'image',)

@admin.register(address)
class address_admin(admin.ModelAdmin):
    list_display = ('address', 'link')

@admin.register(footer)
class footer_admin(admin.ModelAdmin):
    list_display = ('link1', 'link2', 'link3', 'link4', 'link5', 'link6', 'link7', 'number1', 'number2')
