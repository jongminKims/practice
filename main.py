# Test python env
def print_hello():
    animals = ['dog','cat','hamster'] # in one line
    foods = [
            'Spagetti',
            'Pizza'
    ] # w/o trailing comma
    names = [
            'John',
            'Jane',
            'Gil-gond',
            ] #w/ trailing comma
    fopr f_name in names:
        print(f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()
