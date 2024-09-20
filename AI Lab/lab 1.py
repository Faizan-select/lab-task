#!/usr/bin/env python
# coding: utf-8

# In[25]:


import re

def preprocess_expression(expression):
    expression = re.sub(r'(\d)(\()', r'\1 * \2', expression)
    expression = expression.replace('÷', '/')
    expression = expression.replace('×', '*')
    
    return expression


def calculator(expression):
    try:
        processed_expression = preprocess_expression(expression)
        result = eval(processed_expression)
        return result
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    expression = input("Enter a mathematical expression: ")
    
    result = calculator(expression)
    print(f"The result of the expression '{expression}' is: {result}")


# In[ ]:





# In[ ]:




