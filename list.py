vegan_no_nos = ['eggs', 'meat', 'milk', 'figs', 'fish']

pie_ingredients = ['flour', 'apple', 'sugar', 'eggs', 'salt']

for food in pie_ingredients:
    if food in vegan_no_nos:
        print(f"OH NO CANNOT EAT {food} ITS NOT VEGAN")
    else:
        print(f"YUM< I LOVE {food}")