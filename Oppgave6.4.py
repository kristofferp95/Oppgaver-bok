
def reverse(number):
    reverseNumber = 0
    while number > 0: 
        remainder = number % 10
        reverseNumber = (reverseNumber * 10) + remainder
        number = number // 10

    return reverseNumber


def main():
    testnumber = int(input(f'Enter a random integer: '))
    isPalindrome = reverse(testnumber)
    if testnumber == isPalindrome: 
        print(f'{testnumber} is a Palindrome')
    else:
        print(f'{testnumber} is not a palindrome')

main()