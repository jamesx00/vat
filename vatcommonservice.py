import urllib3
import sys
import zeep

from requests import Session
from zeep import Client
from zeep.transports import Transport


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":

    session = Session()
    session.verify = False
    transport = Transport(session=session)

    client = Client(
        "https://rdws.rd.go.th/serviceRD3/commonserviceRD3.asmx?wsdl",
        transport=transport,
    )

    result = client.service.Service(
        username="anonymous",
        password="anonymous",
        typeofservice="VATCommonService",
    )

    # Convert Zeep Response object (in this case Service) to Python dict.
    result = zeep.helpers.serialize_object(result)
    print(result)
    # for k in result.keys():
    #     # print(k, result[k])
    #     if result[k] is not None:
    #         v = result[k].get("anyType", None)[0]
    #         print(k, v)
