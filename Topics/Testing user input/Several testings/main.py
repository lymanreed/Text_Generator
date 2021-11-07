def check(num_apples):
    try:
        print(num_apples if int(num_apples) >= 202 else
              "There are less than 202 apples! You cheated me!")
    except ValueError:
        print("It is not a number!")
