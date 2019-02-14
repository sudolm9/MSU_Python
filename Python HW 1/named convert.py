#This program takes an input from the user and changes the sentence that is inputed.
print('Enter a sentence and i will change it')
a = input('Enter a sentence')
print('The sentence in lower case is: ',a.lower())
a1 = a.lower()
for c in ['a','e','i','o','u']:
    a1=a1.replace(c,c.upper())
a2 = a.lower()
for d in ['b','c','d','f','g','h','j','k','l','m','n','m','p','q','r','s','t','v','w','x','y','z']:
    a2=a2.replace (d,d.upper())
print('The string with vowels in uppercase and consotants in lowercase is: ',a1,a2)
a1=a.lower
print('The sentence in reverse order is: ',a[::-1])

