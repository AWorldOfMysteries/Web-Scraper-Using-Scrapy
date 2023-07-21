try:
    x = 10 / 0  
except ZeroDivisionError:
    try:
        print("Error:", str(e))
    except NameError as n:
        print("Error:", str(n))