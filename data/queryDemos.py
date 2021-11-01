#(1)Restituisce tutti gli attacchi della tabella
attacks = DomainsOfAttack.objects.all()
print(attacks)

#(2)Restituisce un singolo attacco per nome
attackByName = DomainsOfAttack.objects.get(name "Argument Injection")

#(3)Restituisce un singolo attacco per id
attackById = DomainsOfAttack.objects.get(id=151)

#(4)Una volta dichiarata la variabile è possibile ottenere tutti gli attributi relativi ad essa
print(attacks.relatedattackpatterns) #figli
print(attacks.typicalseverity) #gravità
print(attacks.abstraction) #livello di astrazione

#(5)Restituisce tutti gli attacchi con un determinato livello di astrazione
attacks = DomainsOfAttack.objects.filter(abstraction="Meta")

#(5)Restituisce tutti gli attacchi figli dato un certo ID
attacks = DomainsOfAttack.objects.filter(relatedattackpatterns__icontains="151")