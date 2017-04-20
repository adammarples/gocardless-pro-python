# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import os
import re
import json

import responses

from contextlib import contextmanager

import gocardless_pro

def load_fixture(resource):
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    fixture_filename = '{0}.json'.format(resource)
    fixture_path = os.path.join(fixtures_path, fixture_filename)
    return json.load(open(fixture_path))

def stub_response(resource_fixture):
    path = re.sub(r':(\w+)', r'\w+', resource_fixture['path_template'])
    url_pattern = re.compile('http://example.com' + path)
    json_body = json.dumps(resource_fixture['body'])
    responses.add(resource_fixture['method'], url_pattern, body=json_body)

def url_pattern_for(resource_fixture):
    path = re.sub(r':(\w+)', r'\w+', resource_fixture['path_template'])
    return re.compile('http://example.com' + path)


@contextmanager
def stub_timeout_then_response(resource_fixture):
    url_pattern = url_pattern_for(resource_fixture)
    json_body = json.dumps(resource_fixture['body'])
    with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
      rsps.add(resource_fixture['method'], url_pattern, status=408)
      rsps.add(resource_fixture['method'], url_pattern, body=json_body)
      yield rsps
    # Will raise 'AssertionError: Not all requests have been executed'
    # if not all of the responses are hit.

@contextmanager
def stub_502_then_response(resource_fixture):
    url_pattern = url_pattern_for(resource_fixture)
    json_body = json.dumps(resource_fixture['body'])
    with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
      rsps.add(resource_fixture['method'], url_pattern, status=502,
               content_type='text/html',
               body='<html><body>Response from Cloudflare</body></html>')
      rsps.add(resource_fixture['method'], url_pattern, body=json_body)
      yield rsps
    # Will raise 'AssertionError: Not all requests have been executed'
    # if not all of the responses are hit.

def idempotency_conflict_body(resource_fixture):

    return {
      'error': {
        'type': 'invalid_state',
        'code': 409,
        'errors': [{
          'message': 'A resource has already been created with this idempotency key',
          'reason': 'idempotent_creation_conflict',
          'links': {
            'conflicting_resource_id': tuple(resource_fixture['body'].values())[0]['id']
          }
        }]
      }
    }


@contextmanager
def stub_timeout_then_idempotecy_conflict(create_fixture, get_fixture):
    create_url_pattern = url_pattern_for(create_fixture)
    get_url_pattern = url_pattern_for(create_fixture)
    error_body = json.dumps(idempotency_conflict_body(create_fixture))
    get_body = json.dumps(get_fixture['body'])
    with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
      rsps.add(create_fixture['method'], create_url_pattern, status=409, body=error_body)
      rsps.add(get_fixture['method'], get_url_pattern, status=200, body=get_body)
      yield rsps

client = gocardless_pro.Client(access_token='secret', base_url='http://example.com')
