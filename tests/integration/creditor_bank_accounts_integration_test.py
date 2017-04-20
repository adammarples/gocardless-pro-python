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

from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_creditor_bank_accounts_create():
    fixture = helpers.load_fixture('creditor_bank_accounts')['create']
    helpers.stub_response(fixture)
    response = helpers.client.creditor_bank_accounts.create(*fixture['url_params'])
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, resources.CreditorBankAccount)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.account_holder_name, body.get('account_holder_name'))
    assert_equal(response.account_number_ending, body.get('account_number_ending'))
    assert_equal(response.bank_name, body.get('bank_name'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.enabled, body.get('enabled'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])

def test_timeout_creditor_bank_accounts_idempotency_conflict():
    create_fixture = helpers.load_fixture('creditor_bank_accounts')['create']
    get_fixture = helpers.load_fixture('creditor_bank_accounts')['get']
    with helpers.stub_timeout_then_idempotecy_conflict(create_fixture, get_fixture) as rsps:
      response = helpers.client.creditor_bank_accounts.create(*create_fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      good_response = rsps.calls[1].response

    assert_is_instance(response, resources.CreditorBankAccount)

def test_timeout_creditor_bank_accounts_retries():
    fixture = helpers.load_fixture('creditor_bank_accounts')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.creditor_bank_accounts.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, resources.CreditorBankAccount)

def test_502_creditor_bank_accounts_retries():
    fixture = helpers.load_fixture('creditor_bank_accounts')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.creditor_bank_accounts.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, resources.CreditorBankAccount)
  

@responses.activate
def test_creditor_bank_accounts_list():
    fixture = helpers.load_fixture('creditor_bank_accounts')['list']
    helpers.stub_response(fixture)
    response = helpers.client.creditor_bank_accounts.list(*fixture['url_params'])
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.CreditorBankAccount)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal([r.account_holder_name for r in response.records],
                 [b.get('account_holder_name') for b in body])
    assert_equal([r.account_number_ending for r in response.records],
                 [b.get('account_number_ending') for b in body])
    assert_equal([r.bank_name for r in response.records],
                 [b.get('bank_name') for b in body])
    assert_equal([r.country_code for r in response.records],
                 [b.get('country_code') for b in body])
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.currency for r in response.records],
                 [b.get('currency') for b in body])
    assert_equal([r.enabled for r in response.records],
                 [b.get('enabled') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.metadata for r in response.records],
                 [b.get('metadata') for b in body])

def test_timeout_creditor_bank_accounts_retries():
    fixture = helpers.load_fixture('creditor_bank_accounts')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.creditor_bank_accounts.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.CreditorBankAccount)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

def test_502_creditor_bank_accounts_retries():
    fixture = helpers.load_fixture('creditor_bank_accounts')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.creditor_bank_accounts.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.CreditorBankAccount)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

@responses.activate
def test_creditor_bank_accounts_all():
    fixture = helpers.load_fixture('creditor_bank_accounts')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.creditor_bank_accounts.all())
    assert_equal(len(all_records), len(fixture['body']['creditor_bank_accounts']) * 2)
    for record in all_records:
      assert_is_instance(record, resources.CreditorBankAccount)
    
  

@responses.activate
def test_creditor_bank_accounts_get():
    fixture = helpers.load_fixture('creditor_bank_accounts')['get']
    helpers.stub_response(fixture)
    response = helpers.client.creditor_bank_accounts.get(*fixture['url_params'])
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, resources.CreditorBankAccount)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.account_holder_name, body.get('account_holder_name'))
    assert_equal(response.account_number_ending, body.get('account_number_ending'))
    assert_equal(response.bank_name, body.get('bank_name'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.enabled, body.get('enabled'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])

def test_timeout_creditor_bank_accounts_retries():
    fixture = helpers.load_fixture('creditor_bank_accounts')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.creditor_bank_accounts.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, resources.CreditorBankAccount)

def test_502_creditor_bank_accounts_retries():
    fixture = helpers.load_fixture('creditor_bank_accounts')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.creditor_bank_accounts.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, resources.CreditorBankAccount)
  

@responses.activate
def test_creditor_bank_accounts_disable():
    fixture = helpers.load_fixture('creditor_bank_accounts')['disable']
    helpers.stub_response(fixture)
    response = helpers.client.creditor_bank_accounts.disable(*fixture['url_params'])
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, resources.CreditorBankAccount)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.account_holder_name, body.get('account_holder_name'))
    assert_equal(response.account_number_ending, body.get('account_number_ending'))
    assert_equal(response.bank_name, body.get('bank_name'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.enabled, body.get('enabled'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])

def test_timeout_creditor_bank_accounts_doesnt_retry():
    fixture = helpers.load_fixture('creditor_bank_accounts')['disable']
    with assert_raises(AssertionError):
      with helpers.stub_timeout_then_response(fixture) as rsps:
        try:
          response = helpers.client.creditor_bank_accounts.disable(*fixture['url_params'])
        except Exception:
          pass
        assert_equal(1, len(rsps.calls))

def test_502_creditor_bank_accounts_doesnt_retry():
    fixture = helpers.load_fixture('creditor_bank_accounts')['disable']
    with assert_raises(AssertionError):
      with helpers.stub_502_then_response(fixture) as rsps:
        try:
          response = helpers.client.creditor_bank_accounts.disable(*fixture['url_params'])
        except Exception:
          pass
        assert_equal(1, len(rsps.calls))
  
