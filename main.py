print('PASSWORD GENERATOR')
while True:

    import random

    
    symbol_password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    length_password = int(input('Введите длину пароля: '))
    gen_password = ''

    for i in range(length_password):
        gen_password += random.choice(symbol_password)
    print(gen_password)
