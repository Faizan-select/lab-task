#!/usr/bin/env python
# coding: utf-8

# In[7]:


def FizzBuzz():
  print(""" 
        ----Fizzbuzz----
        
    Here is a new Game of fizzbuzz.

       """)
  enter_number = set()
  while True:
    num = int(input("enter a number "))
       
    if num in enter_number:
        print("you have already entered the number")
        continue
    enter_number.add(num)


    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print("Not a fizz buzz ") 
        break   
 
 
FizzBuzz()


# In[5]:


movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

def get_budgets(movies):
    budget = []
    for i in movies:
        budget.append(i[1])
    return budget

def Avg_Budget(budget):
    return sum(budget) / len(budget)

def high_budget(moveis, average_budget):
    high = []
    for movie, budget in movies:
        if budget > average_budget:
            high.append((movie, budget))
            
    # Count of high budget movies
    count_high_budget = len(high)
    for movie, budget in high:
        print(f"{movie}: {budget:,} ({budget - average_budget:,.2f} above average)")
    
    return count_high_budget  # Return the count of high budget movies
    
def add():
    num_movie = int(input("enter the number of movie you want to add "))
    new_movie = []
    for i in range(num_movie):
        name = input("Enter name of the movie you want to add")
        budget = int(input("enter budget of the movei in numbers"))
        new_movie.append((name,budget))
    return new_movie   

    


def main():
    new_movie = add()
    movies_list = movies + new_movie
    
    budget = get_budgets(movies_list)
    avarage_budget = Avg_Budget(budget)
    
    print(f"Average budget: {avarage_budget:,.2f}")
    count_high_budget = high_budget(movies_list, avarage_budget)
    print(f"Number of movies with budgets higher than the average: {count_high_budget}")

    
main()


# In[ ]:




