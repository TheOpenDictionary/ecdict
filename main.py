import csv

from xml.etree.ElementTree import Element, tostring
from python.odict import Dictionary

root = Element('dictionary')

root.attrib["name"] = "ECDICT"

with open('ecdict.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        m = dict(zip(['word', 'phonetic', 'definition', 'translation', 'pos',
                      'collins', 'oxford', 'tag', 'bnc', 'frq', 'exchange', 'detail', 'audio'], row))

        prn = m['phonetic']
        attr = {'term': m['word']}

        if len(prn) > 0:
            attr['pronunciation'] = prn

        entry = Element("entry", attrib=attr)
        definitions = m['translation'].splitlines()

        print("Processing word %s..." % m['word'])

        ety = Element("ety")
        usage = Element("usage")

        for deff in definitions:
            d = Element("definition")
            d.text = deff
            usage.append(d)

        ety.append(usage)
        entry.append(ety)
        root.append(entry)

    print("Writing dictionary to disk..." % m['word'])
    Dictionary.write(tostring(root).decode('utf-8'), "ecdict.odict")
