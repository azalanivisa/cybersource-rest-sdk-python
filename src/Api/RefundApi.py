import sys
sys.path.append('./src/Client')
from ApiAccessor import ApiAccessor

class RefundApi(ApiAccessor):
    transactionType = ''
    queryString = ''
    __payLoad__ = ''
    
    def __init__(self, payLoad):
        self.resourcePath = 'payments/v1/refunds'
        self.__payLoad__ = payLoad
        self.queryString = 'apikey='

    def retrieve(self, refundId):
        self.transactionType = 'get'
        self.resourcePath += refundId
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType)

    def retrievebyCaptureId(self, captureId):
        self.transactionType = 'get'
        self.resourcePath += captureId
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType)

    def retrievebySalesId(self, salesId):
        self.transactionType = 'get'
        self.resourcePath += salesId
        return super().runTransaction(self.resourcePath, self.queryString, self.transactionType)
