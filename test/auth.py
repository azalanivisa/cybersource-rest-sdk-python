import json
import sys
sys.path.append('../src/Api')
from AuthApi import AuthorizationApi 

import os
import unittest
if sys.version_info < (3, 0):
    import ConfigParser as parser
else:
    import configparser as parser

class TestCybersourcePayment(unittest.TestCase):
    
    config = parser.ConfigParser()
    config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'../','configuration.ini'))
    config.read(config_path)

    def setUp(self):
        self.paymentAuthorizationRequest = ''
        with open(sys.argv[1],'r') as authPayLoad:
            self.paymentAuthorizationRequest = json.loads(authPayLoad.read())
        self.visa_api_client = AuthorizationApi(self.paymentAuthorizationRequest)
    
    def test_cybersource_payment_authorization(self):
        query_string = 'apikey=' + self.config.get('VDP','apiKey')
        try:
            response = self.visa_api_client.auth()
            print("transaction successful")
        except Exception as e:
            print("transaction failed!!")
            print(e.args)

if __name__=="__main__":
    test = TestCybersourcePayment()
    test.setUp()
    test.test_cybersource_payment_authorization()
