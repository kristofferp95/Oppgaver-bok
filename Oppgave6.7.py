def futureinvestmentvalue(investmentAmount, monthlyInterestRate, years): 
    months = years * 12 
    interestRate = (monthlyInterestRate / 100) / 12 
    result = investmentAmount * (1 + interestRate)**months

    return result


def main():
    amount = float(input(f'Enter the total of investmentamount: '))
    interestRate = float(input(f'Enter the monthly interest rate: '))
    years = int(input(f'Enter number of years: '))

    result = futureinvestmentvalue(amount, interestRate, years)

    print(f'The future result is {result:.2f}')

main()