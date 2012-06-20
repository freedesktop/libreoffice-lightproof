import xml.etree.ElementTree as ET
import string


tree = ET.parse("test.xml") # parsing grammar.xml into an ElementTree instance

# list all rules with simple tokens
for rule in tree.iter("rule"):  # cycle for all <rule> elements of grammar.xml, variable rule contains the data of the actual element
  simple = True  # simple rule is a rule with tokens without attributes (see documentaton of LanguageTool grammar.xml)
  for token in rule.iter("token"): # cycle for all tokens in the actual rule, variable token contains the data of the actual <token> element
    if token.attrib and token.attrib.keys() != ["regexp"]: # if attrib is not an empty dict (attrib is the Python dict of attributes of the XML element, see ElementTree doc), regexp is supported by the parethesized tokens in the output
      simple = False  # the rule is not simple
  if simple:
    for token in rule.iter("token"):
      if pattern.attrib == None:
	print "(%s)" % token.text,
      if pattern.attrib != None:
	MarkFrom = pattern.attrib['mark_from'].text - 1
	MarkTo = pattern.attrib['mark_to'].text + 1
	MarkText = token.text
	Mark = string.split(MarkText)
	for list in Mark:
	  list[MarkFrom:MarkTo] = "(" + Mark[MarkFrom:MarkTo] + ")"
      print "(%s)" % Mark,
    print "->", rule.find('message').find('suggestion').text, "# Did you mean?"
      
