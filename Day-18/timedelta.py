from datetime import date, time, datetime, timedelta

today = date.today()
now = datetime.now()

today_7 = today-timedelta(days=7)
print(today_7)

now_30 = now+timedelta(minutes=30)
print(now_30)

# 1. Armstromg 
# 2. Anagram
# 3. Fibonacci
# 4.Factorial
# 5.Strong Number
# 6. First non-rep character
# 7. reverse a string
# 8. Palindrome
# 9. sumofdigits
# 10. Len of number
