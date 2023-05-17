import logging
from src.settings import NETWORK_API_URL
from .models import Network, Company, Location, Stations, Extra, Payment
from utils.exceptions import NotFound
from utils.utils import request_page
from django.db import transaction

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


def store_network_from_api(network_id: str) -> dict:
    # check if network id exist
    network = Network.objects.filter(network_id=network_id).first()
    if network is None:
        try:
            response = request_page(NETWORK_API_URL.format(network_id))
        except NotFound as e:
            raise NotFound(str(e))
        except Exception as e:
            raise Exception(str(e))
        with transaction.atomic():
            data = response.get('network')
            network = Network.objects.create(
                network_id=data.get('id'),
                name=data.get('name'),
                gbfs_href=None if data.get('gbfs_href') is None else data.get('gbfs_href'),
                href=data.get('href')
            )
            # store company if not exist
            for company in data.get('company'):
                obj, created = Company.objects.get_or_create(
                    name=company,
                )
                network.company.add(obj)
            # store location data
            location = Location.objects.create(
                network=network,
                country=data.get('location').get('country'),
                city=data.get('location').get('city'),
                latitude=data.get('location').get('latitude'),
                longitude=data.get('location').get('longitude')
            )
            for station in data.get('stations'):
                station_obj = Stations.objects.create(
                    id=station.get('id'),
                    network=network,
                    name=station.get('name'),
                    free_bikes=station.get('free_bikes'),
                    empty_slots=station.get('empty_slots'),
                    latitude=station.get('latitude'),
                    longitude=station.get('longitude'),
                )
                # create extra value
                extra_obj = station.get('extra')
                extra = Extra.objects.create(
                    stations=station_obj,
                    uid=int(extra_obj.get('uid')),
                    address=extra_obj.get('address'),
                    slots=extra_obj.get('slots'),
                    altitude=0 if extra_obj.get('altitude') is None else extra_obj.get('altitude'),
                    ebikes=0 if extra_obj.get('ebikes') is None else extra_obj.get('ebikes'),
                    has_ebikes=False if extra_obj.get('has_ebikes') is None else extra_obj.get('has_ebikes'),
                    normal_bikes=0 if extra_obj.get('normal_bikes') is None else extra_obj.get('normal_bikes'),
                    payment_terminal=False if extra_obj.get('payment-terminal') is None else extra_obj.get('payment-terminal'),
                    returning=0 if extra_obj.get('returning') is None else extra_obj.get('returning'),
                    renting=0 if extra_obj.get('renting') is None else extra_obj.get('renting')
                )
                # create all payment
                if extra_obj.get('payment'):
                    for payment in extra_obj.get('payment'):
                        obj, created = Payment.objects.get_or_create(
                            name=payment,
                        )
                        extra.payment.add(obj)
        return {"detail": "the network data has been store correctly"}
    return {"detail": "the network element all ready exists"}

