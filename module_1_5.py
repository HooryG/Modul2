immutable_var = 5,[7,6],["Yes","No"],"Start",8,True,124,"Hold",False,1.25
print(immutable_var)
# immutable_var = (5,[7,6],["Yes","No"],"Start",8,True,124,"Hold",False,1.25)
# immutable_var =tuple([5,[7,6],["Yes","No"],"Start",8,True,124,"Hold",False,1.25]) все три варианта ввода являются кортеж(не изменяемой коллекцией обьектов)
print(type(immutable_var))

print(immutable_var)  # [7,6] tuple(Кортеж может нести в себе изменяемые обьекты к примеру список -являеться изменяемым обьектом
                      # или значением в кортетже пример работы с ним ниже)
immutable_var[1][1]=9
immutable_var[1][0]=3
immutable_var[2][0]="No"
immutable_var[2][1]="Yes"
# immutable_var[3] = 8 попытка изменить не изменяемый обьект приовдит к ошибке так как изменять в
                # кортеже внесеные значения нельзя если эти обьекты являються неизменяемыми, так же нельзя изменить и порядок расположения обьектов
print(immutable_var)
print(immutable_var[1])
print(immutable_var[1]+[3]) #можем выплнить сложение concatenate (Сложение строк."в уроке", но по мне так это прикрепить или сцепить)
print(immutable_var[1]*5)   # умножение т.е. по мне так копирование 5 раз списка
mutable_list = [5,[7,6],["Yes","No"],"Start",8,True,124,"Hold",False,1.25]
print(type(mutable_list)) #проверил класс списка - коллекции
mutable_list[3]="Finish"
print(mutable_list)
mutable_list[5] = False
mutable_list[9] = 2
mutable_list[2][1]= "Yes"
mutable_list[1][0]= 2
print(mutable_list)
