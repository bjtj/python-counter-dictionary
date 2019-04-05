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
    print('sum:', cd.sum())
    print('sum:', cd.sum('a', 'A'))
    print('sum:', cd.sum('a', 'A', 'b'))
    print('sum:', cd.sum(*cd.keys()))
    
    print('cd.keys(): {}'.format(cd.keys()))
    print('cd.values(): {}'.format(cd.values()))
    print('cd.items(): {}'.format(cd.items()))
    print(cd.stdev())

    cd.clear()
    cd.putlist(['a', 'a', 'A', 'b', 'a', 'c', 'b', 'b', 'd'])
    print(cd)

    print(cd.max())
    print(cd.min())
    print(cd.stdev())

    print(CounterDictionary().max())
    print(CounterDictionary().min())
    try:
        print(CounterDictionary().stdev())
    except Exception as e:
        print('expected: {}'.format(e))
    

if __name__ == '__main__':
    main()
