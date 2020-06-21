import hashlib
import datetime
import base64
import requests
import xml.dom.minidom as MND


class Helper(object):

    @staticmethod
    def formatXML(input):
        doc = MND.parseString(input)
        output = doc.toprettyxml(indent="\t", newl="\n", encoding="utf-8").decode('UTF-8')
        return output

    def ComputeHash(hashString):
        encoded = hashlib.sha1(hashString.encode('ISO-8859-9')).digest()
        encoded = base64.b64encode(encoded)
        return encoded.decode('ISO-8859-9')


class HttpClient(object):
    # Xml çağrılarını Url bilgisi ve xml metinleri ile birlikte belirtilen url adresine post edilmesini sağlar.
    @staticmethod
    def post(url, content):
        print("----IN HTTP POST----")
        print("URL: ", url)
        print("DATA:", content)
        client = requests.post(url, content, verify=False)
        return client.text
