import argparse
import math


def calc_payment(p, n, i):
    i = i / 12 / 100
    a = p * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    ceil_a = math.ceil(a)
    total_payment = math.ceil(a) * n
    overpay = math.ceil(total_payment - p)
    return print(f'Your annuity payment = {ceil_a}!\nOverpayment = {overpay}')


def calc_loan_principal(a, n, i):
    i = i / 12 / 100
    p = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    round_p = math.floor(p)
    total_payment = a * n
    overpay = math.ceil(total_payment - p)
    return print(f'Your loan principal = {round_p}!\nOverpayment = {overpay}')


def calc_number_of_months(p, a, i):
    i = i / 12 / 100
    if i == 0:
        return math.ceil(p / a)
    base = 1 + i
    x = a / (a - i * p)
    n = math.log(x, base)
    return math.ceil(n)


def in_years(n):
    y = math.floor(n / 12)
    m = n - y * 12
    return y, m


def calc_diff_payment(p, n, i):
    i = i / 12 / 100
    m = 1
    total_payment = 0
    for x in range(1, n + 1):
        d = p / n + i * (p - p * (m - 1) / n)
        d = math.ceil(d)
        print(f'Month {m}: payment is {d}')
        total_payment += d
        m += 1
    overpay = math.ceil(total_payment - p)
    return print(f'Overpayment = {overpay}')


def overpayment(p, a, n):
    total_payment = a * n
    overpay = math.ceil(total_payment - p)
    return print(f'Overpayment = {overpay}')


def parse_arguments():
    parser = argparse.ArgumentParser(description="Credit calculator.")
    parser.add = parser.add_argument('--type', help='Payment type: diff / annuity.')
    parser.add = parser.add_argument('--principal', type=float, help='Principal amount.')
    parser.add = parser.add_argument('--payment', type=float, help='Monthly payment.')
    parser.add = parser.add_argument('--periods', type=int, help='Number of months to repay loan.')
    parser.add = parser.add_argument('--interest', type=float, help='Loan interest.')
    arguments = parser.parse_args()
    if not arguments.type or arguments.type != 'diff' and arguments.type != 'annuity':
        print('Incorrect parameters')
        exit(1)
    elif arguments.type == 'diff' and arguments.payment:
        print('Incorrect parameters')
        exit(1)
    elif not arguments.interest:
        print('Incorrect parameters')
        exit(1)
    elif arguments.principal is None:
        if arguments.payment <= 0 or arguments.periods <= 0 or arguments.interest < 0:
            print('Incorrect parameters')
            exit(1)
    elif arguments.periods is None:
        if arguments.principal <= 0 or arguments.payment <= 0 or arguments.interest < 0:
            print('Incorrect parameters')
            exit(1)
    elif arguments.payment is None:
        if arguments.principal <= 0 or arguments.periods <= 0 or arguments.interest < 0:
            print('Incorrect parameters')
            exit(1)
    return arguments


args = parse_arguments()
if not args.principal:
    calc_loan_principal(args.payment, args.periods, args.interest)
elif not args.payment:
    if args.type == 'annuity':
        calc_payment(args.principal, args.periods, args.interest)
    elif args.type == 'diff':
        calc_diff_payment(args.principal, args.periods, args.interest)
elif not args.periods:
    number_of_months = calc_number_of_months(args.principal, args.payment, args.interest)
    years, months = in_years(number_of_months)
    if months == 0:
        print(f'It will take {years} years to repay this loan!')
    elif years == 0:
        print(f'It will take {months} months to repay this loan!')
    else:
        print(f'It will take {years} years and {months} months to repay this loan!')
    overpayment(args.principal, args.payment, number_of_months)
