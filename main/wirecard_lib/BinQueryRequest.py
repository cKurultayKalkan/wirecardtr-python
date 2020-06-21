from main.wirecard_lib.Helper import Helper, HttpClient
from main.wirecard_lib.configs import Configs
from xml.etree.ElementTree import Element, SubElement, tostring


class BinQueryRequest:
    ServiceType = ""
    OperationType = ""
    Token = ""
    BIN = ""

    def execute(self, req, configs):
        helper = Helper()
        result = HttpClient.post(configs.BaseUrl, self.convert_to_xml(req))
        return result

    def convert_to_xml(self, req):
        main_root = Element('WIRECARD')
        ServiceType = SubElement(main_root, 'ServiceType')
        ServiceType.text = req.ServiceType
        OperationType = SubElement(main_root, 'OperationType')
        OperationType.text = req.OperationType
        token_root = SubElement(main_root, 'Token')
        UserCode = SubElement(token_root, 'UserCode')
        UserCode.text = req.Token.UserCode
        Pin = SubElement(token_root, 'Pin')
        Pin.text = req.Token.Pin
        BIN = SubElement(main_root, 'BIN')
        BIN.text = req.BIN

        result = tostring(main_root).decode('ISO-8859-9')
        return (result)
