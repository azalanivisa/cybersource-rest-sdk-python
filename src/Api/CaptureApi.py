import sys
sys.path.append('../src/Client')
from ApiAccessor import ApiAccessor

class CaptureApi(ApiAccessor):
    transactionType = ''
    queryString = ''
    __payLoad__ = ''
    
    def __init__(self, payLoad=''):
        self.resourcePath = 'payments/v1/'
        self.__payLoad__ = payLoad
        self.queryString = 'apikey='

    def capture(self, authId):
        self.transactionType = 'post'
        self.resourcePath += 'authorizations/' + authId + '/captures'
        print(self.resourcePath)
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType, self.__payLoad__)

    def refund(self, captureId):
        self.transactionType = 'post'
        self.resourcePath += 'captures/' + captureId + '/refunds'
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType, self.__payLoad__)

    def void(self, captureId):
        self.transactionType = 'post'
        self.resourcePath += 'captures' + captureId + '/voids'
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType, self.__payLoad__)

    def retrieve(self, captureId):
        self.transactionType = 'get'
        self.resourcePath += 'captures' + captureId
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType)

    def retrieveByAuthId(self, authId):
        self.transactionType = 'get'
        self.resourcePath += 'authorizations' + authId + '/captures'
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType)
