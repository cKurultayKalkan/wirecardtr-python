from main.wirecard_lib.Helper import Helper, HttpClient
from main.wirecard_lib.configs import Configs
from xml.etree.ElementTree import Element, SubElement, tostring


# MarketPlaceCreateSubPartnerRequest Xml  çağrısının yapıldığı alanı temsil eder.
# Xml çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
# İstenen Xml metni convert_to_xml metodu sayesinde oluşturulur.
class MarketPlaceCreateSubPartnerRequest:
    ServiceType = ""
    OperationType = ""
    Token = ""
    UniqueId = ""
    SubPartnerType = ""

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
        UniqueId = SubElement(main_root, 'UniqueId')
        UniqueId.text = req.UniqueId
        SubPartnerType = SubElement(main_root, 'SubPartnerType')
        SubPartnerType.text = req.SubPartnerType

        result = tostring(main_root).decode('utf-8')
        return (result)
