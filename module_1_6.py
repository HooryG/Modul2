 #1
my_dict = {'Kostya': 1977,'Natasha':1979,'Egor':2006,'Valya':1953,'Vika':1974}
print('Dict:',my_dict)
print('Existing value:',my_dict['Egor'])
print('Not existing value:',my_dict.get('Olga'))
my_dict.update ({'Nadya': 1981,'Gena':1949})
Gena_ = my_dict.pop('Gena') # Как я понял del удалил бы  и ключ и значение,  а pop удаляет ключ
                            # из коллекции, но помнит  значение этого ключа в переменной(Gena_).Верно.?
print('Deleted value:',Gena_)
print('Modified dictionary:',my_dict)
print(my_dict.keys())
 #2
my_set = {10,'LvlGod',20,30,45.5,10,'LvlGod',20,30,45.5,(10,20,40)}
print('Set:',my_set)
my_set.add(25)
my_set.add(75)
my_set.discard('LvlGod')
print('Modified set:',my_set)

