import random
import string


domain_list=['gmail.com', 'yahoo.com','outlook.com']
email_list=[]
email_len=11
letters=string.ascii_lowercase
for domain in domain_list:
    for i in range(5):
        random_string=''.join(random.choice(letters) for i in range(email_len))
        email=random_string + str(random.randint(10,20)) +"@" + domain
        email_list.append(email)

print(email_list)
with open('./email_output.txt', 'w') as f:
    for i in email_list:
      f.write(i+'\n')

''' or with open('./email_output.txt', 'w') as f:
       allemail='\n'.join(email_list)
       f.write(allemail) '''

