a = input('text:  ')

for v in ['a','i','o','u','e']:
    a = a.replace(v,'').replace(v.upper(),'')

a = a.replace('v','%')
a = a.replace('b','v')
a = a.replace('%','b')



len(a.replace(' ',' '))
