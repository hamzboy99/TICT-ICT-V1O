import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse((filestring))
        return xmldictionary

artikelendict = processXML('artikelen.xml')
artikelen = artikelendict['artikelen']['artikel']

for artikel in artikelen:
    print(artikel['naam'])
