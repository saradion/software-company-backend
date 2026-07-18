
from django.db import models

# Create your models here.

###################################################################################

class interface(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000, blank= False)
    file1 = models.FileField(upload_to='media/interface/', blank=True)
    file2 = models.FileField(upload_to='media/interface/', blank=True)
    file3 = models.FileField(upload_to='media/interface/', blank=True)
    class Meta:
        verbose_name = 'رابط کاربری'
        verbose_name_plural = 'رایط کاربری'
    def __str__(self):
        return self.name

#########################################################################################

class intro(models.Model):
    title = models.CharField(max_length=300, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    class Meta:
        verbose_name = "معرفی"
        verbose_name_plural = "معرفی"
    def __str__(self):
        return self.title


class poster(models.Model):
    poster = models.FileField(upload_to='media/poster/', blank=True)
    class Meta:
        verbose_name = "پوستر بالا"
        verbose_name_plural = "پوستر بالا"
    def __str__(self):
        return self.title
#####################################################################################

class logo(models.Model):
    title = models.CharField(max_length= 400, blank=False)
    description = models.TextField(blank=False)
    file1 = models.FileField(upload_to='media/logos/', blank=True)
    file2 = models.FileField(upload_to='media/logos/', blank=True)
    file3 = models.FileField(upload_to='media/logos/', blank=True)
    class Meta:
        verbose_name = 'لوگو'
        verbose_name_plural = 'لوگوها'
    def __str__(self):
        return self.title

#################################################################################################

class systems(models.Model):
    title = models.CharField(max_length= 400)
    description = models.TextField(blank=True)
    file1 = models.FileField(upload_to='media/systems/', blank=True)
    file2 = models.FileField(upload_to='media/systems/', blank=True)
    file3 = models.FileField(upload_to='media/systems/', blank=True)
    link = models.URLField(blank=True)
    class Meta:
        verbose_name = 'سامانه مدیریتی'
        verbose_name_plural = 'سامانه های مدیریتی'
    def __str__(self):
        return self.title

#############################################################################

class applications(models.Model):
    title = models.CharField(max_length= 400)
    description = models.TextField(blank=True)
    file1 = models.FileField(upload_to='media/applications/', blank=True)
    file2 = models.FileField(upload_to='media/applications/', blank=True)
    file3 = models.FileField(upload_to='media/applications/', blank=True)
    link = models.URLField(blank=True)
    class Meta:
        verbose_name = 'اپلیکیشن ها'
        verbose_name_plural = 'اپلیکیشن ها'
    def __str__(self):
        return self.title

##############################################################################
class websites(models.Model):
    title = models.CharField(max_length= 400)
    description = models.TextField(blank=True)
    file1 = models.FileField(upload_to='media/websites/', blank=True)
    file2 = models.FileField(upload_to='media/websites/', blank=True)
    file3 = models.FileField(upload_to='media/websites/', blank=True)
    link = models.URLField(blank=True)

    class Meta:
        verbose_name = 'وبسایت'
        verbose_name_plural = 'وبسایت ها'
    def __str__(self):
        return self.title

###################################################################################

class posts(models.Model):
    title = models.CharField(max_length=400)
    file1 = models.FileField(upload_to='media/posts/', blank=True)
    file2 = models.FileField(upload_to='media/posts/', blank=True)
    file3 = models.FileField(upload_to='media/posts/', blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
    def __str__(self):
        return self.title

###############################################################################

class s37(models.Model):
    title = models.CharField(max_length=250, default='سامانه ورزشی 37')
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='media/s37/', blank=True)
    link = models.URLField()
    class Meta:
        verbose_name = 'سامانه 37'
        verbose_name_plural = 'سامانه 37'
    def __str__(self):
        return self.title 

#############################################################

class associations(models.Model):
    title = models.CharField(max_length=500, blank=True)
    image = models.FileField(upload_to='media/associations/')
    class Meta:
        verbose_name = 'همکاری'
        verbose_name_plural = 'همکاری ها'
    def __str__(self):
        return self.title 

#############################################################

class address(models.Model):
    title = models.CharField(max_length=250, default='آدرس')
    address = models.TextField(blank=True)
    link = models.URLField(blank=True)

###################################################################

class footer(models.Model):
    link1 = models.URLField(blank=True)
    link2 = models.URLField(blank=True)
    link3 = models.URLField(blank=True)
    link4 = models.URLField(blank=True)
    link5 = models.URLField(blank=True)
    link6 = models.URLField(blank=True)
    link7 = models.URLField(blank=True)
    number1 = models.CharField(max_length= 13, blank=True)
    number2 = models.CharField(max_length= 13, blank=True)
    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'ارتباط با ما'
    def __str__(self):
        return self.title 
