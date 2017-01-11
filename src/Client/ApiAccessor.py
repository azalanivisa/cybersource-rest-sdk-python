import ApiClient

class ApiAccessor:
    baseUri = 'cybersource/' 
    def runTransaction(self, resourcePath, queryString, transactionType, payLoad=''):
        return ApiClient.CybersourceApiClient().do_x_pay_request(self.baseUri, resourcePath, queryString, payLoad, 'Cybersource Payments Test', transactionType)
