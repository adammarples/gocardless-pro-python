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
def test_mandates_create():
    fixture = helpers.load_fixture('mandates')['create']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.create(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.next_possible_charge_date, body.get('next_possible_charge_date'))
    assert_equal(response.payments_require_approval, body.get('payments_require_approval'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.new_mandate,
                 body.get('links')['new_mandate'])

def test_timeout_mandates_idempotency_conflict():
    create_fixture = helpers.load_fixture('mandates')['create']
    get_fixture = helpers.load_fixture('mandates')['get']
    with helpers.stub_timeout_then_idempotency_conflict(create_fixture, get_fixture) as rsps:
      response = helpers.client.mandates.create(*create_fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      good_response = rsps.calls[1].response

    assert_is_instance(response, resources.Mandate)

def test_timeout_mandates_retries():
    fixture = helpers.load_fixture('mandates')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.mandates.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)

def test_502_mandates_retries():
    fixture = helpers.load_fixture('mandates')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.mandates.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)
  

@responses.activate
def test_mandates_list():
    fixture = helpers.load_fixture('mandates')['list']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.list(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Mandate)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.metadata for r in response.records],
                 [b.get('metadata') for b in body])
    assert_equal([r.next_possible_charge_date for r in response.records],
                 [b.get('next_possible_charge_date') for b in body])
    assert_equal([r.payments_require_approval for r in response.records],
                 [b.get('payments_require_approval') for b in body])
    assert_equal([r.reference for r in response.records],
                 [b.get('reference') for b in body])
    assert_equal([r.scheme for r in response.records],
                 [b.get('scheme') for b in body])
    assert_equal([r.status for r in response.records],
                 [b.get('status') for b in body])

def test_timeout_mandates_retries():
    fixture = helpers.load_fixture('mandates')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.mandates.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['mandates']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Mandate)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

def test_502_mandates_retries():
    fixture = helpers.load_fixture('mandates')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.mandates.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['mandates']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Mandate)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

@responses.activate
def test_mandates_all():
    fixture = helpers.load_fixture('mandates')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.mandates.all())
    assert_equal(len(all_records), len(fixture['body']['mandates']) * 2)
    for record in all_records:
      assert_is_instance(record, resources.Mandate)
    
  

@responses.activate
def test_mandates_get():
    fixture = helpers.load_fixture('mandates')['get']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.get(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.next_possible_charge_date, body.get('next_possible_charge_date'))
    assert_equal(response.payments_require_approval, body.get('payments_require_approval'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.new_mandate,
                 body.get('links')['new_mandate'])

def test_timeout_mandates_retries():
    fixture = helpers.load_fixture('mandates')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.mandates.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)

def test_502_mandates_retries():
    fixture = helpers.load_fixture('mandates')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.mandates.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)
  

@responses.activate
def test_mandates_update():
    fixture = helpers.load_fixture('mandates')['update']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.update(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.next_possible_charge_date, body.get('next_possible_charge_date'))
    assert_equal(response.payments_require_approval, body.get('payments_require_approval'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.new_mandate,
                 body.get('links')['new_mandate'])

def test_timeout_mandates_retries():
    fixture = helpers.load_fixture('mandates')['update']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.mandates.update(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)

def test_502_mandates_retries():
    fixture = helpers.load_fixture('mandates')['update']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.mandates.update(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)
  

@responses.activate
def test_mandates_cancel():
    fixture = helpers.load_fixture('mandates')['cancel']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.cancel(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.next_possible_charge_date, body.get('next_possible_charge_date'))
    assert_equal(response.payments_require_approval, body.get('payments_require_approval'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.new_mandate,
                 body.get('links')['new_mandate'])

def test_timeout_mandates_doesnt_retry():
    fixture = helpers.load_fixture('mandates')['cancel']
    with assert_raises(AssertionError):
      with helpers.stub_timeout_then_response(fixture) as rsps:
        try:
          response = helpers.client.mandates.cancel(*fixture['url_params'])
        except Exception:
          pass
        assert_equal(1, len(rsps.calls))

def test_502_mandates_doesnt_retry():
    fixture = helpers.load_fixture('mandates')['cancel']
    with assert_raises(AssertionError):
      with helpers.stub_502_then_response(fixture) as rsps:
        try:
          response = helpers.client.mandates.cancel(*fixture['url_params'])
        except Exception:
          pass
        assert_equal(1, len(rsps.calls))
  

@responses.activate
def test_mandates_reinstate():
    fixture = helpers.load_fixture('mandates')['reinstate']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.reinstate(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.next_possible_charge_date, body.get('next_possible_charge_date'))
    assert_equal(response.payments_require_approval, body.get('payments_require_approval'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.customer_bank_account,
                 body.get('links')['customer_bank_account'])
    assert_equal(response.links.new_mandate,
                 body.get('links')['new_mandate'])

def test_timeout_mandates_doesnt_retry():
    fixture = helpers.load_fixture('mandates')['reinstate']
    with assert_raises(AssertionError):
      with helpers.stub_timeout_then_response(fixture) as rsps:
        try:
          response = helpers.client.mandates.reinstate(*fixture['url_params'])
        except Exception:
          pass
        assert_equal(1, len(rsps.calls))

def test_502_mandates_doesnt_retry():
    fixture = helpers.load_fixture('mandates')['reinstate']
    with assert_raises(AssertionError):
      with helpers.stub_502_then_response(fixture) as rsps:
        try:
          response = helpers.client.mandates.reinstate(*fixture['url_params'])
        except Exception:
          pass
        assert_equal(1, len(rsps.calls))
  
