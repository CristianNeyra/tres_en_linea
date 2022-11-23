gato=[[" "," "," "],[" "," "," "],[" "," "," "]];
gatop=[["7","8","9"],["4","5","6"],["1","2","3"]];

def ganar(matriz, signo):
    #TODO: programar el resto de als columnas, filas y diagonales para verificar al ganador
    ganador=False;
    c1=contadorcol1(matriz, signo);
    c2=contadorcol2(matriz, signo);
    c3=contadorcol3(matriz, signo);
    f1=contadorfil1(matriz,signo);
    f2=contadorfil2(matriz,signo);
    f3=contadorfil3(matriz,signo);
    d1=contadordiag1(matriz,signo);
    d2=contadordiag2(matriz,signo);
    if c1==3 or c2==3 or c3==3 or f1==3 or f2==3 or f3==3 or d1==3 or d2==3:
        ganador=True;
    return ganador; 

def mostrargato(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print ("["+str(matriz[i][j])+"] ",end='');
        print ("");


def contadorcol1(matriz, signo):
    contador=0;
    if signo=="X":
        for i in range(3):
            if matriz[i][0] == "X":
                contador=contador+1;
    elif signo=="O":
        for i in range(3):
            if matriz[i][0] == "O":
                contador=contador+1;
    return contador;

#TODO: definir Contador Columna 2
def contadorcol2(matriz, signo):
    contador=0;
    if signo=="X":
        for i in range(3):
            if matriz[i][1]=="X":
                contador=contador+1;
    elif signo=="O":
        for i in range(3):
            if matriz[i][1]=="O":
                contador=contador+1;
    return contador;


#TODO: definir Contador Columna 3
def contadorcol3(matriz, signo):
    contador=0;
    if signo=="X":
        for i in range(3):
            if matriz[i][2]=="X":
                contador=contador+1;
    elif signo=="O":
        for i in range(3):
            if matriz[i][2]=="O":
                contador=contador+1;
    return contador;


def contadorfil1(matriz, signo):
    contador=0;
    if signo=="X":
        for j in range(3):
            if matriz[0][j]=="X":
                contador=contador+1;
    elif signo=="O":
        for j in range(3):
            if matriz[0][j]=="O":
                contador=contador+1;
    return contador;

#TODO: definir Contador Fila 2
def contadorfil2(matriz, signo):
    contador=0;
    contador=0;
    if signo=="X":
        for j in range(3):
            if matriz[1][j]=="X":
                contador=contador+1;
    elif signo=="O":
        for j in range(3):
            if matriz[1][j]=="O":
                contador=contador+1;
    return contador;

#TODO: definir Contador Fila 3
def contadorfil3(matriz, signo):
    contador=0;
    if signo=="X":
        for j in range(3):
            if matriz[2][j]=="X":
                contador=contador+1;
    elif signo=="O":
        for j in range(3):
            if matriz[2][j]=="O":
                contador=contador+1;
    return contador;

#TODO: definir diagonal 1
def contadordiag1(matriz, signo):
    diagonal = 0;
    contador = 0;
    if signo=="X":
        for i in range(3):
            if matriz[diagonal][i]=="X":
                diagonal=diagonal+1;
                contador=contador+1;
    elif signo == "O":
        for i in range(3):
            if matriz[diagonal][i]=="O":
                diagonal=diagonal+1;
                contador=contador+1;
    return contador;

#TODO: definir diagonal 2
def contadordiag2(matriz, signo):
    diagonal2=2;
    contador2=0;
    if signo=="X":
        for i in range(3):
            if matriz[i][diagonal2]=="X":
                diagonal2=diagonal2-1;
                contador2=contador2+1;
    elif signo=="O":
        for i in range(3):
            if matriz[i][diagonal2]=="O":
                diagonal2=diagonal2-1;
                contador2=contador2+1;
    return contador2;

#TODO: validar que la posicion de la jugada es valida y la casilla se encuentra disponible
def posicion(gatop, nposicion, gato):
    disponible=False;
    for i in range(len(gatop)):
        for j in range(len(gatop)):
            if nposicion == gatop[i][j]:
                #TODO: verificar si la posicion es valida para continuar la ejecucion, optimizar el codigo a ejecutar
                if gato[i][j]==" ":
                    disponible=True;           
    return disponible;

#TODO: asignar la jugada en la matriz gato, de acuerdo a la posición indicada en la jugada
def jugada(gato,nposicion,gatop, signo):
    for i in range(len(gatop)):
        for j in range(len(gatop)):
            if nposicion==gatop[i][j]:
                gato[i][j]=signo;


# Cuerpo principal del programa
continuar=True;
while continuar==True:
    # Inicia un nuevo juego
    maxjugadas=0;
    jugador1=input(print("Ingrese el Nombre del Jugador 1"));
    print(jugador1+" juega con X");
    jugador2=input(print("Ingrese el Nombre del Jugador 2"));
    print(jugador1+" juega con O");
    print("");
    print(jugador1 + " v/s " + jugador2);
    print("");
    print(mostrargato(gato));
    print ("Turno de Jugador "+jugador1);
    # Mientras las condciones se cumplan los jugadores tomaran turno alternadamente
    empate=False;
    ganador=False;
    while (maxjugadas<=9 and empate==False and ganador==False):
        #Jugador1 mientras la jugada no sea valida continua solicitando la jugada 
        finturno=False;
        while (finturno==False and ganador==False):
            pojugar=input(print(jugador1 +" Ingrese posicion a jugar"));
            if posicion(gatop, pojugar,gato)== True:
                signo="X";
                jugada(gato,pojugar,gatop,signo);
                mostrargato(gato);
                if ganar(gato,signo)== True:
                    print("GANADOR!!!! " + str(jugador1));
                    ganador=True;
                finturno=True;
                maxjugadas=maxjugadas+1;
                if maxjugadas==9:
                    print("EMPATE!!!!!!");
                    empate=True;
            else:
                mostrargato(gato);
                print ("Jugada no diponible");
            
        finturno=False;
        #Jugador2 mientras la jugada no sea valida continua solicitando la jugada 
        while (finturno==False and ganador==False and empate==False):
            pojugar=input(print(jugador2 +" Ingrese posicion a jugar"));
            if posicion(gatop, pojugar,gato)== True:
                signo="O";
                jugada(gato,pojugar,gatop,signo);
                mostrargato(gato);
                if ganar(gato,signo)== True:
                    print("GANADOR!!!! " + str(jugador2));
                    ganador=True;
                finturno=True;
                maxjugadas=maxjugadas+1;
                if maxjugadas==9:
                    print("EMPATE!!!!!!");
                    empate=True;
            else:
                mostrargato(gato);
                print ("Jugada no diponible");
    # Al finalizar el juego consulta si se quiere continuar jugando
    pregunta=input(print("Quiere continuar jugando? S/N "))
    if pregunta.upper()=="N":
        continuar=False;    
    gato=[[" "," "," "],[" "," "," "],[" "," "," "]];