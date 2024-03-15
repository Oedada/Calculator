a = 0
b = 0
operation = ""
while operation != "break":
    print("Напишите первое число ",end = '')
    a = int(input())
    while operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "**" and operation != ">":
        print("Введите нужную операцию ",end = '')
        operation = input()
        if operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "**" and operation != ">":
            print("ошибка ввода")
    print("Напишите второе число ",end = '')
    b = int(input())
    print("Весь список доступных операций доступен на https://github.com/Oedada/Calculator/blob/63b1ab9a9360a04e0378b39d0d510b5910206a62/README.md?plain=1")
    print("Результат:",end = '')
    if operation == "+":
        print(a+b)
    elif operation=="-":
        print(a-b)   
    elif operation=="*":
        print(a*b) 
    elif operation=="/":
        print(a/b)  
    elif operation=="**":
        print(a**b)  
    elif operation==">":
        print(a**(1/b)) 
    operation = ""               


