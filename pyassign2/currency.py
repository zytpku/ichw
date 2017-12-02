"""assign2.py:
The second python assignment of course "Introduction to Computing".
In this module, we can know the amount of currency in another kind of money
by providing the currency code of them and the amount of money in currency_to.
__author__ = "Songchen TAN"
__pkuid__  = "1700011706"
__email__  = "tansongchen@pku.edu.cn"
"""

from urllib.request import urlopen


def analysis(docstr):
    '''Returns:
    The amount of currency received in the given exchange, having type float.

    In the analysis, the binary string received from internet are analyzed
    in order to get the correct amount.

    Parameter docstr: the binary string.
    '''

    jstr = docstr.decode('ascii')
    currency_to_and_its_amount = jstr.split('"')[7]
    amount_to = float(currency_to_and_its_amount.split()[0])

    return amount_to


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    infomation = 'from=' + str(currency_from) + '&to=' + str(currency_to) + '&amt=' + str(amount_from)
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?' + infomation
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    amount_to = analysis(docstr)
    return amount_to


def test_analysis():
    assert(2.0952375 == analysis(b'{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'))


def test_exchange():
    assert(2.0952375 == exchange('USD', 'EUR', 2.5))


def test_all():
    """test all cases"""
    test_analysis()
    test_exchange()

    print("all tests passed")


def main():
    """The main function, receiving the parameters,
    passing them to the function "exchange",
    and giving the answer."""
    test_all()

    currency_from = input('The currency on hand: ')
    currency_to = input('The currency to convert to: ')
    amount_from = float(input('Amount of currency to convert: '))
    amount_to = exchange(currency_from, currency_to, amount_from)

    print('Amount of currency to get:', amount_to)


if __name__ == '__main__':
    main()
