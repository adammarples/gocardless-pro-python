# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import requests
import responses
from nose.tools import (
  assert_equal,
  assert_is_instance,
  assert_is_none,
  assert_is_not_none,
  assert_raises
)

from gocardless_pro.errors import MalformedResponseError
from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_mandate_pdfs_create():
    fixture = helpers.load_fixture('mandate_pdfs')['create']
    helpers.stub_response(fixture)
    response = helpers.client.mandate_pdfs.create(*fixture['url_params'])
    body = fixture['body']['mandate_pdfs']

    assert_is_instance(response, resources.MandatePdf)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.expires_at, body.get('expires_at'))
    assert_equal(response.url, body.get('url'))

@responses.activate
def test_timeout_mandate_pdfs_create_retries():
    fixture = helpers.load_fixture('mandate_pdfs')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.mandate_pdfs.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['mandate_pdfs']

    assert_is_instance(response, resources.MandatePdf)

def test_502_mandate_pdfs_create_retries():
    fixture = helpers.load_fixture('mandate_pdfs')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.mandate_pdfs.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['mandate_pdfs']

    assert_is_instance(response, resources.MandatePdf)
  
