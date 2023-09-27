# pouzit switch
# zo vstupu sa bude pytat aky je den v tyzdni
# vypisat podla toho napr happy monday, taco tuesday, its wednesday dudes etc...
# konverzia lower upper case

day = input("Please, what day is today?\n")
day_converted = day.lower()
#print(day_converted)

match day_converted:
    case "monday":
        print("Mondays are the start of the work week which offer new beginnings 52 times a year!")
    case "tuesday":
        print("Blame it on Tuesday.")
    case "wednesday":
        print("Elephants love Wednesday, and so will you.")
    case "thursday":
        print("You can quit anything on a Thursday.")
    case "friday":
        print("Friday afternoon feels like heaven.")
    case "saturday":
        print("Live every day as if it were Saturday night.")
    case "sunday":
        print("Warning: Going to sleep on Sunday will cause Monday.")
    case _:
        print("Please, provide valid day (e.g. Friday).")