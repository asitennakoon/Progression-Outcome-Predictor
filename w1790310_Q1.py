# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1790310 / SE20191050

# Date: 17/04/2020

# Part 1 - Student Version

def intro():
    print("This program allows you to predict your progression outcome at the end of each academic year.\n")
def error():
    print("Range error")

intro()

while True:
    try:
        pass_cred=int(input("Enter your number of credits at Pass: "))
        if pass_cred not in range(0, 121, 20):   #credits should be in the range 0, 20, 40, 60, 80, 100 and 120 
            error()
            continue
        defer_cred=int(input("Enter your number of credits at Defer: "))
        if defer_cred not in range(0, 121, 20):
            error()
            continue
        fail_cred=int(input("Enter your number of credits at Fail: "))
        if fail_cred not in range(0, 121, 20):
            error()
            continue

        #total of pass, defer and fail credits should be 120
        if pass_cred+defer_cred+fail_cred!=120:
            print("Total incorrect")    

        elif pass_cred==120:
            print("\nProgress")
            break

        elif pass_cred==100 and 0<=defer_cred<=20 and 0<=fail_cred<=20:
            print("\nProgress – module trailer")
            break

        elif 0<=pass_cred<=80 and 0<=defer_cred<=120 and 0<=fail_cred<=60:
            print("\nDo not progress – module retriever")
            break

        elif 0<=pass_cred<=40 and 0<=defer_cred<=40 and 80<=fail_cred<=120:
            print("\nExclude")
            break

    except ValueError:
        print("Integers required")   #data type of credit inputs should be integer and integer only
