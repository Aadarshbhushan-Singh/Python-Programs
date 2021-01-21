import re
regularex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #mo=matched object
mo=regularex.search("My phone number is 452-190-1980 call me tomorrow")
print(mo.group())
regularex2=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')  #when an object is placed in parenthesis and bracket us used then the object in bracket becomens optional and works for both 0 and 1.
'''re.compile(r'dinner\?')  note that\? searches for the index and dinner is not optional text '''
mo2=regularex2.search("My phone number is 452-1234 call me tomorrow")
print(mo2.group())

regularex3=re.compile(r'Bat(wo)*man')
mo3=regularex3.search("This is batwowowoman")
print(mo3.group())