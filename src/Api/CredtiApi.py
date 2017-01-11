import sys
sys.path.append('../src/Client')
from ApiAccessor import ApiAccessor

class CreditApi(ApiAccessor):
    transactionType = ''
    queryString = ''
    __payLoad__ = ''
    
    def __init__(self, payLoad):
        self.resourcePath = 'payments/v1/credits'
        self.__payLoad__ = payLoad
        self.queryString = 'apikey='

    def credit(self):
        self.transactionType = 'post'
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType, self.__payLoad__)

    def void(self, creditId):
        self.transactionType = 'post'
        self.resourcePath += captureId + '/voids'
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType, self.__payLoad__)

    def retrieve(self, creditId):
        self.transactionType = 'get'
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType)

