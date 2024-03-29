from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length= 255, blank=False, null=False)
    name_en = models.CharField(max_length=255, blank=False, null=False)
    name_cat = models.CharField(max_length=255, blank=False, null=False)
    desc = models.CharField(max_length=255, blank=False, null=False)
    desc_en = models.CharField(max_length=255, blank=False, null=False)
    desc_cat = models.CharField(max_length=255, blank=False, null=False)
    price = models.CharField(max_length=255, blank=False, null=False)
    category = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to= 'files/',blank=True,null=True)


    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

    def __str__ (self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __repr__(self):
        return 'Drink(%s, %s)' % (self.name, self.file)

    def __str__ (self):
        return self.name
