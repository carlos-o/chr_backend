from bs4 import BeautifulSoup
from urllib3.exceptions import HTTPError
from .exceptions import NotFound
import requests
import logging

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


def request_page(url: str, response_type="json"):
    try:
        logger.info("Make requests from sii page")
        response = requests.get(url=url)
    except requests.exceptions.HTTPError as e:
        logger.error(f"Request Problem exceptions HTTPError {str(e)}")
        raise HTTPError(str(e))
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Request Problem exceptions ConnectionError {str(e)}")
        raise ConnectionError(str(e))
    except requests.exceptions.Timeout as e:
        logger.error(f"Request Problem exceptions Timeout {str(e)}")
        raise TimeoutError(str(e))
    except requests.exceptions.RequestException as e:
        logger.error(f"Request Problem exceptions RequestException {str(e)}")
        raise ValueError(str(e))
    except Exception as e:
        logger.error(f"Request Problem exceptions {str(e)}")
        raise Exception(str(e))
    if response.status_code == 200:
        if response_type == 'json':
            return response.json()
        return response.text
    raise NotFound("The requested URL was not found on the server")


def parse_html(source: str) -> BeautifulSoup:
    """
        Parser the content html

        :param source: html to parse
        :type source: str
        :return: BeautifulSoup parser content
    """
    try:
        logger.info("parse html page")
        parser = BeautifulSoup(source, 'html.parser')
    except Exception as e:
        logger.error(f"ERROR cannot be parser this content {str(e)}")
        raise ValueError(str(e))
    return parser
