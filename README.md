# Collections Task 1 - List basics and Waiter program

#### User story 1: I want to be able to see the menu in a formatted way so that I can order my meal

You first need to create a separate list for the starter, main and dessert. Then, print the menu for each.
```
starters = ["bread", "olives", "soup"]
mains = ["lamb", "chicken_wings", "pie"]
desserts = ["cake", "icescream", "fruits"]

menu = [starters, mains, desserts]
print (f"These are today's starters: {starters}")
print (f"These are today's mains: {mains}")
print(f"These are today's desserts: {desserts}")

```
#### User story 2: as a user, I want to be able to order three separate times and have my responses added to a list so they are not forgotten.

The user is first requested to input their order. Once included the order is added to a new list.
```     
starter_order = (input ('what would you like to order for your "Starter"?')).lower()
main_order = input ('what would you like to order for your "Main"?').lower()
dessert_order = input ('what would you like to order for your "Dessert"?').lower()

total_order = []
total_order.append(starter_order)
total_order.append(main_order)
total_order.append(dessert_order)
print(f"Your total order today is {total_order}")
```

#### User story 3: As a user, I want to have my order read back to me in a formatted way so I know what I ordered.

```
print(f"Today you have ordered starter: {starter_order}, main: {main_order} and dessert: {dessert_order}")
```


# Collections Task 2 - Hero Story

#### 1. define a dictionary
```
story1 = {
    "start": "there once was a magnificent wizzrard, the only problem is he didnt know any spells",
    "middle": "so he searched far and wide until finally he decided what he need to do",
    "end": "he needed to attend a bootcamp!!"
}
```
#### 2. print the dictionary

``print(story1)``

#### 3. print the type of your dictionary
``print(type(story1))``

#### 4. print only the keys of your dictionary

``print(story1.keys())``

#### 5. print only the values of your dictionary
``print(story1.values())``

#### 6. print the individual values using the keys
```
print(story1["start"])
print(story1["middle"])
print(story1["end"])

```
#### 7. add a new key pair
```
story1["hero"] = "yourSuperHero"
print(story1)

```

