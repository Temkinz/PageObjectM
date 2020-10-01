import random

class Utils():

    def passwords():
        password = ''
        for x in range(9):
            password = password + random.choice(list('1234567890qwertyuiopASDFGHJKLZXCVBMNMNM'))
        print(password)
        return password

