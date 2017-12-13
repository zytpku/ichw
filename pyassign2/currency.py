#!/usr/bin/env python3

"""currency.py: Description of what currency does.

exchange the amount of currency you have to the currency you want to have and test if the output is correct.
If it is right,you will get the answer
"""

fromwhere = input()
towhere = input()
amount = input()


def exchange(currency_from, currency_to, amount_from):
    '''exchange specific amount of the currency you have to another kind of currency you want'''
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%s&to=%s&amt=%s'%(currency_from,currency_to,amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = jstr.replace('false','False')
    jstr = jstr.replace('true','True')
    test = dict(eval(jstr))
    a = test['to']
    b = a.split()
    c = float(b[0])
    return c


def test_get_from():
    '''test if the exchange founction is correct'''
    assert(0.9<=3.672878 / exchange('USD', 'AED', 1)<=1.1)
    assert(0.9<=314.6101 / exchange('USD', 'AFN', 4.6)<=1.1)
    assert(0.9<=890.8074 / exchange('USD', 'ALL', 7.98)<=1.1)
    

def test_all():
    '''test all cases'''
    test_get_from()
    print('All tests passed') 


def main():
    '''create a main function and run the code'''
    result = exchange(fromwhere,towhere,amount)
    test_all()
    print(result)


if __name__=="__main__":
	main()
