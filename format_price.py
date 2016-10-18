import argparse
import re

def create_parser():
    parser = argparse.ArgumentParser(description="Скрипт выполняет "
                                                 "форматирование строки "
                                                 "цены товара.")
    parser.add_argument('price', metavar='PRICE',
                        help='Форматируемая строка цены товара.')
    return parser


def format_price(price):
    if not isinstance(price,(float, int, str)):
        raise TypeError('price type must be a string, int or float.')
    if not re.match('\d+\.?\d+$', str(price).strip()):
        raise ValueError('Error format: value must contain only numbers and '
                         'symbol "." (like int or float type)')
    price = float(price)
    if round(price, 2) % 1 == 0:
        return '{:,.0f}'.format(price).replace(',', ' ')
    else:
        return '{:,.2f}'.format(price).replace(',', ' ')

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    print(format_price(namespace.price))
