from django.db import models
from django.utils.translation import gettext as _
from django_jsonform.models.fields import ArrayField


class Snifa(models.Model):
    file = models.CharField(_("File"), max_length=50, blank=False, null=False)
    auditable_unit = ArrayField(models.CharField(_("Auditable Unit"), max_length=20, blank=False, null=False))
    auditable_unit_url = ArrayField(models.URLField(_('Auditable Unit URL'), blank=True, null=True))
    company_name = ArrayField(models.CharField(_("Company Name"), max_length=100, blank=True, null=True))
    category = models.CharField(_("Category"), max_length=255, blank=True, null=True)
    region = models.CharField(_("Region"), max_length=100, blank=False,  null=False)
    state = models.CharField(_("State"), max_length=100, blank=False, null=False)
    detail_url = models.URLField(_('Detail URL'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.auditable_unit
