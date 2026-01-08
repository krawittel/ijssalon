mijn_dictionary = {
    "voornaam :" : "harry",
    "geboortedatum :" : "31-maart-1939",
    "registratienummer :" : "AA18891"
}
del mijn_dictionary["geboortedatum :"] 
print()
for k,v in mijn_dictionary.items():
    print (k,v)
