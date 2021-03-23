menu=True
while menu:                                                                                                                 
    funcao = int(input('''
    ---------------------------Escolha uma função--------------------------

    1 - Calculadora;
    2 - Contador;
    3 - fechar

    Digite a opção desejada, ou precione 4 para obter informações: '''))

    if funcao == 1:
        
        operacao = int(input('''
    ------------------------------Escolha uma operação------------------------

    1 - Soma;
    2 - divisão;
    3 - Subtração;
    4 - Multiplicação;
    5 - Calcúlo de média(notas escolares);
    6 - Calcúlo de quadrado;

    Digite o a opção desejada: '''))
        
        if operacao == 1:
            n1 = int(input(print('Digite o primeiro valor')))
            n2 = int(input(print('Digite o segundo valor')))
            mv = str(input(print('deseja digitar mais valor? sim(y) não (n)')))
            if mv == 'y':
                n3 = int(input(print('digite o terceiro valor')))
                valor3 = n1 + n2 + n3
                print('Seu valor foi:', valor3)
            elif mv == 'n':
                valor2 = n2 + n1
                print('Seu valor foi:', valor2)
                
    


                
        elif operacao == 2:
            nd1 = int(input('Digite o primeiro valor: '))
            nd2 = int(input('Digite o segundo valor: '))
            if nd2 == 0:


                print('não foi possivel realizar essa operação')
            else:
                valord1 = nd1 / nd2
                print('Seu valor foi:', valord1)
            
                
            
        elif operacao == 3:
            ns1 = int(input('Digite o primeiro valor: '))
            ns2 = int(input('Digite o segundo valor: '))
            valors1 = ns1 - ns2
            print('Seu valor foi:', valors1)
            
        elif operacao == 4:
            
            nm1 = int(input('Digite o primeiro valor: '))
            nm2 = int(input('Digite o segundo valor: '))
            valorm1 = nm1 * nm2
            print('Seu valor foi:', valorm1)
          
        elif operacao == 5:
            quantidade = int(input('''
    --------------------------Quanto valores deseja inserir?-----------------

    
                                     2 - 3 - 4 - 5 

                                : '''))
                       
          
            if quantidade == 2:
                d1 = int(input('valor1: '))
                d2 = int(input('valor2: '))
                val1 = (d1 + d2) / 2
                print('sua média é:', val1)
            elif quantidade == 3:
                d3 = int(input('valor1: '))
                d4 = int(input('valor2: '))
                d5 = int(input('valor3: '))
                
                val2 = (d3 + d4 + d5) / 3
                print('sua média é:', val2)
            elif quantidade == 4:
                d6 = int(input('valor1: '))
                d7 = int(input('valor2: '))
                d8 = int(input('valor3: '))
                d9 = int(input('valor4: '))
                
                val3 = (d6 + d7 + d8 + d9) / 4
                print('sua média é:', val3)
            elif quantidade == 5:
                d10 = int(input('valor1: '))
                d11 = int(input('valor2: '))
                d12 = int(input('valor3: '))
                d13 = int(input('valor4: '))
                d14 = int(input('valor5: '))
                
                val4 = (d10 + d11 + d12 + d13 + d14) / 5
                print('sua média é:', val4)
           
        elif operacao == 6:
            aq = int(input('''
    --------------------------O que deseja calcular?-----------------

    
    1 - Área;
    2 - Perimetro;
  

    : '''))
            if aq == 1:
                print('Sendo desenvolvido')
            elif aq == 2:
                print('Sendo desenvolvido')

    elif funcao == 2:
        
        fim = int(input('Digite o número que deseja acabar a contagem: '))
        cont = 0
        fim1 = fim + 1
      
           
        while cont < fim1:
           
            print(cont)
            cont = cont + 1

    elif funcao == 3:
        exit()
        
    elif funcao == 4:
        print('''
    Seja bem vindo a calculadore e multifunçõe, programa que te auxiliará em funções
matematicas e/ou fara sua diversão nas horas vagas.
    ao escolher o numero um, você irá para a calculadora que irá realizar calculos
de matematica.
    ao escolher o 2, você será redirecionado para um contador básico.
            ''')







