# Algoritmo que calcula a tabuada do 2 até a do 9.

tabuada = 1
while tabuada < 10:
  print(tabuada)
  tabuada = tabuada + 1
  for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))
