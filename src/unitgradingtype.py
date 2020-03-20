import xml.etree.ElementTree as ET

class Unitgradingtype(ET.Element):

    def __init__(self, text):
        super(Unitgradingtype, self).__init__('unitgradingtype')

        self.text = text
