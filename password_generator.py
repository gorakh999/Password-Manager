import random

def generate_pass():
    s1 = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(s1)

    s3 = list("0123456789")
    s4 = list('!#$%&()*+-/;<=>?@[\]^{|}')
 
    letter_pass = ''.join(random.choices(s1, k=8))
    number_pass = ''.join(random.choices(s3, k=2))
    punctuation_pass = ''.join(random.choices(s4, k=2))

    new_password = letter_pass + number_pass + punctuation_pass
    return new_password


# print(generate_password())

def save_password(str1):
    
    with open("data.txt", "a") as f:
        f.write(str1)
        f.write("\n")

