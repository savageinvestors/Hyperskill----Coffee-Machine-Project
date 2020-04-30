water = 400
milk = 540
beans = 120
cups = 9
money = 550
task = ('buy', 'fill', 'take', 'remaining', 'exit', 'back')
print('Write action (buy, fill, take, remaining, exit): ')
x = input()
while x in task:
# Supplies on Hand
# Supplies Needed
    espresso_water = 250
    espresso_milk = 0
    espresso_beans = 16
    espresso_cups = 1
    espresso_price = 4
    latte_water = 350
    latte_milk = 75
    latte_beans = 20
    latte_cups = 1
    latte_price = 7
    cappuccino_water = 200
    cappuccino_milk = 100
    cappuccino_beans = 12
    cappuccino_cups = 1
    cappuccino_price = 6
# Do we have enough to make one cup?
    make_espresso1 = water - espresso_water
    make_espresso2 = milk - espresso_milk
    make_espresso3 = beans - espresso_beans
    make_espresso4 = cups - espresso_cups
    espresso_min = min(make_espresso1, make_espresso2, make_espresso3, make_espresso4)
    make_latte1 = water - latte_water
    make_latte2 = milk - latte_milk
    make_latte3 = beans - latte_beans
    make_latte4 = cups - latte_cups
    latte_min = min(make_latte1, make_latte2, make_latte3, make_latte4)
    make_cappuccino1 = water - cappuccino_water
    make_cappuccino2 = milk - cappuccino_milk
    make_cappuccino3 = beans - cappuccino_beans
    make_cappuccino4 = cups - cappuccino_cups
    cappuccino_min = min(make_cappuccino1, make_cappuccino2, make_cappuccino3, make_cappuccino4)
# Run Machine
    if x == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
        b = input()
        if b == '1':
            if make_espresso1 >= 0 and make_espresso2 >= 0 and make_espresso3 >= 0 and make_espresso4 >= 0:
                print('I have enough resources, making you a coffee!')
                water = water - espresso_water
                milk = milk - espresso_milk
                beans = beans - espresso_beans
                cups = cups - espresso_cups
                money = money + espresso_price
            else:
                if espresso_min == make_espresso1:
                    print('Sorry, not enough water!')
                if espresso_min == make_espresso2:
                    print('Sorry, not enough milk!')
                if espresso_min == make_espresso3:
                    print('Sorry, not enough coffee beans')
                if espresso_min == make_espresso4:
                    print('Sorry, not enough disposable cups')
        elif b == '2':
            if make_latte1 >= 0 and make_latte2 >= 0 and make_latte3 >= 0 and make_latte4 >= 0:
                print('I have enough resources, making you a coffee!')
                water = water - latte_water
                milk = milk - latte_milk
                beans = beans - latte_beans
                cups = cups - latte_cups
                money = money + latte_price
            else:
                if latte_min == make_latte1:
                    print('Sorry, not enough water!')
                if latte_min == make_latte2:
                    print('Sorry, not enough milk!')
                if latte_min == make_latte3:
                    print('Sorry, not enough coffee beans')
                if latte_min == make_latte4:
                    print('Sorry, not enough disposable cups')
        elif b == '3':
            if make_cappuccino1 >= 0 and make_cappuccino2 >= 0 and make_cappuccino3 >= 0 and make_cappuccino4 >= 0:
                print('I have enough resources, making you a coffee!')
                water = water - cappuccino_water
                milk = milk - cappuccino_milk
                beans = beans - cappuccino_beans
                cups = cups - cappuccino_cups
                money = money + cappuccino_price
            else:
                if cappuccino_min == make_cappuccino1:
                    print('Sorry, not enough water!')
                if cappuccino_min == make_cappuccino2:
                    print('Sorry, not enough milk!')
                if cappuccino_min == make_cappuccino3:
                    print('Sorry, not enough coffee beans')
                if cappuccino_min == make_cappuccino4:
                    print('Sorry, not enough disposable cups')
        else:
            ()
    elif x == 'fill':
        print('Write how many ml of water do you want to add: ')
        water_fill = int(input())
        print('Write how many ml of milk do you want to add: ')
        milk_fill = int(input())
        print('Write how many grams of coffee beans do you want to add: ')
        beans_fill = int(input())
        print('Write how many disposable cups of coffee do you want to add: ')
        cups_fill = int(input())
        water = water + water_fill
        milk = milk + milk_fill
        beans = beans + beans_fill
        cups = cups + cups_fill
        money = money + 0
    elif x == 'take':
        print('I gave you $' + str(money))
        water = water + 0
        milk = milk + 0
        beans = beans + 0
        cups = cups + 0
        money = 0
    elif x == 'remaining':
        print('The coffee machine has:')
        print(str(water) + ' of water')
        print(str(milk) + ' of milk')
        print(str(beans) + ' of coffee beans')
        print(str(cups) + ' of disposable cups')
        print('$' + str(money) + ' of money')
    elif x == 'exit':
        exit()
    print('Write action (buy, fill, take, remaining, exit): ')
    x = input()
