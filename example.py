#!/bin/python
import textbelt
text = textbelt.textbelt()

#success send
print("testing a good number")
print(text.send('1234567890','I sent this message from python through textbelt.com'))

#failed send
print("testing a failed number")
print(text.send('123456','I sent this message from python through textbelt.com'))
