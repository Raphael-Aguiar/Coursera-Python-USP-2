def insertion_sort(lista):
  for i in range (1, len(lista)):
    while i > 0 and lista[i-1] > lista[i]:
      chave = lista[i]
      lista[i] = lista[i-1]
      lista[i-1] = chave
      i -= 1
  return lista