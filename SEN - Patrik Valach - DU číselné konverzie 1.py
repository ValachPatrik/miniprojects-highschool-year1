#base input and check range
base = int(input('Input the base which to convert from (2 - 16): '))
while base < 2 or base > 16:
  print('Unsuported base, please write number in range 2 to 16.')
  base = int(input('Input the base (2 - 16): '))

#inputed number and check
number_check = False
number = str(input('Input the number to convert: '))
while number_check == False:
  number_check = True
  for i in number:
    if (i < '0' or (i >= str(base) and base < 10)) and (i < 'a' or (ord(i) - ord('a') + 10) >= base):
      print ('Number not in range.')
      number = str(input('Input the number to convert: '))
      number_check = False

#conversion
result = 0
mocnina = len(number)-1
for i in number:
  if i >= 'a':
    result = result + (ord(i) - ord('a') + 10) * base ** mocnina
  else:
    result = result + int(i) * (base ** mocnina)
  mocnina -= 1

print ('result =', int(result))