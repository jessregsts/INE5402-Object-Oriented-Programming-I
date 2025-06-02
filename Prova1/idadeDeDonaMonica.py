 # idade da dona monica e de seus dois filhos
 m = int(input())
 a = int(input())
 b = int(input())
 # idade do terceiro filho que sera calculada
 c = m - (a + b)
 # comparaçao entre as idades (qual a maior)
 if a > b and a > c:
   print(a)
 elif b > a and b > c:
   print(b)
 elif c > a and c > b:
   print(c)
