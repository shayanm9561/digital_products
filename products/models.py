from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
 parent = models.ForeignKey('self', verbose_name='parent', blank=True, null=True,on_delete=models.CASCADE)
 title = models.CharField(_('Title'),max_length=50)
 description = models.TextField(_('description'),blank=True)
 avatar = models.ImageField(blank=True , upload_to='categories/')
 is_enable = models.BooleanField(default=True)
 created_time = models.DateTimeField(auto_now_add=True)
 update_time = models.DateTimeField(auto_now= True)

 class Meta:
         db_table = 'categories'
         verbose_name = _('category')
         verbose_name_plural = _('Categories')



class Products(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(blank=True, upload_to='products/')
    is_enable = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', verbose_name= _('categories') , blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)




class File(models.Model):
    product = models.ForeignKey('Products',verbose_name='product', on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file = models.FileField(_('file'), upload_to= "files /%y/%m/%d")
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)