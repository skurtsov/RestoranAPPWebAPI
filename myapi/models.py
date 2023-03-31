from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length= 255, blank=False, null=False, attrs={'class': "input-lg"})
    name_en = models.CharField(max_length=255, blank=False, null=False)
    desc = models.CharField(max_length=255, blank=False, null=False)
    desc_en = models.CharField(max_length=255, blank=False, null=False)
    price = models.CharField(max_length=255, blank=False, null=False)
    category = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to= 'files/',null=True)


    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

    def __str__ (self):
        return self.name
