
'''entrada= []
entrada.append(input().upper())
entrada.append(input().upper())
entrada.append(input().upper()) '''


d ={
  "AGUIA":["VERTEBRADO","AVE","CARNIVORO"],
  "POMBA":["VERTEBRADO","AVE","ONIVORO"],
  "HOMEM":["VERTEBRADO","MAMIFERO","ONIVORO"],
  "VACA":["VERTEBRADO","MAMIFERO","HERBIVORO"],
  "PULGA":["INVERTEBRADO","INSETO","HEMATOFAGO"],
  "LAGARTA":["INVERTEBRADO","INSETO","HERBIVORO"],
  "SANGUESSUGA":["INVERTEBRADO","ANELIDEO","HEMATOFAGO"],
  "MINHOCA":["INVERTEBRADO","ANELIDEO","ONIVORO"]
}
key = d.keys()
print(key)
print(key[0])
'''for i in range(len(d)):
  if entrada in d[i]:
    print(d[i])'''