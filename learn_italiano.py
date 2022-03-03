diccionary_numbers  = {0: 'zero', 1: 'uno', 2: 'due', 3: 'tre', 4: 'quattro', 5: 'cinque', 6: 'sei', 7: 'sette', 8: 'otto', 9: 'nove', 10: 'dieci', 11: 'undici', 12: 'dodici'}
diccionary_fam_1    = {0: {'la madre': 'la madre'}, 1: {'el padre': 'il padre'}, 2: {'la hermana': 'la sorella'}, 3: {'el hermano': 'il fratello'}, 4: {'la abuela': 'la nonna'}, 5: {'el abuelo': 'il nono'}, 6: {'la tía': 'la zia'}, 7: {'el tío': 'lo zio'}, 8: {'la prima': 'la cugina'}, 9: {'el primo': 'il cugino'}}
diccionary_fam_2    = {0: diccionary_fam_1[0]['la madre'], 1: diccionary_fam_1[1]['el padre'], 2: diccionary_fam_1[2]['la hermana'], 3: diccionary_fam_1[3]['el hermano'], 4: diccionary_fam_1[4]['la abuela'], 5: diccionary_fam_1[5]['el abuelo'], 6: diccionary_fam_1[6]['la tía'], 7: diccionary_fam_1[7]['el tío'], 8: diccionary_fam_1[8]['la prima'], 9: diccionary_fam_1[9]['el primo']}
diccionary_colors_1 = {0: {'azul': 'blu'}, 1: {'rojo': 'rosso'}, 2: {'verde': 'verde'}, 3: {'negro': 'negro'}, 4: {'blanco': 'blanco'}, 5: {'gris': 'grigio'}, 6: {'amarillo': 'giallo'}, 7: {'marron': 'marrone'}, 8: {'anaranjado': 'arancione'}, 9: {'rosa': 'rosa'}}
diccionary_colors_2 = {0: diccionary_colors_1[0]['azul'], 1: diccionary_colors_1[1]['rojo'], 2: diccionary_colors_1[2]['verde'], 3: diccionary_colors_1[3]['negro'], 4: diccionary_colors_1[4]['blanco'], 5: diccionary_colors_1[5]['gris'], 6: diccionary_colors_1[6]['amarillo'], 7: diccionary_colors_1[7]['marron'], 8: diccionary_colors_1[8]['anaranjado'], 9: diccionary_colors_1[9]['rosa']}
diccionary_clock_1  = {0: {'las nueve': 'le nove'}, 1: {'las once': 'le undici'}, 2: {'la una': 'le una'}, 3: {'las tres': 'le tre'}, 4: {'las once y media': 'le undici e mezza'}, 5: {'las diez y cuarto': 'le dieci e un quarto'}, 6: {'cuarto para las cinco': 'le cinque meno un quarto'}, 7: {'las seis y veinte': 'le sei e venti'}, 8: {'las ocho veinticinco': 'le otto e venticinque'}, 9: {'cinco para las diez': 'le dieci meno cinque'}}
diccionary_clock_2  = {0: diccionary_clock_1[0]['las nueve'], 1: diccionary_clock_1[1]['las once'], 2: diccionary_clock_1[2]['la una'], 3: diccionary_clock_1[3]['las tres'], 4: diccionary_clock_1[4]['las once y media'], 5: diccionary_clock_1[5]['las diez y cuarto'], 6: diccionary_clock_1[6]['cuarto para las cinco'], 7: diccionary_clock_1[7]['las seis y veinte'], 8: diccionary_clock_1[8]['las ocho veinticinco'], 9: diccionary_clock_1[9]['cinco para las diez']}

def menu():
    global option
    print('       ----------- Menu ------------')
    print('0 Salir')
    print('1 Numeros')
    print('2 Integrantes de la familia')
    print('3 Colores')
    print('4 La hora')
    print('5 Oraciones básicas')
    option = int(input("Please enter a number: "))

def numeros():
    print('       ----------- Numeros ------------')
    print(' 0 -> ' + diccionary_numbers[0], '        7 -> ' + diccionary_numbers[7])
    print(' 1 -> ' + diccionary_numbers[1], '         8 -> ' + diccionary_numbers[8])
    print(' 2 -> ' + diccionary_numbers[2], '         9 -> ' + diccionary_numbers[9])
    print(' 3 -> ' + diccionary_numbers[3], '         10 -> ' + diccionary_numbers[10])
    print(' 4 -> ' + diccionary_numbers[4], '     11 -> ' + diccionary_numbers[11])
    print(' 5 -> ' + diccionary_numbers[5], '      12 -> ' + diccionary_numbers[12])
    print(' 6 -> ' + diccionary_numbers[6])
    print('-------------------------------------------')
    i = 0
    while i <= 12:
        print('Repite escribiendo correctamente los números en palabras')
        reply_number = input(diccionary_numbers[i] + ' -> : ')
        if reply_number == diccionary_numbers[i]:
            i += 1
        else:
            print('intenta nuevamente')
    print('Congratulazioni...!!!')

def fam():
    print('       ----------- Integrantes de la familia ------------')
    print('la madre    ==  ' + diccionary_fam_1[0]['la madre'])
    print('el padre    ==  ' + diccionary_fam_1[1]['el padre'])
    print('la hermana  ==  ' + diccionary_fam_1[2]['la hermana'])
    print('el hermano  ==  ' + diccionary_fam_1[3]['el hermano'])
    print('la abuela   ==  ' + diccionary_fam_1[4]['la abuela'])
    print('el abuelo   ==  ' + diccionary_fam_1[5]['el abuelo'])
    print('la tía      ==  ' + diccionary_fam_1[6]['la tía'])
    print('el tío      ==  ' + diccionary_fam_1[7]['el tío'])
    print('la prima    ==  ' + diccionary_fam_1[8]['la prima'])
    print('el primo    ==  ' + diccionary_fam_1[9]['el primo'])
    print('-------------------------------------------')
    i = 0
    while i <=9:
        print('Repite escribiendo correctamente')
        reply_fam = input(diccionary_fam_2[i] + ' -> : ')
        if reply_fam == diccionary_fam_2[i]:
            i += 1
        else:
            print('intenta nuevamente')
    print('Congratulazioni...!!!')

def colors():
    print('       ----------- Colores ------------')
    print('azul        ==  ' + diccionary_colors_1[0]['azul'])
    print('rojo        ==  ' + diccionary_colors_1[1]['rojo'])
    print('verde       ==  ' + diccionary_colors_1[2]['verde'])
    print('negro       ==  ' + diccionary_colors_1[3]['negro'])
    print('blanco      ==  ' + diccionary_colors_1[4]['blanco'])
    print('gris        ==  ' + diccionary_colors_1[5]['gris'])
    print('amarillo    ==  ' + diccionary_colors_1[6]['amarillo'])
    print('marron      ==  ' + diccionary_colors_1[7]['marron'])
    print('anaranjado  ==  ' + diccionary_colors_1[8]['anaranjado'])
    print('rosa        ==  ' + diccionary_colors_1[9]['rosa'])
    print('-------------------------------------------')
    i = 0
    while i <=9:
        print('Repite escribiendo correctamente')
        reply_colors = input(diccionary_colors_2[i] + ' -> : ')
        if reply_colors == diccionary_colors_2[i]:
            i += 1
        else:
            print('intenta nuevamente')
    print('Congratulazioni...!!!')

def relog():
    print('       ----------- Relog ------------')
    print('las nueve               ==  ' + diccionary_clock_1[0]['las nueve'])
    print('las once                ==  ' + diccionary_clock_1[1]['las once'])
    print('la una                  ==  ' + diccionary_clock_1[2]['la una'])
    print('las tres                ==  ' + diccionary_clock_1[3]['las tres'])
    print('las once y media        ==  ' + diccionary_clock_1[4]['las once y media'])
    print('las diez y cuarto       ==  ' + diccionary_clock_1[5]['las diez y cuarto'])
    print('cuarto para las cinco   ==  ' + diccionary_clock_1[6]['cuarto para las cinco'])
    print('las seis y veinte       ==  ' + diccionary_clock_1[7]['las seis y veinte'])
    print('las ocho veinticinco    ==  ' + diccionary_clock_1[8]['las ocho veinticinco'])
    print('cinco para las diez     ==  ' + diccionary_clock_1[9]['cinco para las diez'])
    print('-------------------------------------------')
    i = 0
    while i <=9:
        print('Repite escribiendo correctamente')
        reply_colors = input(diccionary_clock_2[i] + ' -> : ')
        if reply_colors == diccionary_clock_2[i]:
            i += 1
        else:
            print('intenta nuevamente')
    print('Congratulazioni...!!!')


while True:
    try:
        menu()
        if option == 1:
            numeros()
        elif option == 2:
            fam()
        elif option == 3:
            colors()
        elif option == 4:
            relog()
        elif option == 0:
            print('BYE')
            break
        else:
            print('*Error, elige una option valida')
    except ValueError:
        print('*NOT ACCEPT CHAR')
        print('------------------------------------------------------\n')