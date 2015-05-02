# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources

class HelpersService(base_service.BaseService):
    """Service class that provides access to the helpers
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.Helper
    RESOURCE_NAME = 'helpers'

    def mandate(self, params=None):
        """Mandate PDF.

        Returns a PDF mandate form with a signature field, ready to be signed
        by your customer. May be fully or partially pre-filled.
        
      
         You must specify `Accept: application/pdf` on requests to this
        endpoint.
        
        Bank account details may either be supplied
        using the IBAN (international bank account number), or [local
        details](https://developer.gocardless.com/pro/2015-04-29/#ui-compliance-local-bank-details).
        For more information on the different fields required in each country,
        please see the [local bank
        details](https://developer.gocardless.com/pro/2015-04-29/#ui-compliance-local-bank-details)
        section.
        
        To generate a mandate in a foreign language,
        set your `Accept-Language` header to the relevant [ISO
        639-1](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes#Partial_ISO_639_table)
        language code. Currently Dutch, English, French, German, Italian,
        Portuguese and Spanish are supported.
        
        _Note:_ If you
        want to render a PDF of an existing mandate you can also do so using
        the [mandate show
        endpoint](https://developer.gocardless.com/pro/2015-04-29/#mandates-get-a-single-mandate).

        Args:
          params (dict, optional): Request body.

        Returns:
          Helper
        """
        path = '/helpers/mandate'
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

    def modulus_check(self, params=None):
        """Modulus checking.

        Check whether an account number and bank / branch code combination are
        compatible.
        
        Bank account details may either be
        supplied using the IBAN (international bank account number), or [local
        details](https://developer.gocardless.com/pro/2015-04-29/#ui-compliance-local-bank-details).
        For more information on the different fields required in each country,
        please see the [local bank
        details](https://developer.gocardless.com/pro/2015-04-29/#ui-compliance-local-bank-details)
        section.

        Args:
          params (dict, optional): Request body.

        Returns:
          Helper
        """
        path = '/helpers/modulus_check'
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

