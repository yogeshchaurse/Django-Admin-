from __future__ import absolute_import
from django.db import models
from .utils import ugettext_lazy_compact as _
# from localflavor.in_ import models as india_models



class ClientIndustry(models.Model):
    name =models.CharField(
        max_length=50,
        blank=False,
        unique=True,
        null=False)

    slug= models.SlugField(
        max_length=50,
        blank=False,
        null=False,
        unique=True,
        db_index=True)

    def __unicode__(self):
        return self.name


class Client(models.Model):

    name =models.CharField(
        verbose_name='Client name',
        max_length=200,
        blank=False,
        unique=True,
        null=False
    )

    industry = models.ForeignKey(
        'ClientIndustry',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,)


    mailing_street = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('Mailing Street'))

    mailing_street2 = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('Mailing Street 2'))

    mailing_city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('Mailing City'))

    # mailing_state = india_models.INStateField(
    #     blank=True,
    #     null=True,
    #     verbose_name=_('Mailing State'))

    mailing_zip = models.CharField(
        max_length=10,
        blank=True,
        null=True,)

    website = models.URLField(
        max_length=200,
        blank=True,
        null=True,)

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')

    def __unicode__(self):
        return self.name
