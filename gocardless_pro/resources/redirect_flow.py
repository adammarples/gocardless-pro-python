# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class RedirectFlow(object):
    """A thin wrapper around a redirect_flow, providing easy access to its
    attributes.

    Example:
      redirect_flow = client.redirect_flows.get()
      redirect_flow.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def created_at(self):
        return self.attributes.get('created_at')
  

    @property
    def description(self):
        return self.attributes.get('description')
  

    @property
    def id(self):
        return self.attributes.get('id')
  

    @property
    def links(self):
        return self.Links(self.attributes.get('links'))
  

    @property
    def redirect_url(self):
        return self.attributes.get('redirect_url')
  

    @property
    def scheme(self):
        return self.attributes.get('scheme')
  

    @property
    def session_token(self):
        return self.attributes.get('session_token')
  

    @property
    def success_redirect_url(self):
        return self.attributes.get('success_redirect_url')
  


  

  

  

  
    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def creditor(self):
            return self.attributes.get('creditor')
    
        @property
        def customer(self):
            return self.attributes.get('customer')
    
        @property
        def customer_bank_account(self):
            return self.attributes.get('customer_bank_account')
    
        @property
        def mandate(self):
            return self.attributes.get('mandate')
    
  

  

  

  

  

