dia = int(input())
mes = int(input())

#Enero
if mes == 1:
    if dia >= 1 and dia <= 20:
        print("Capricornio")
    elif dia >= 21 and dia <= 30:
        print("Acuario")

#Febrero  
elif mes == 2:
    if dia >= 1 and dia <= 19:
        print("Acuario")
    elif dia >= 20 and dia <= 28:
        print("Picis")

#Marzo   
elif mes == 3:
    if dia >= 1 and dia <= 20:
        print("Picis")
    elif dia >= 21 and dia <= 31:
        print("Aries")

#Abril   
elif mes == 4:
    if dia >= 1 and dia <= 20:
        print("Aries")
    elif dia >= 21 and dia <= 30:
        print("Tauro")

#Mayo 
elif mes == 5:
    if dia >= 1 and dia <= 21:
        print("Tauro")
    elif dia >= 22 and dia <= 31:
        print("Géminis")

#Junio
elif mes == 6:
    if dia >= 1 and dia <= 21:
        print("Géminis")
    elif dia >= 22 and dia <= 30:
        print("Cáncer")

#Julio
elif mes == 7:
    if dia >= 1 and dia <= 22:
        print("Cáncer")
    elif dia >= 23 and dia <= 31:
        print("Leo")

#Agosto   
elif mes == 8:
    if dia >= 1 and dia <= 23:
        print("Leo")
    elif dia >= 24 and dia <= 31:
        print("Virgo")

#Septiembre   
elif mes == 9:
    if dia >= 1 and dia <= 22:
        print("Virgo")
    elif dia >= 23 and dia <= 30:
        print("Libra")

#Octubre
elif mes == 10:
    if dia >= 1 and dia <= 22:
        print("Libra")
    elif dia >= 23 and dia <= 30:
        print("Escorpion")

#Noviembre       
elif mes == 11:
    if dia >= 1 and dia <= 21:
        print("Escorpion")
    elif dia >= 22 and dia <= 31:
        print("Sagitario")

#DICIEMBRE
elif mes == 12:
    if dia >= 1 and dia <= 21:
        print("Sagitario")
    elif dia >= 22 and dia <= 31:
        print("Capricornio")
else:
    print("No existe ese mes")