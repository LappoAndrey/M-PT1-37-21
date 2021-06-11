from django.db import models, signals
from django.conf import settings
import shutil, os, glob, re
from distutils.dir_util import mkpath


class CustomImageField(models.ImageField):

    def __init__(self, *args, **kwargs):
        kwargs['upload_to'] = kwargs.get('upload_to', 'tmp')

        try:
            self.use_key = kwargs.pop('use_key')
        except KeyError:
            self.use_key = False

        super(CustomImageField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        """Hook up events so we can access the instance."""
        super(CustomImageField, self).contribute_to_class(cls, name)
        signals.post_save.connect(self._move_image, sender=cls)

    def _move_image(self, instance, **kwargs):
        """
            Function to move the temporarily uploaded image to a more suitable directory
            using the model's get_upload_to() method.
        """
        if hasattr(instance, 'get_upload_to'):
            src = getattr(instance, self.attname)
            if src:
                m = re.match(r"%s/(.*)" % self.upload_to, str(src))
                if m:
                    if self.use_key:
                        dst = "%s/%d_%s" % (instance.get_upload_to(self.attname), instance.id, m.groups()[0])
                    else:
                        dst = "%s/%s" % (instance.get_upload_to(self.attname), m.groups()[0])
                    basedir = "%s/%s/" % (settings.MEDIA_ROOT, os.path.dirname(dst))
                    mkpath(basedir)
                    shutil.move("%s/%s" % (settings.MEDIA_ROOT, src), "%s/%s" % (settings.MEDIA_ROOT, dst))
                    setattr(instance, self.attname, dst)
                    instance.save()

    def db_type(self):
        """Required by Django for ORM."""
        return 'varchar(100)'


#class Image(models.Model):
#    file = CustomImageField(use_key=True, upload_to='tmp')

#    def get_upload_to(self, attname):
#        return 'path/{0}'.format(self.id)


class Brand(models.Model):
    brand = models.CharField(max_length=20, blank=False, unique=True)
    slug = models.SlugField(max_length=20, default='', unique=True)
    brand_url = models.URLField(max_length=50, default='')
    logo = models.ImageField(blank=False)

    def __str__(self):
        return self.brand


class ModelBranch(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ModelInstance:
    pass
