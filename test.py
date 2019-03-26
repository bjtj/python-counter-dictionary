from pycountdict import CounterDictionary

def main():
    cd = CounterDictionary()
    print(cd)
    cd['a'] = 1
    print(cd)
    cd['b'] = 1
    print(cd)
    cd['A'] = 1
    print(cd)
    cd['a'] = 1
    print(cd)
    print(cd.sum('a', 'A', 'b'))
    print(cd.sum(*cd.keys()))
    
    print('cd.keys(): {}'.format(cd.keys()))
    print('cd.values(): {}'.format(cd.values()))
    print('cd.items(): {}'.format(cd.items()))


if __name__ == '__main__':
    main()
