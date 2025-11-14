text=str(input("enter a string:"))
fchar=text[0]
result=fchar+text[1:].replace(fchar,"$")
print(result)
