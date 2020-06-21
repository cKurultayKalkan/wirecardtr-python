from zeep import Client


# TransactionQueryByOrderRequest Soap Servis çağrısının yapıldığı alanı temsil eder.
# Soap çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
class TransactionQueryByOrderRequest:
    def execute(self, token, inputrequest):
        client = Client('https://www.wirecard.com.tr/services/saleservice.asmx?WSDL')
        result = client.service.GetSaleResult(vars(token), inputrequest.orderId)
        return result
