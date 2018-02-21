import urllib.request

u = urllib.request.urlopen('http://www.webservicex.com/globalweather.asmx?WSDL')
data = u.read()

from xml.etree.ElementTree import XML
doc = XML(data)

for pt in doc.findall('.//element'):
	print(pt.text)

