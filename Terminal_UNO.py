import random
print("")
print("=" * 40 + "BEM VINDO AO TERMINAL UNO FOR PYTHON 3.6 - " + "=" * 40)

# ********************************************Declaração de variaveis*********************************************

tentativa = 0
carta_escolhida_pc = 0
carta_escolhida_us = 0
qtd_cartas_us = 0
qtd_cartas_pc = 0
seq_carta_escolhida_pc = 0
seq_carta_escolhida_us = 0
qtd_carta_comprada= 0

# *******************************************Criação de conjunto de cartas - Baralho UNO**************************

cartas = [ '0blue' , '1blue' , '2blue' , '3blue' , '4blue' , '5blue' ,
           '6blue' , '7blue' , '8blue' , '9blue' ,
           '0red' , '1red' , '2red' , '3red' , '4red' , '5red' ,
           '6red' , '7red' , '8red' , '9red' ,
           '0yellow' , '1yellow' , '2yellow' , '3yellow' , '4yellow' , '5yellow' ,
           '6yellow' , '7yellow' , '8yellow' , '9yellow' ,
           '0green' , '1green' , '2green' , '3green' , '4green' , '5green' ,
           '6green' , '7green' , '8green' , '9green' ,
           '6blue' , '7blue' , '8blue' , '9blue' ,
           '0red' , '1red' , '2red' , '3red' , '4red' , '5red' ,
           '6red' , '7red' , '8red' , '9red' ,
           '0yellow' , '1yellow' , '2yellow' , '3yellow' , '4yellow' , '5yellow' ,
           '6yellow' , '7yellow' , '8yellow' , '9yellow' ,
           '0green' , '1green' , '2green' , '3green' , '4green' , '5green' ,
           '6green' , '7green' , '8green' , '9green' ]

# ********************************************Coleta dados do player**********************************************
print ( "" )
user = str(input("Qual é o seu nome? : ")).upper()
print ( "" )
print ( "Boa sorte {} !".format ( user ) )
print ( "=" * 100 )

# **********************************************PC dando cartas***************************************************

pc1 = random.choice ( cartas )
pc2 = random.choice ( cartas )
pc3 = random.choice ( cartas )
pc4 = random.choice ( cartas )
pc5 = random.choice ( cartas )
pc6 = random.choice ( cartas )
pc7 = random.choice ( cartas )

mao_pc = [ pc1 , pc2 , pc3 , pc4 , pc5 , pc6 , pc7 ]
qtd_cartas_pc += 7

#print ( "" )
#print ( "A mão do PC é {} .".format ( mao_pc ) )
print ( "O pc têm {} cartas".format ( qtd_cartas_pc ) )

us1 = random.choice ( cartas )
us2 = random.choice ( cartas )
us3 = random.choice ( cartas )
us4 = random.choice ( cartas )
us5 = random.choice ( cartas )
us6 = random.choice ( cartas )
us7 = random.choice ( cartas )

mao_us = [ us1 , us2 , us3 , us4 , us5 , us6 , us7 ]

print ( "" )
print ( "A mão do {} é {} .".format ( user , mao_us ) )
qtd_cartas_us += 7
print ( "O {} têm {} cartas".format ( user , qtd_cartas_us ) )
print ( "" )

# **********************************************PC fazendo o tombo ***************************************************

print ( "=" * 47 + "ESCOLHENDO O TOMBO" + "=" * 47)
print ( "" )
tombo = str ( random.choice ( cartas ) )
cor_do_tombo = (tombo[ 1:10 ])
numero_do_tombo = (tombo[ 0:1 ])
print ( "O tombo na mesa é {} .".format ( tombo ) )

# **********************************************PC fazendo o tombo ***************************************************

while qtd_cartas_pc is not 0 and qtd_cartas_us is not 0:

    print ( "" )
    print ( "=" * 47 + "JOGADA" + "=" * 47)
    print ( "O tombo na mesa é {} .".format ( tombo ) )
    print ( "" )
    print ( "A mão do {} é {} .".format ( user , mao_us ) )
    print ( "O {} agora tem {} cartas".format ( user , qtd_cartas_us ) )
    print ( "" )

    jogada_us = str(input("[J] = JOGAR / [P] PASSAR / [C] COMPRAR")).capitalize()
    print(jogada_us)

    if jogada_us == "C":
        carta_comprada_us = random.choice ( cartas )
        mao_us.append ( carta_comprada_us )
        print ( "Comprando carta..." )
        print ( "A carta comprada foi {}".format ( carta_comprada_us ) )
        print ( "A mão do {} é {} .".format ( user , mao_us ) )
        print ( "" )
        qtd_cartas_us += 1
        jogada_us = str ( input ( "[J] = JOGAR / [P] PASSAR / [C] COMPRAR" ) ).capitalize ( )
        print ( jogada_us )
        qtd_tentativa_antes = 0
        qtd_carta_comprada = 0

    if jogada_us == "P":
        pass
        print("{} passou a vez..".format(user))
        tentativa = 0
        carta_escolhida_pc = 0
        seq_carta_escolhida_pc = 0
        qtd_tentativa_antes = 0
        qtd_carta_comprada = 0

    if jogada_us == "J":
        seq_carta_escolhida_us = (int ( input ( "Escolha uma carta para jogar {}: ".format ( user ) ) )) - 1
        carta_escolhida_us = str ( mao_us[ seq_carta_escolhida_us ] )

        print ( "" )
        print ( "A carta escolhida foi {}".format ( carta_escolhida_us ) )

        print ( "" )
        del mao_us[ seq_carta_escolhida_us ]
        qtd_cartas_us -= 1

        tombo = carta_escolhida_us
        cor_do_tombo = (tombo[ 1:10 ])
        numero_do_tombo = (tombo[ 0:1 ])

        print ( "A mão do {} agora é {} .".format ( user , mao_us ) )
        print ( "O {} agora tem {} cartas".format ( user , qtd_cartas_us ) )
        print ( "" )

        print ( "O tombo na mesa é {} .".format ( tombo ) )

        print ( "" )
        print ( "-" * 100 )
        tentativa = 0
        seq_carta_escolhida_pc = 0
        print ( "Agora é a vez do PC" )
        print ( "O tombo na mesa é {} .".format ( tombo ) )
        qtd_tentativa_antes = 0
        qtd_carta_comprada = 0

    while tentativa < qtd_cartas_pc:

           # print ( "" )
           # print ( "A mão do PC é {} .".format ( mao_pc ) )

            carta_escolhida_pc = str ( mao_pc[ seq_carta_escolhida_pc ] )

           # print ( "PC tentou escolher a carta {}...".format ( carta_escolhida_pc ) )

            cor_da_carta_escolhida_pc = (carta_escolhida_pc[ 1:10 ])
            numero_da_carta_escolhida_pc = (carta_escolhida_pc[ 0:1 ])

            # ve a cor se é igual ou o numero de alguma carta é igual ao do tombo

            if cor_da_carta_escolhida_pc == cor_do_tombo or numero_do_tombo == numero_da_carta_escolhida_pc:
                #print ( "O tombo na mesa é {} .".format ( tombo ) )
                print ( "" )
                del mao_pc[ seq_carta_escolhida_pc ]  # se encontrou alguma carta que atenda, descaerte
                qtd_cartas_pc -= 1

                print ( "Na tentativa de numero {} o PC escolheu a carta {}...".format ( (tentativa + 1) ,
                                                                                         carta_escolhida_pc ) )
                print ( " ...e essa carta pôde ser jogada :)..." )
                print ( "" )
                print ( "O pc têm {} cartas".format ( qtd_cartas_pc ) )
                print ( "" )


            #    print ( "A mão do PC é {} .".format ( mao_pc ) )
            #    print ( "" )

                tombo = carta_escolhida_pc
                cor_do_tombo = (tombo[ 1:10 ])
                numero_do_tombo = (tombo[ 0:1 ])
                print ( "O tombo na mesa é {} .".format ( tombo ) )
                print ( "" )

                tentativa += 100

            else:
                print("Na tentativa de numero {} o PC escolheu uma carta, ...".format ( (tentativa + 1) ,carta_escolhida_pc ) )
                print (" ...mas a cor ou numero é diferente..." )#print("Na tentativa de numero {} o PC escolheu a carta{}...".format( (tentativa + 1) ,carta_escolhida_pc ) )
                print ( "" )
                seq_carta_escolhida_pc += 1
                tentativa += 1
                if qtd_tentativa_antes > 0:
                    tentativa = 100

                if seq_carta_escolhida_pc == qtd_cartas_pc:
                    if qtd_carta_comprada < 1:
                        qtd_tentativa_antes = tentativa
                        carta_comprada_pc = random.choice ( cartas )
                        mao_pc.append ( carta_comprada_pc )
                        print ( "O PC comprou uma carta" )
                        #print ( "A carta comprada foi {}".format ( carta_comprada_pc ) )
                   #     print ( "A mão do PC é {} .".format ( mao_pc ) )
                        print ( "" )
                        qtd_cartas_pc += 1
                        qtd_carta_comprada = 1


# ********************************************** GAME OVER*************************************************************				


if qtd_cartas_us < qtd_cartas_pc:
    print ( "O {} GANHOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".format ( user ) )
else:
    print ( "O PC GANHOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" )


print ( "=" * 47 + "GAME-OVER" + "=" * 47)




