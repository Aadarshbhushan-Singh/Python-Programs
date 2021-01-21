mydict = {
    "carl": 40,
    "alan": 2,
    "bob": 1,
    "danny": 3,
}
### with quotation mark
for key in sorted(mydict.keys()):
    print("%s: %s" % (key, mydict[key]))
### without quotation mark
for key in sorted(mydict.keys()):
    print((key, mydict[key]))