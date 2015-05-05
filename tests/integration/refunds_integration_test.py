# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import requests
import responses
from nose.tools import assert_equal, assert_is_instance

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

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))

@responses.activate
def test_refunds_list():
    fixture = helpers.load_fixture('refunds')['list']
    helpers.stub_response(fixture)
    response = helpers.client.refunds.list(*fixture['url_params'])
    body = fixture['body']['refunds']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(next(iter(response)), resources.Refund)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

    assert_equal([r.amount for r in response],
                 [b.get('amount') for b in body])
    assert_equal([r.created_at for r in response],
                 [b.get('created_at') for b in body])
    assert_equal([r.currency for r in response],
                 [b.get('currency') for b in body])
    assert_equal([r.id for r in response],
                 [b.get('id') for b in body])
    assert_equal([r.links for r in response],
                 [b.get('links') for b in body])
    assert_equal([r.metadata for r in response],
                 [b.get('metadata') for b in body])

@responses.activate
def test_refunds_get():
    fixture = helpers.load_fixture('refunds')['get']
    helpers.stub_response(fixture)
    response = helpers.client.refunds.get(*fixture['url_params'])
    body = fixture['body']['refunds']

    assert_is_instance(response, resources.Refund)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))

@responses.activate
def test_refunds_update():
    fixture = helpers.load_fixture('refunds')['update']
    helpers.stub_response(fixture)
    response = helpers.client.refunds.update(*fixture['url_params'])
    body = fixture['body']['refunds']

    assert_is_instance(response, resources.Refund)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))

