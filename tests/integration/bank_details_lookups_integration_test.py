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
def test_bank_details_lookups_create():
    fixture = helpers.load_fixture('bank_details_lookups')['create']
    helpers.stub_response(fixture)
    response = helpers.client.bank_details_lookups.create(*fixture['url_params'])
    body = fixture['body']['bank_details_lookups']

    assert_is_instance(response, resources.BankDetailsLookup)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.available_debit_schemes, body.get('available_debit_schemes'))
    assert_equal(response.bank_name, body.get('bank_name'))
    assert_equal(response.bic, body.get('bic'))

@responses.activate
def test_timeout_bank_details_lookups_create_retries():
    fixture = helpers.load_fixture('bank_details_lookups')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.bank_details_lookups.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['bank_details_lookups']

    assert_is_instance(response, resources.BankDetailsLookup)

def test_502_bank_details_lookups_create_retries():
    fixture = helpers.load_fixture('bank_details_lookups')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.bank_details_lookups.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['bank_details_lookups']

    assert_is_instance(response, resources.BankDetailsLookup)
  
