print("Clases v2")

class Datos:
    def __init__(self,est,peso):
        self.est=est
        self.peso=peso
    def m_datos(self):
        print(f"Peso: {self.peso} k")
        print(f"Estatura: {self.est} m") 
    def my_lista(self):
        ins=['piano','trompeta','bajo']
        print(ins)
        for y in ins:
            print(y)
    def my_dic(self):
        edad={
            "pancho": 45,
            'rosa':30,
            'ulises':20
        }
        print(edad)
        for a,b in edad.items():
            print(a, b)
    def my_tupla(self):
        lengua=('español','portugues','mandarin')
        print(lengua)
        for d in lengua:
            print(d)
    def my_set(self):
        m_carro={'Nissan','Ford','Mitsubishi'}
        print(m_carro)
        for c in m_carro:
            print(c)

info=Datos(1.80,50)

print("-Ejemplo-")
info.m_datos()
print("-Lista-")
info.my_lista()
print("-Diccionario-")
info.my_dic()
print("-Tupla-")
info.my_tupla()
print("-Set-")
info.my_set()

print('')
print('--Gabriel Montes--')
# python tiposdedatos.py