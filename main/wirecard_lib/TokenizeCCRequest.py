from main.wirecard_lib.Helper import Helper, HttpClient
from main.wirecard_lib.configs import Configs
from xml.etree.ElementTree import Element, SubElement, tostring


# TokenizeCCRequest Xml  çağrısının yapıldığı alanı temsil eder.
# Xml çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
# İstenen Xml metni convert_to_xml metodu sayesinde oluşturulur.
class TokenizeCCRequest:
    ServiceType = ""
    OperationType = ""
    Token = ""
    CreditCardNumber = ""
    NameSurname = ""
    ExpiryDate = ""
    CVV = ""
    CustomerId = ""
    ValidityPeriod = ""
    IPAddress = ""
    Port = ""

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

        CreditCardNumber = SubElement(main_root, 'CreditCardNumber')
        CreditCardNumber.text = req.CreditCardNumber

        NameSurname = SubElement(main_root, 'NameSurname')
        NameSurname.text = req.NameSurname

        ExpiryDate = SubElement(main_root, 'ExpiryDate')
        ExpiryDate.text = req.ExpiryDate

        CVV = SubElement(main_root, 'CVV')
        CVV.text = req.CVV
        CustomerId = SubElement(main_root, 'CustomerId')
        CustomerId.text = req.CustomerId
        ValidityPeriod = SubElement(main_root, 'ValidityPeriod')
        ValidityPeriod.text = req.ValidityPeriod
        Port = SubElement(main_root, 'Port')
        Port.text = req.Port
        IPAddress = SubElement(main_root, 'IPAddress')
        IPAddress.text = req.IPAddress

        result = tostring(main_root).decode('utf-8')
        return (result)
