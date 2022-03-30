import math
import argparse


def what_calculate(args):
    """ Selecting the value to be found """
    if args.type == "annuity":
        if args.payment is None:
            return 'annuity_payment'
        if args.principal is None:
            return 'annuity_loan_principal'
        if args.periods is None:
            return 'annuity_payments_number'
    elif args.type == 'diff':
        return 'diff_payments'


def calc_number(loan_principal, payment_per_month, loan_interest):
    """ Calculation of the number of payments """
    loan_principal = int(loan_principal)
    payment_per_month = int(payment_per_month)
    loan_interest = float(loan_interest)

    loan_interest = loan_interest / 12 / 100
    a = payment_per_month / (payment_per_month - loan_interest * loan_principal)
    b = 1 + loan_interest
    n = math.log(a, b)
    months = math.ceil(n)
    if months > 11:
        years = months // 12
        remainder_months = months % 12
        if remainder_months == 0:
            print(f'It will take {years} years to repay this loan!')
        elif remainder_months == 1:
            print(f'It will take {years} years and {remainder_months} month to repay this loan!')
        else:
            print(f'It will take {years} years and {remainder_months} months to repay this loan!')
    else:
        print(f'It will take {months} months to repay this loan!')

    print()
    overpayment = round(months * payment_per_month - loan_principal)
    print(f'Overpayment =', overpayment)


def calc_annuity(loan_principal, periods, loan_interest):
    """ Calculate the annuity payment """
    loan_principal = float(loan_principal)
    periods = int(periods)
    loan_interest = float(loan_interest) / 1200

    payment_per_month = math.ceil(loan_principal * (loan_interest * pow((1 + loan_interest), periods)) /
                  (pow((1 + loan_interest), periods) - 1))
    print(f'Your annuity payment = {payment_per_month}!')

    print()
    overpayment = round(periods * payment_per_month - loan_principal)
    print(f'Overpayment =', overpayment)


def calc_loan(payment_per_month, periods, loan_interest):
    """ Calculation of the loan amount """
    payment_per_month = float(payment_per_month)
    periods = int(periods)
    loan_interest = float(loan_interest) / 1200

    loan_principal = math.ceil(payment_per_month / ((loan_interest * pow((1 + loan_interest), periods)) /
                                       (pow((1 + loan_interest), periods) - 1)))
    print(f'Your loan principal = {loan_principal}!')

    print()
    overpayment = round(periods * payment_per_month - loan_principal)
    print(f'Overpayment =', overpayment)


def calc_diff_payments(loan_principal, periods, loan_interest):
    """ Calculating differentiated payments """
    loan_principal = float(loan_principal)
    periods = int(periods)
    loan_interest = float(loan_interest)

    loan_interest = loan_interest / 1200
    payments_amount = 0

    for i in range(1, (periods + 1)):
        payment_this_month = loan_principal / periods + loan_interest * \
                             (loan_principal - (loan_principal * (i - 1)) / periods)
        payment_this_month = math.ceil(payment_this_month)
        payments_amount += payment_this_month
        print(f'Month {i}: payment is {payment_this_month}')

    print()
    overpayment = round(payments_amount - loan_principal)
    print('Overpayment =', overpayment)


def menu(args):
    """ Main menu """
    value_we_looking_for = what_calculate(args)

    # for number of monthly payments
    if value_we_looking_for == 'annuity_payments_number':
        calc_number(loan_principal=args.principal,
                    payment_per_month=args.payment,
                    loan_interest=args.interest)

    # for annuity monthly payment amount
    elif value_we_looking_for == 'annuity_payment':
        calc_annuity(loan_principal=args.principal,
                     periods=args.periods,
                     loan_interest=args.interest)

    # for loan principal
    elif value_we_looking_for == 'annuity_loan_principal':
        calc_loan(payment_per_month=args.payment,
                  periods=args.periods,
                  loan_interest=args.interest)

    # calculating differentiated payments
    elif value_we_looking_for == 'diff_payments':
        calc_diff_payments(loan_principal=args.principal,
                           periods=args.periods,
                           loan_interest=args.interest)


def is_args_enough(args):
    """  Check if all values are enough """

    all_args = [args.type, args.payment, args.principal, args.interest, args.periods]
    entered_args = 0
    for arg in all_args:
        if arg is not None:
            entered_args += 1
    if entered_args > 3:
        return True
    else:
        return False


def args_have_problems(args):
    """ Checking arguments received from the console """

    if args.type is None:
        print('You must specify the type of payment')
        return True

    if args.type == 'diff' and args.payment is not None:
        print('With the "diff" type, the "payment" parameter is not specified')
        return True

    if args.interest is None:
        print('Argument "interest" not entered')
        return True

    if not is_args_enough(args):
        print('Not enough arguments')
        return True

    if args.periods is not None:
        if float(args.periods) < 1:
            print('Invalid number of months')
            return True

    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', choices=['annuity', 'diff'])
    parser.add_argument('--payment')
    parser.add_argument('--principal')
    parser.add_argument('--interest')
    parser.add_argument('--periods')
    args = parser.parse_args()

    if args_have_problems(args):
        print('Incorrect parameters')
        exit(1)

    menu(args)
