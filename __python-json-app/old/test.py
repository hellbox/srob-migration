#! /usr/bin/python
sample_text = "Foo for bar's foo."
converted = "sample text = %s\n" % sample_text
converted2 = "sample text = %r\n" % sample_text
print(converted)
print(converted2)
