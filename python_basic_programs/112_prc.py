def user_details(first_name,last_name,phone_num,address,job, middle_name='',job_loc=''):

    return first_name,middle_name,last_name,phone_num,address,job,job_loc

first_name=input("Enter your first_name:")
last_name=input("Enter your last_name:")
phone_num=input("Enter your phone_num:")
address=input("Enter your address:")
job=input("Enter your job:")
job_loc=input("Enter your job_loc:")
middle_name=input("Enter your middle_name:")

print(user_details( phone_num,address,job,job_loc))