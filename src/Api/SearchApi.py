import sys
sys.path.append('./src/Client')
from ApiAccessor import ApiAccessor

class AuthorizationApi(ApiAccessor):
    transactionType = ''
    queryString = ''
    __payLoad__ = ''
    
    def __init__(self, payLoad=''):
        self.resourcePath = 'payments/v1/authorizations'
        self.__payLoad__ = payLoad
        self.queryString = 'apikey='

    def search(self, searchId=''):
        if searchId == '':
            self.transactionType = 'post'
        else:
            self.transactionType = 'get'

        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType, self.__payLoad__)

