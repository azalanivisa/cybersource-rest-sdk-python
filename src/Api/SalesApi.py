import sys
sys.path.append('../src/Client')
from ApiAccessor import ApiAccessor

class SalesApi(ApiAccessor):
    transactionUri = ''
    transactionType = 'post'
    queryString = ''
    __payLoad__ = ''
    __salesId__ = ''
    
    def __init__(self, payLoad=''):
        self.resourcePath = 'payments/v1/sales'
        self.__payLoad__ = payLoad
        self.queryString = 'apikey='

    def sale(self):
        self.transactionType = 'post'
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType, self.__payLoad__)

    def refund(self, salesId):
        self.transactionType = 'post'
        self.resourcePath += salesId + '/refunds'
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType, self.__payLoad__)

    def void(self, salesId):
        self.transactionType = 'post'
        self.resourcePath += salesId + '/voids'
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType, self.__payLoad__)

    def search(self, salesId):
        self.transactionType = 'get'
        self.resourcePath += salesId
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType)
