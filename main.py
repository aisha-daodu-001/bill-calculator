print("Enter the type of bill you want to calculate:")
print("1. Electricity")
print("2. Water")

bill = int(input("Enter the type of bill you want to calculate: "))

if bill == 1:
    try:
        amount = int(input("Enter your electric meter reading in kwH: "))
        per_person = int(input('Enter the number of people in household-max 20 people: '))
        print('Calculating electricity bill...')
        if amount <= 100:
            bill_rate = amount * 5
            per_personrate = bill_rate/per_person 
            print('Your total Electricity bill is $',bill_rate )
            if per_personrate <= 200:
                print('Your per person rate is', per_personrate ,'This is considered normal')
            elif per_personrate > 200:
                print('Your per person rate is', per_personrate ,'This is considered above average')
        elif amount > 100 and amount <= 1000:
            bill_rate = amount * 5
            per_personrate = bill_rate/per_person 
            print('Your total Electricity bill is $',bill_rate )
            if per_personrate <= 200:
                print('Your per person rate is', per_personrate ,'This is considered normal')
            elif per_personrate > 200:
                print('Your per person rate is', per_personrate ,'This is considered above average')
        elif amount > 1000:
            bill_rate = amount * 5
            per_personrate = bill_rate/per_person 
            print('Your total Electricity bill is $',bill_rate )
            if per_personrate <= 200:
                print('Your per person rate is', per_personrate ,'This is considered normal')
            elif per_personrate > 200:
                print('Your per person rate is', per_personrate ,'This is considered above average')
    except:
          print('Error: Please enter a numerical meter reading')
if bill == 2:
      try:
          amount = int(input("Enter your water meter reading in m^3: "))
          per_person = int(input('Enter the number of people in        6household-max 20 people: '))
          print('Calculating water bill...')
          if amount <= 500:
            bill_rate = amount * 50
            per_personrate = bill_rate/per_person 
            print('Your total Electricity bill is $',bill_rate )
            if per_personrate <= 200:
                print('Your per person rate is', per_personrate ,'This is considered normal')
            elif per_personrate > 200:
                print('Your per person rate is', per_personrate ,'This is considered above average')
          elif amount > 500 and amount <= 2500:
            bill_rate = amount * 60
            per_personrate = bill_rate/per_person 
            print('Your total Electricity bill is $',bill_rate )
            if per_personrate <= 200:
                print('Your per person rate is', per_personrate ,'This is considered normal')
            elif per_personrate > 200:
                print('Your per person rate is', per_personrate ,'This is considered above average')
          elif amount > 2500:
            bill_rate = amount * 70
            per_personrate = bill_rate/per_person 
            print('Your total Electricity bill is $',bill_rate )
            if per_personrate <= 200:
                print('Your per person rate is', per_personrate ,'This is considered normal')
            elif per_personrate > 200:
                print('Your per person rate is', per_personrate ,'This is considered above average')
      except:
          print('Error: Please enter a numerical meter reading')

else:
      print('Error: enter a number to choose a bill type from the list')
