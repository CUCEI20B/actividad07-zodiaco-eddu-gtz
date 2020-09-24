dia = int(input())
mes = int(input())

#Enero
if mes == 1:
    if dia >= 1 and dia <= 20:
        print("capricornio")
    elif dia >= 21 and dia <= 30:
        print("acuario")

#Febrero  
elif mes == 2:
    if dia >= 1 and dia <= 19:
        print("acuario")
    elif dia >= 20 and dia <= 28:
        print("picis")

#Marzo   
elif mes == 3:
    if dia >= 1 and dia <= 20:
        print("picis")
    elif dia >= 21 and dia <= 31:
        print("aries")

#Abril   
elif mes == 4:
    if dia >= 1 and dia <= 20:
        print("aries")
    elif dia >= 21 and dia <= 30:
        print("tauro")

#Mayo 
elif mes == 5:
    if dia >= 1 and dia <= 21:
        print("tauro")
    elif dia >= 22 and dia <= 31:
        print("geminis")

#Junio
elif mes == 6:
    if dia >= 1 and dia <= 21:
        print("geminis")
    elif dia >= 22 and dia <= 30:
        print("cancer")

#Julio
elif mes == 7:
    if dia >= 1 and dia <= 22:
        print("cancer")
    elif dia >= 23 and dia <= 31:
        print("leo")

#Agosto   
elif mes == 8:
    if dia >= 1 and dia <= 23:
        print("leo")
    elif dia >= 24 and dia <= 31:
        print("virgo")

#Septiembre   
elif mes == 9:
    if dia >= 1 and dia <= 22:
        print("virgo")
    elif dia >= 23 and dia <= 30:
        print("libra")

#Octubre
elif mes == 10:
    if dia >= 1 and dia <= 22:
        print("libra")
    elif dia >= 23 and dia <= 30:
        print("escorpion")

#Noviembre       
elif mes == 11:
    if dia >= 1 and dia <= 21:
        print("escorpion")
    elif dia >= 22 and dia <= 31:
        print("sagitario")

#DICIEMBRE
elif mes == 12:
    if dia >= 1 and dia <= 21:
        print("sagitario")
    elif dia >= 22 and dia <= 31:
        print("capricornio")
else:
    print("No existe ese mes")