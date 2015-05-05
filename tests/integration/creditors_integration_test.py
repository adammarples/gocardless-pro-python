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
def test_creditors_create():
    fixture = helpers.load_fixture('creditors')['create']
    helpers.stub_response(fixture)
    response = helpers.client.creditors.create(*fixture['url_params'])
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)

    assert_equal(response.address_line1, body.get('address_line1'))
    assert_equal(response.address_line2, body.get('address_line2'))
    assert_equal(response.address_line3, body.get('address_line3'))
    assert_equal(response.city, body.get('city'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.postal_code, body.get('postal_code'))
    assert_equal(response.region, body.get('region'))

@responses.activate
def test_creditors_list():
    fixture = helpers.load_fixture('creditors')['list']
    helpers.stub_response(fixture)
    response = helpers.client.creditors.list(*fixture['url_params'])
    body = fixture['body']['creditors']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(next(iter(response)), resources.Creditor)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

    assert_equal([r.address_line1 for r in response],
                 [b.get('address_line1') for b in body])
    assert_equal([r.address_line2 for r in response],
                 [b.get('address_line2') for b in body])
    assert_equal([r.address_line3 for r in response],
                 [b.get('address_line3') for b in body])
    assert_equal([r.city for r in response],
                 [b.get('city') for b in body])
    assert_equal([r.country_code for r in response],
                 [b.get('country_code') for b in body])
    assert_equal([r.created_at for r in response],
                 [b.get('created_at') for b in body])
    assert_equal([r.id for r in response],
                 [b.get('id') for b in body])
    assert_equal([r.links for r in response],
                 [b.get('links') for b in body])
    assert_equal([r.name for r in response],
                 [b.get('name') for b in body])
    assert_equal([r.postal_code for r in response],
                 [b.get('postal_code') for b in body])
    assert_equal([r.region for r in response],
                 [b.get('region') for b in body])

@responses.activate
def test_creditors_get():
    fixture = helpers.load_fixture('creditors')['get']
    helpers.stub_response(fixture)
    response = helpers.client.creditors.get(*fixture['url_params'])
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)

    assert_equal(response.address_line1, body.get('address_line1'))
    assert_equal(response.address_line2, body.get('address_line2'))
    assert_equal(response.address_line3, body.get('address_line3'))
    assert_equal(response.city, body.get('city'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.postal_code, body.get('postal_code'))
    assert_equal(response.region, body.get('region'))

@responses.activate
def test_creditors_update():
    fixture = helpers.load_fixture('creditors')['update']
    helpers.stub_response(fixture)
    response = helpers.client.creditors.update(*fixture['url_params'])
    body = fixture['body']['creditors']

    assert_is_instance(response, resources.Creditor)

    assert_equal(response.address_line1, body.get('address_line1'))
    assert_equal(response.address_line2, body.get('address_line2'))
    assert_equal(response.address_line3, body.get('address_line3'))
    assert_equal(response.city, body.get('city'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.postal_code, body.get('postal_code'))
    assert_equal(response.region, body.get('region'))

