from main.wirecard_lib.Helper import Helper, HttpClient
from main.wirecard_lib.configs import Configs
from xml.etree.ElementTree import Element, SubElement, tostring


# MarketPlaceWdticketMpsale3dSecureRequest Xml  çağrısının yapıldığı alanı temsil eder.
# Xml çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
# İstenen Xml metni convert_to_xml metodu sayesinde oluşturulur.
class MarketPlaceWdticketMpsale3dSecureRequest:
    ServiceType = ""
    OperationType = ""
    Token = ""
    MPAY = ""
    ExtraParam = ""
    Description = ""
    ErrorURL = ""
    SuccessURL = ""
    CommissionRate = ""
    InstallmentOptions = ""
    CommissionRateList = ""
    Price = ""
    SubPartnerId = ""
    PaymentContent = ""

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
        MPAY = SubElement(main_root, 'MPAY')
        MPAY.text = req.MPAY
        ExtraParam = SubElement(main_root, 'ExtraParam')
        ExtraParam.text = req.ExtraParam
        Description = SubElement(main_root, 'Description')
        Description.text = req.Description

        ErrorURL = SubElement(main_root, 'ErrorURL')
        ErrorURL.text = req.ErrorURL
        SuccessURL = SubElement(main_root, 'SuccessURL')
        SuccessURL.text = req.SuccessURL

        CommissionRate = SubElement(main_root, 'CommissionRate')
        CommissionRate.text = req.CommissionRate
        InstallmentOptions = SubElement(main_root, 'InstallmentOptions')
        InstallmentOptions.text = req.InstallmentOptions

        commissionRateList_root = SubElement(main_root, 'CommissionRateList')
        Inst0 = SubElement(commissionRateList_root, 'Inst0')
        Inst0.text = req.CommissionRateList.Inst0
        Inst3 = SubElement(commissionRateList_root, 'Inst3')
        Inst3.text = req.CommissionRateList.Inst3
        Inst6 = SubElement(commissionRateList_root, 'Inst6')
        Inst6.text = req.CommissionRateList.Inst6
        Inst9 = SubElement(commissionRateList_root, 'Inst9')
        Inst9.text = req.CommissionRateList.Inst9

        Price = SubElement(main_root, 'Price')
        Price.text = req.Price
        SubPartnerId = SubElement(main_root, 'SubPartnerId')
        SubPartnerId.text = req.SubPartnerId
        PaymentContent = SubElement(main_root, 'PaymentContent')
        PaymentContent.text = req.PaymentContent

        token_root = SubElement(main_root, 'Token')
        UserCode = SubElement(token_root, 'UserCode')
        UserCode.text = req.Token.UserCode
        Pin = SubElement(token_root, 'Pin')
        Pin.text = req.Token.Pin

        result = tostring(main_root).decode('utf-8')
        return (result)
