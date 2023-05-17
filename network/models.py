from django.db import models
from django.utils.translation import gettext as _
from uuid import uuid4


class Company(models.Model):
    name = models.CharField(_('Name'), max_length=100, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Network(models.Model):
    network_id = models.CharField(_('NetworkID'), max_length=100, blank=False, null=False, unique=True)
    name = models.CharField(_('Name'), max_length=100, blank=False, null=False)
    gbfs_href = models.URLField(_('GBFS_Href'), blank=True, null=True)
    href = models.CharField(_('Href'), max_length=255,  blank=False, null=False)
    company = models.ManyToManyField(Company, verbose_name=_('network_company'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Location(models.Model):
    network = models.OneToOneField(Network, related_name='network_location', on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(_('Country'), max_length=2)
    city = models.CharField(_('City'), max_length=100)
    latitude = models.DecimalField(_('Latitude'), max_digits=10, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(_('Longitude'), max_digits=10, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.country}-{self.city}"


class Stations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    network = models.ForeignKey(Network, related_name='network_stations', on_delete=models.CASCADE, blank=True,
                                null=True)
    name = models.CharField(_('Name'), max_length=255, blank=False, null=False)
    free_bikes = models.SmallIntegerField(_('Free Bikes'), blank=False, null=False)
    empty_slots = models.SmallIntegerField(_('Empty Slots'), blank=False, null=False)
    latitude = models.DecimalField(_('Latitude'), max_digits=10, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(_('Longitude'), max_digits=10, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(_('timestamp'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class Payment(models.Model):
    name = models.CharField(_('Name'), max_length=50, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("last_updated"), auto_now=True, editable=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Extra(models.Model):
    stations = models.OneToOneField(Stations, related_name="stations_extra", on_delete=models.CASCADE)
    uid = models.IntegerField(_("UID"), blank=False, null=False)
    altitude = models.SmallIntegerField(blank=True, null=True)
    ebikes = models.SmallIntegerField(default=0)
    has_ebikes = models.BooleanField(default=False)
    normal_bikes = models.SmallIntegerField(default=0)
    address = models.CharField(max_length=255, blank=False, null=False)
    payment_terminal = models.BooleanField(default=False)
    slots = models.SmallIntegerField(default=0)
    returning = models.SmallIntegerField(default=0)
    renting = models.SmallIntegerField(default=0)
    payment = models.ManyToManyField(Payment, related_name="payment_extra", verbose_name=_('payment_extra'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("last_updated"), auto_now=True, editable=False)



