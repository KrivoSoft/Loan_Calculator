# Loan_Calculator
Console program for calculating a loan by parameters.

## What can this program do?
1. Annuity payments:
   - Calculate the loan term (according to the loan amount, payments per month and rate);
   - Calculate the amount of the monthly payment (according to the loan term, loan amount and loan rate);
   - Calculate the loan amount (according to the amount of monthly payments, loan rate and term).
2. Differentiated payments:
   - Calculate payments by month (by loan amount, period and loan rate).
3. Calculate the loan repayment amount.

## How to run the program?
The program starts and accepts input data through the console.
Some examples are presented below.

Calculate differentiated payments given a principal of 500,000 over 8 months at an interest rate of 7.8%:
```
python main.py --type=diff --principal=500000 --periods=8 --interest=7.8
```

Calculate the principal for a person who paying 8,722 per month for 120 months (10 years) at 5.6% interest:
```
python main.py --type=annuity --payment=8722 --periods=120 --interest=5.6
```
