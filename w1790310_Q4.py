# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1790310 / SE20191050

# Date: 17/04/2020

# Part 4 – Alternative Staff Version

def intro():
    print("This program allows you to predict the progression outcome for multiple students at the end of each academic year. Relevant data will be accessed from a list.\n")
def histogram():
    print("\nProgress",str(progress)+":","*"*progress)   #each star represents a student who achieved a progress outcome in the particular category
    print("Trailing",str(trailing)+":","*"*trailing)
    print("Retriever",str(retriever)+":","*"*retriever)
    print("Excluded",str(excluded)+":","*"*excluded,'\n')
    print(len(cred_list),"outcomes in total.")

intro()

#below variables are created and set to zero to count the corresponding outcomes for each category  
progress=0
trailing=0
retriever=0
excluded=0

#The data held in this list match the test cases 1 to 10 shown in the appendix
cred_list=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

for i in range(len(cred_list)):
    pass_cred=int(cred_list[i][0])   #this for loop matches the elements in each sublist to the corresponding variable
    defer_cred=int(cred_list[i][1])
    fail_cred=int(cred_list[i][2])

    if pass_cred==120:
        print("Progress")
        progress+=1   #each outcome would add '1' to the variable of the corresponding category

    elif pass_cred==100 and 0<=defer_cred<=20 and 0<=fail_cred<=20:
        print("Progress – module trailer")
        trailing+=1

    elif 0<=pass_cred<=80 and 0<=defer_cred<=120 and 0<=fail_cred<=60:
        print("Do not progress – module retriever")
        retriever+=1

    elif 0<=pass_cred<=40 and 0<=defer_cred<=40 and 80<=fail_cred<=120:
        print("Exclude")
        excluded+=1

histogram()

print("\nProgress","Trailing","Retriever","Excluded")
for x in range(max(progress, trailing, retriever, excluded)):   #string formatting is used to structure the output positions for each line
    print("    {0}       {1}         {2}        {3}".format('*' if x<progress else ' ','*' if x<trailing else ' ','*' if x<retriever else ' ','*' if x<excluded else ' '))
