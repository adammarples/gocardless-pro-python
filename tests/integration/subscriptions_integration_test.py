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
def test_subscriptions_create():
    fixture = helpers.load_fixture('subscriptions')['create']
    helpers.stub_response(fixture)
    response = helpers.client.subscriptions.create(*fixture['url_params'])
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.day_of_month, body.get('day_of_month'))
    assert_equal(response.end_date, body.get('end_date'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.interval, body.get('interval'))
    assert_equal(response.interval_unit, body.get('interval_unit'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.month, body.get('month'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.payment_reference, body.get('payment_reference'))
    assert_equal(response.start_date, body.get('start_date'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.upcoming_payments, body.get('upcoming_payments'))
    assert_equal(response.links.mandate,
                 body.get('links')['mandate'])

def test_timeout_subscriptions_idempotency_conflict():
    create_fixture = helpers.load_fixture('subscriptions')['create']
    get_fixture = helpers.load_fixture('subscriptions')['get']
    with helpers.stub_timeout_then_idempotency_conflict(create_fixture, get_fixture) as rsps:
      response = helpers.client.subscriptions.create(*create_fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      good_response = rsps.calls[1].response

    assert_is_instance(response, resources.Subscription)

def test_timeout_subscriptions_retries():
    fixture = helpers.load_fixture('subscriptions')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.subscriptions.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)

def test_502_subscriptions_retries():
    fixture = helpers.load_fixture('subscriptions')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.subscriptions.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)
  

@responses.activate
def test_subscriptions_list():
    fixture = helpers.load_fixture('subscriptions')['list']
    helpers.stub_response(fixture)
    response = helpers.client.subscriptions.list(*fixture['url_params'])
    body = fixture['body']['subscriptions']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Subscription)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal([r.amount for r in response.records],
                 [b.get('amount') for b in body])
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.currency for r in response.records],
                 [b.get('currency') for b in body])
    assert_equal([r.day_of_month for r in response.records],
                 [b.get('day_of_month') for b in body])
    assert_equal([r.end_date for r in response.records],
                 [b.get('end_date') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.interval for r in response.records],
                 [b.get('interval') for b in body])
    assert_equal([r.interval_unit for r in response.records],
                 [b.get('interval_unit') for b in body])
    assert_equal([r.metadata for r in response.records],
                 [b.get('metadata') for b in body])
    assert_equal([r.month for r in response.records],
                 [b.get('month') for b in body])
    assert_equal([r.name for r in response.records],
                 [b.get('name') for b in body])
    assert_equal([r.payment_reference for r in response.records],
                 [b.get('payment_reference') for b in body])
    assert_equal([r.start_date for r in response.records],
                 [b.get('start_date') for b in body])
    assert_equal([r.status for r in response.records],
                 [b.get('status') for b in body])
    assert_equal([r.upcoming_payments for r in response.records],
                 [b.get('upcoming_payments') for b in body])

def test_timeout_subscriptions_retries():
    fixture = helpers.load_fixture('subscriptions')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.subscriptions.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['subscriptions']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Subscription)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

def test_502_subscriptions_retries():
    fixture = helpers.load_fixture('subscriptions')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.subscriptions.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['subscriptions']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Subscription)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

@responses.activate
def test_subscriptions_all():
    fixture = helpers.load_fixture('subscriptions')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.subscriptions.all())
    assert_equal(len(all_records), len(fixture['body']['subscriptions']) * 2)
    for record in all_records:
      assert_is_instance(record, resources.Subscription)
    
  

@responses.activate
def test_subscriptions_get():
    fixture = helpers.load_fixture('subscriptions')['get']
    helpers.stub_response(fixture)
    response = helpers.client.subscriptions.get(*fixture['url_params'])
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.day_of_month, body.get('day_of_month'))
    assert_equal(response.end_date, body.get('end_date'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.interval, body.get('interval'))
    assert_equal(response.interval_unit, body.get('interval_unit'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.month, body.get('month'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.payment_reference, body.get('payment_reference'))
    assert_equal(response.start_date, body.get('start_date'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.upcoming_payments, body.get('upcoming_payments'))
    assert_equal(response.links.mandate,
                 body.get('links')['mandate'])

def test_timeout_subscriptions_retries():
    fixture = helpers.load_fixture('subscriptions')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.subscriptions.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)

def test_502_subscriptions_retries():
    fixture = helpers.load_fixture('subscriptions')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.subscriptions.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)
  

@responses.activate
def test_subscriptions_update():
    fixture = helpers.load_fixture('subscriptions')['update']
    helpers.stub_response(fixture)
    response = helpers.client.subscriptions.update(*fixture['url_params'])
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.day_of_month, body.get('day_of_month'))
    assert_equal(response.end_date, body.get('end_date'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.interval, body.get('interval'))
    assert_equal(response.interval_unit, body.get('interval_unit'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.month, body.get('month'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.payment_reference, body.get('payment_reference'))
    assert_equal(response.start_date, body.get('start_date'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.upcoming_payments, body.get('upcoming_payments'))
    assert_equal(response.links.mandate,
                 body.get('links')['mandate'])

def test_timeout_subscriptions_retries():
    fixture = helpers.load_fixture('subscriptions')['update']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.subscriptions.update(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)

def test_502_subscriptions_retries():
    fixture = helpers.load_fixture('subscriptions')['update']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.subscriptions.update(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)
  

@responses.activate
def test_subscriptions_cancel():
    fixture = helpers.load_fixture('subscriptions')['cancel']
    helpers.stub_response(fixture)
    response = helpers.client.subscriptions.cancel(*fixture['url_params'])
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.day_of_month, body.get('day_of_month'))
    assert_equal(response.end_date, body.get('end_date'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.interval, body.get('interval'))
    assert_equal(response.interval_unit, body.get('interval_unit'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.month, body.get('month'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.payment_reference, body.get('payment_reference'))
    assert_equal(response.start_date, body.get('start_date'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.upcoming_payments, body.get('upcoming_payments'))
    assert_equal(response.links.mandate,
                 body.get('links')['mandate'])

def test_timeout_subscriptions_doesnt_retry():
    fixture = helpers.load_fixture('subscriptions')['cancel']
    with helpers.stub_timeout(fixture) as rsps:
      try:
        response = helpers.client.subscriptions.cancel(*fixture['url_params'])
      except requests.ConnectTimeout as err:
        pass
      assert_equal(1, len(rsps.calls))

def test_502_subscriptions_doesnt_retry():
    fixture = helpers.load_fixture('subscriptions')['cancel']
    with helpers.stub_502(fixture) as rsps:
      try:
        response = helpers.client.subscriptions.cancel(*fixture['url_params'])
      except MalformedResponseError as err:
        pass
      assert_equal(1, len(rsps.calls))
  
