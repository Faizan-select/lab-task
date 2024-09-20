#!/usr/bin/env python
# coding: utf-8

# In[4]:


def luhn_algorithm(number):
    number = number[::-1]
    total_sum = 0
    for i, digit in enumerate(number):
        digit = int(digit)
        
        if i % 2 == 1:
            digit *= 2
            print(digit)
            
            if digit > 9:
                digit -= 9
        
        
        total_sum += digit
    
    
    return total_sum % 10 == 0


def is_visa_card(number):
    
    if number.startswith("4") and 13 <= len(number) <= 19:
        return True
    return False


def validate_visa_card(number):

    number = number.replace(" ", "").replace("-", "")
    
    if not is_visa_card(number):
        return "Invalid Visa card number format"
    
    if luhn_algorithm(number):
        return "Valid Visa card"
    else:
        return "Invalid Visa card"


number = input("Enter your Visa card number: ")
print(validate_visa_card(number))


# In[9]:


import string

def remove_punctuation(user_input):
    punctuation = string.punctuation
    result = ""
    for i in user_input:
        if i not in punctuation:
            result += i
    
    return result

user_input = input("Enter a string with punctuation: ")

output = remove_punctuation(user_input)
print("String without punctuation:", output)


# In[14]:


def sort_sentense(sentense):
    tense = sentense.split()
    for i in range(len(tense)):
        for j in range(0, len(tense) - i - 1):
            if tense[j] > tense[j + 1]:
                tense[j], tense[j + 1] = tense[j + 1], tense[j]
    sorted_tense = " ".join(tense)
    return sorted_tense
user_input = input("Enter a string of words: ")
output = sort_sentense(user_input)
print("Words in alphabetical order:", output)


# In[ ]:




