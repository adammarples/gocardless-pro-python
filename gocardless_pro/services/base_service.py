# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import re
import time

from .. import list_response
from ..api_response import ApiResponse

class BaseService(object):
    """Base class for API service classes."""
    def __init__(self, api_client):
        self._api_client = api_client

    def _attempt_request(self, method, path, params, headers):
        if method == 'GET':
            return self._api_client.get(path, params=params, headers=headers)

        if method == 'POST':
            return self._api_client.post(path, body=params, headers=headers)

        if method == 'PUT':
            return self._api_client.put(path, body=params, headers=headers)

        raise ValueError('Invalid method "{}"'.format(method))

    def _perform_request(self, *args, **kwargs):
        max_attempts = kwargs.pop('retries', 1)
        retry_delay_seconds = kwargs.pop('retry_delay_seconds', 0.5)
        network_execption = None
        for _ in range(max_attempts):
            try:
                return self._attempt_request(*args, **kwargs)
            except Exception as e:
               network_exception = e
               time.sleep(retry_delay_seconds)
        raise network_exception

    def _envelope_key(self):
        return type(self).RESOURCE_NAME

    def _resource_for(self, response):
        api_response = ApiResponse(response)

        data = api_response.body[self._envelope_key()]
        klass = type(self).RESOURCE_CLASS
        if isinstance(data, dict):
            return klass(data, api_response)
        else:
            records = [klass(item, api_response) for item in data]
            return list_response.ListResponse(records, api_response)

    def _sub_url_params(self, url, params):
        return re.sub(r':(\w+)', lambda match: params[match.group(1)], url)

