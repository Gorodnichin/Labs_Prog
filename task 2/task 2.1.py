s=input('Введите строку: ')
q=''
for i in range(len(s)):
    if i==0 or s[i-1]==' ':
        q=q+s[i].upper()
    else:
        q=q+s[i].lower()
print (q)