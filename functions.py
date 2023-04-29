def greet(name):
    return f"Hello there, {name}"


def divide(a,b):
    if type(a) is int and type(b) is int:
        return a / b
    return 'a and b must be integers!'

def three_things(a,b,c):
    print('hi')

def send_email(to_email, from_email, subject, body):
    """add a to email, a from email, a subject, and a body to the parenths"""
    email= f'''
        to: {to_email}
        from: {from_email}
        subject: {subject}
        --------------------
        body: {body}
    '''
    print(email)
# Python does care about the order you pass in the arguements but if you declare the arguement with an equal then it does not matter about order
send_email(subject="Homework", to_email="springboard@usf.com", from_email="michael.aylmer@yahoo.com", body="HI Springboard i cant wait to graduate!")

# you can also pass in a defined value to the functions like in JavaScript.
def power(num, power=2):
# default values must come at the end of the parameter list.
    return num**power