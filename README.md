# Python Module for REST API calls
## Installing the SDK 
1. Download the cybersource-rest-sdk-python-master.zip package into a directory of your choice. 
2. Extract and go to the cybersource-rest-sdk-python-master directory.
3. To install the package and the required dependencies run the following command:
            $ python setup.py install 

## Usage

1. Register on VDP (Visa Developer Platform) (hyperlink to “https://developer.visa.com/”).

2. Create an application on VDP. Make sure “CyberSource Payment API” is checked before creating the application.

3. Payload has to be in the form of a json file. Mention path of the payload file in configuration.ini.

4. Put API key and Shared Sercet in app.config. For more information on configuration.ini refer : Manual . CyberSource Payment API uses X-Pay-Token authentication method in the manual.

5. Run the samples using the following command:
   $ python sampleTransaction.py payloadPath 
