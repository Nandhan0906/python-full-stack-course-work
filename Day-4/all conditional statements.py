'''
if examples
min_balance=5000
cur_balance=4000

if cur_balance < min_balance:
    print("Send message and cut some amount")

'''



'''
data=('user@gmail.com','user@123')
mail=input("Enter the email:")
password=input("Enter the password: ")

if data == (mail,password):
    print("Login Successful")
else:
    print("Invalid Login")
'''



'''
fruits=['mango','apple','papaya','pine apple']
search_item=input("Search here: ")
if search_item in fruits:
    print(f"{search_item} found! Buy Now")
    else:
        print(f"{search_item} is out of stock, we will notify you once it is available")
'''

'''
time=int(input("Enter the buses: "))
print("Available buses are: ")
if 0<= time <=6:
         print("Adilabad\nHanumakonda\nHyderabad\nKamareddy")
if 7<= time <=12:
         print("Karimnagar\nMahabubnagar\nMedak\nWarangal")
if 13<= time <=18:
         print("Nalgonda\nNizamabad\nRangareddy\nSangareddy")
if 13<= time <=18:
         print("Suryapet\nVikarabad\nNirmal\nRajanna Sircilla")
else:
    print("Enter the time in the given range")
'''

'''
print("Welcome to uber, Book your ride")
print("1.bike")
print("2.Auto")
print("3.Cab")
choice=int(input("Choose the options: "))
if choice == 1:
           print("Hey you have booked bike successfully.\nDriver is on the way.Wear the helmet.")
elif choice == 2:
           print("Hey you have booked Auto successfully.\nDriver is on the way.Track your vehicle.")
elif choice == 3:
           print("Hey you have booked Cab successfully.\nDriver is on the way.Wear the seat belt.")
'''

login_status = True
premium_account=True
if login_status:
    print("Welcome to the hotstar")
    if premium_account:
        print("Play the video with high quality and without ads")
    else:
        print("Play the video with normal quality and with ads")
else:
    print("Invalid input")

