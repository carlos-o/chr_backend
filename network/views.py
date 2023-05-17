import logging
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from .services import store_network_from_api
from src.settings import LOGGING_CONFIG
from utils.exceptions import NotFound

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


class NetworkApiView(View):
    def get(self, request, network_id, *args, **kwargs):
        try:
            response = store_network_from_api(network_id)
        except NotFound as e:
            logger.warning(str(e))
            return HttpResponse(str(e), status=404)
        except Exception as e:
            logger.error(str(e))
            return HttpResponse(str(e), status=400)
        return JsonResponse(response)
