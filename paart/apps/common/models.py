from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User

SINGLETON_LOCK_ID = 1


class SingletonManager(models.Manager):
    def get(self, **kwargs):
        instance, created = self.model.objects.get_or_create(lock_id=SINGLETON_LOCK_ID, **kwargs)
        return instance


class Singleton(models.Model):
    lock_id = models.CharField(max_length=1, default=SINGLETON_LOCK_ID, editable=False, verbose_name=_(u'lock field'), unique=True)

    objects = SingletonManager()

    def save(self, *args, **kwargs):
        self.id = 1
        super(Singleton, self).save(*args, **kwargs)

    def delete(self, force=False, *args, **kwargs):
        if force:
            return super(Singleton, self).delete(*args, **kwargs)

    class Meta:
        abstract = True


class AnonymousUserSingletonManager(SingletonManager):
    def passthru_check(self, user):
        if isinstance(user, AnonymousUser):
            return self.model.objects.get()
        else:
            return user


class AnonymousUserSingleton(Singleton):
    objects = AnonymousUserSingletonManager()

    def __unicode__(self):
        return ugettext('Anonymous user')

    class Meta:
        verbose_name = _(u'anonymous user')
        verbose_name_plural = _(u'anonymous user')


class AutoAdminSingleton(Singleton):
    account = models.ForeignKey(User, null=True, blank=True, related_name='auto_admin_account', verbose_name=_(u'account'))
    password = models.CharField(null=True, blank=True, verbose_name=_(u'password'), max_length=128)
    password_hash = models.CharField(null=True, blank=True, verbose_name=_(u'password hash'), max_length=128)

    class Meta:
        verbose_name = verbose_name_plural = _(u'auto admin properties')


class LocMemPropertiesMixin(models.Model):
    """
    A mixin model that gives models a list of pseudo fields or properties that
    persists on instantiation of objects from said models
    Example:
    
    Part(LocMemPropertiesMixin, models.Model):
        local_memory_properties = ['label']
        
        part_num = CharField...
        
    hard_disk = Part.objects.create(part_num='hd_1') <= pk == 1
    hard_disk.label = _(u'Hard disk')  <= this property gets stored in ram and related to instance Part, pk == 1
    hard_disk.color = 'blue' <= only assigned to this instance
    
    hd1 = Part.objects.get(pk=1)
    unicode(hd1.label)
    >>> u'Hard disk'
    hd1.color
    >>> AttributeError
    
    Purpose to 'store' in a semi persistent manner properties that have are only
    useful at runtime and not possible or useful to store in a database backend
    such as ugettext values, lambdas, etc
    """

    _properties_registry = {}
    
    def __getattr__(self, attr):
        if attr in self.__class__.local_memory_properties:
            try:
                return self.__class__._properties_registry[self.pk][attr]
            except KeyError:
                return u''
        else:
            raise AttributeError('\'%s\' object has no attribute \'%s\'' % (self.__class__, attr))

    def __setattr__(self, attr, value):
        if attr in self.__class__.local_memory_properties:
            self.__class__._properties_registry.setdefault(self.pk, {})
            self.__class__._properties_registry[self.pk][attr] = value
        else:
            return super(LocMemPropertiesMixin, self).__setattr__(attr, value)

    def __init__(self, *args, **kwargs):
        super(LocMemPropertiesMixin, self).__init__(*args, **kwargs)
        self.__class__._properties_registry.setdefault(self.pk, {})

    class Meta:
        abstract = True
