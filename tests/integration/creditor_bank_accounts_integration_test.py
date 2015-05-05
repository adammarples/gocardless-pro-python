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
def test_creditor_bank_accounts_create():
    fixture = helpers.load_fixture('creditor_bank_accounts')['create']
    helpers.stub_response(fixture)
    response = helpers.client.creditor_bank_accounts.create(*fixture['url_params'])
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, resources.CreditorBankAccount)

    assert_equal(response.account_holder_name, body.get('account_holder_name'))
    assert_equal(response.account_number_ending, body.get('account_number_ending'))
    assert_equal(response.bank_name, body.get('bank_name'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.enabled, body.get('enabled'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))

@responses.activate
def test_creditor_bank_accounts_list():
    fixture = helpers.load_fixture('creditor_bank_accounts')['list']
    helpers.stub_response(fixture)
    response = helpers.client.creditor_bank_accounts.list(*fixture['url_params'])
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(next(iter(response)), resources.CreditorBankAccount)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

    assert_equal([r.account_holder_name for r in response],
                 [b.get('account_holder_name') for b in body])
    assert_equal([r.account_number_ending for r in response],
                 [b.get('account_number_ending') for b in body])
    assert_equal([r.bank_name for r in response],
                 [b.get('bank_name') for b in body])
    assert_equal([r.country_code for r in response],
                 [b.get('country_code') for b in body])
    assert_equal([r.created_at for r in response],
                 [b.get('created_at') for b in body])
    assert_equal([r.currency for r in response],
                 [b.get('currency') for b in body])
    assert_equal([r.enabled for r in response],
                 [b.get('enabled') for b in body])
    assert_equal([r.id for r in response],
                 [b.get('id') for b in body])
    assert_equal([r.links for r in response],
                 [b.get('links') for b in body])
    assert_equal([r.metadata for r in response],
                 [b.get('metadata') for b in body])

@responses.activate
def test_creditor_bank_accounts_get():
    fixture = helpers.load_fixture('creditor_bank_accounts')['get']
    helpers.stub_response(fixture)
    response = helpers.client.creditor_bank_accounts.get(*fixture['url_params'])
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, resources.CreditorBankAccount)

    assert_equal(response.account_holder_name, body.get('account_holder_name'))
    assert_equal(response.account_number_ending, body.get('account_number_ending'))
    assert_equal(response.bank_name, body.get('bank_name'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.enabled, body.get('enabled'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))

@responses.activate
def test_creditor_bank_accounts_disable():
    fixture = helpers.load_fixture('creditor_bank_accounts')['disable']
    helpers.stub_response(fixture)
    response = helpers.client.creditor_bank_accounts.disable(*fixture['url_params'])
    body = fixture['body']['creditor_bank_accounts']

    assert_is_instance(response, resources.CreditorBankAccount)

    assert_equal(response.account_holder_name, body.get('account_holder_name'))
    assert_equal(response.account_number_ending, body.get('account_number_ending'))
    assert_equal(response.bank_name, body.get('bank_name'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.enabled, body.get('enabled'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))

