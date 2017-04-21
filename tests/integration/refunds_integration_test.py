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
def test_refunds_create():
    fixture = helpers.load_fixture('refunds')['create']
    helpers.stub_response(fixture)
    response = helpers.client.refunds.create(*fixture['url_params'])
    body = fixture['body']['refunds']

    assert_is_instance(response, resources.Refund)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.links.payment,
                 body.get('links')['payment'])

def test_timeout_refunds_idempotency_conflict():
    create_fixture = helpers.load_fixture('refunds')['create']
    get_fixture = helpers.load_fixture('refunds')['get']
    with helpers.stub_timeout_then_idempotency_conflict(create_fixture, get_fixture) as rsps:
      response = helpers.client.refunds.create(*create_fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      good_response = rsps.calls[1].response

    assert_is_instance(response, resources.Refund)

def test_timeout_refunds_retries():
    fixture = helpers.load_fixture('refunds')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.refunds.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['refunds']

    assert_is_instance(response, resources.Refund)

def test_502_refunds_retries():
    fixture = helpers.load_fixture('refunds')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.refunds.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['refunds']

    assert_is_instance(response, resources.Refund)
  

@responses.activate
def test_refunds_list():
    fixture = helpers.load_fixture('refunds')['list']
    helpers.stub_response(fixture)
    response = helpers.client.refunds.list(*fixture['url_params'])
    body = fixture['body']['refunds']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Refund)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal([r.amount for r in response.records],
                 [b.get('amount') for b in body])
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.currency for r in response.records],
                 [b.get('currency') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.metadata for r in response.records],
                 [b.get('metadata') for b in body])
    assert_equal([r.reference for r in response.records],
                 [b.get('reference') for b in body])

def test_timeout_refunds_retries():
    fixture = helpers.load_fixture('refunds')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.refunds.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['refunds']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Refund)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

def test_502_refunds_retries():
    fixture = helpers.load_fixture('refunds')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.refunds.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['refunds']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Refund)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

@responses.activate
def test_refunds_all():
    fixture = helpers.load_fixture('refunds')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.refunds.all())
    assert_equal(len(all_records), len(fixture['body']['refunds']) * 2)
    for record in all_records:
      assert_is_instance(record, resources.Refund)
    
  

@responses.activate
def test_refunds_get():
    fixture = helpers.load_fixture('refunds')['get']
    helpers.stub_response(fixture)
    response = helpers.client.refunds.get(*fixture['url_params'])
    body = fixture['body']['refunds']

    assert_is_instance(response, resources.Refund)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.links.payment,
                 body.get('links')['payment'])

def test_timeout_refunds_retries():
    fixture = helpers.load_fixture('refunds')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.refunds.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['refunds']

    assert_is_instance(response, resources.Refund)

def test_502_refunds_retries():
    fixture = helpers.load_fixture('refunds')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.refunds.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['refunds']

    assert_is_instance(response, resources.Refund)
  

@responses.activate
def test_refunds_update():
    fixture = helpers.load_fixture('refunds')['update']
    helpers.stub_response(fixture)
    response = helpers.client.refunds.update(*fixture['url_params'])
    body = fixture['body']['refunds']

    assert_is_instance(response, resources.Refund)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.links.payment,
                 body.get('links')['payment'])

def test_timeout_refunds_retries():
    fixture = helpers.load_fixture('refunds')['update']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.refunds.update(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['refunds']

    assert_is_instance(response, resources.Refund)

def test_502_refunds_retries():
    fixture = helpers.load_fixture('refunds')['update']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.refunds.update(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['refunds']

    assert_is_instance(response, resources.Refund)
  
