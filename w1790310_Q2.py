# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1790310 / SE20191050

# Date: 17/04/2020

# Part 2 - Staff Version 

def intro():
    print("This program allows you to predict the progression outcome for multiple students at the end of each academic year\n")
def error():
    print("Range error")
def histogram():
    print("\nProgress",str(progress)+":","*"*progress)   #each star represents a student who achieved a progress outcome in the particular category
    print("Trailing",str(trailing)+":","*"*trailing)
    print("Retriever",str(retriever)+":","*"*retriever)
    print("Excluded",str(excluded)+":","*"*excluded)
    print('\n'+str(total),"outcomes in total.")

intro()

#below variables are created and set to zero to count the corresponding outcomes for each category  
progress=0
trailing=0
retriever=0
excluded=0
total=0

while True:
    finish=input("Enter 'q' to quit: ")
    finish=finish.upper()   #this makes uppercase and lowercase both valid inputs
    finish=finish.lower()

    if finish=="q":   #when 'q' is entered by the user program would quit and the histogram would be produced
        break   
    else:
        try:
            pass_cred=int(input("\nEnter your number of credits at Pass: "))
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
                print("Progress")
                progress+=1   #each outcome would add '1' to the variable of the corresponding category and the total
                total+=1

            elif pass_cred==100 and 0<=defer_cred<=20 and 0<=fail_cred<=20:
                print("Progress – module trailer")
                trailing+=1
                total+=1

            elif 0<=pass_cred<=80 and 0<=defer_cred<=120 and 0<=fail_cred<=60:
                print("Do not progress – module retriever")
                retriever+=1
                total+=1

            elif 0<=pass_cred<=40 and 0<=defer_cred<=40 and 80<=fail_cred<=120:
                print("Exclude")
                excluded+=1
                total+=1

        except ValueError:
            print("Integers required")   #data type of credit inputs should be integer and integer only
            
histogram()
