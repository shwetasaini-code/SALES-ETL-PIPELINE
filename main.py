f = open('myfile.txt','r');
text = f.read()
print(text)

f = open('myfile.txt','w');
text = f.write("text")
f.close()