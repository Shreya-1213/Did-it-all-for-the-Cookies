from googletrans import Translator
ts = Translator()
text = input("Enter YOur Text : ")
output = ts.translate(text, dest="en")
print(output.text)
