'''
a = 'fddsfrd'
b = 'ddds dsds dfv  fKFSD'
print(b.title())	
print(b.upper())

c = 'hello {n}'.format(n='Bektur')
print(c)

a = 'hello'
c = 'python'
b = a.join(c)
print(b)

h = 'hello bektur good day'
c=h.replace('bektur', 'aidar')
print(c)


a = 'hello'.title()
b = 'bay'.lower()

print( a , b ) 

a = str (True)
print(type(a))

a = input("vedite simvol: ")
b = 'GitHub'
if a in b:
	print(b.split(a))
else:
	print("pshol von")

a = input('vedite chislo:')
b = '12345678'
if a in b:
	print(b.split(a))
else:
	print("pshol von") 
print('finish')

a = 'Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
b = a.replace('е','3')
print (b)
'''

name=input('vashe imya?')
print(f'hello {name}')
a=int(input('skolo vam let?'))
if a>0 and a<=20:
	print('vam zapresheno')
elif a>20 or a==21:
	print('vam razresheno')
b=input('vash lubimyi film?')
print(f'super {b}')
