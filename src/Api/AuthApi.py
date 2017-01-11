import sys
sys.path.append('../src/Client')
from ApiAccessor import ApiAccessor

class AuthorizationApi(ApiAccessor):
    transactionType = ''
    queryString = ''
    __payLoad__ = ''
    
    def __init__(self, payLoad):
        self.resourcePath = 'payments/v1/authorizations'
        self.__payLoad__ = payLoad
        self.queryString = 'apikey='

    def auth(self):
        self.transactionType = 'post'
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType, self.__payLoad__)

    def reversal(self, authId):
        self.transactionType = 'post'
        self.resourcePath += authId + '/reversals'
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType, self.__payLoad__)

    def retrieve(self, authId):
        self.transactionType = 'get'
        self.resourcePath += authId
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType)
