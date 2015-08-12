from validate_email import validate_email 


email = raw_input("Insert email")
is_valid = validate_email('mqd113@gmail.com')
print 'yes'
is_valid = validate_email(email, check_mx=True)
print 'word'
is_valid = validate_email(email, verify=True)
print 'hello'




