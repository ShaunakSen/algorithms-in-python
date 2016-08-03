# USE EXCEPTION HANDLING TO FORCE USER TO ENTER A NO
import random



while True:
    try:
        number = int(raw_input("Enter a no: "))
        break
    except ValueError:
        print "You Did Not enter a no"

    except:
        print "An unknown error occurred"

print "Thank you for entering a no"

# DO WHILE SIMULATION IN PYTHON
rand_num = random.randrange(1, 10)
print rand_num

while True:
    while True:
        try:
            user_number = int(raw_input("Enter a no between 1 and 9: "))
            if 1 <= user_number <= 9:
                break
            else:
                continue
        except ValueError:
            print "You Did Not enter a no"
        except:
            print "An unknown error occurred"

    if user_number == rand_num:
        print "U guessed right!!", user_number
        break
    else:
        continue





