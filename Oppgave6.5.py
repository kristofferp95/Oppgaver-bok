
def displaySortedNumbers(num1, num2, num3):
    sorted_numbers = sorted(displaySortedNumbers)

    return sorted_numbers

def main():
    numa = float(input(f'Enter a random value: '))
    numb = float(input(f'Enter a random value: '))
    numc = float(input(f'Enter a random value: '))

    result = displaySortedNumbers(numa, numb, numc)

    print(result)

main()