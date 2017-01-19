
def my_txt(file_name):
	fr = file("file_name.py",'r')
	text = fr.readlines()
#print text
	for line in text:
	#print line
		try:
			words = line.split(" ")
			print words[1]
		except Exception:
			print "no second word"
return my_txt(file_name)

'''f_c_l=[x[0] for x in text]
print f_c_l
'''

