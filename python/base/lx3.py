append_text='\nThis is appended file'
my_file=open('my file.txt','a')
my_file.write(append_text)
my_file.close()


file=open('my file.txt','r')

content2=file.readlines()

print(content2)
