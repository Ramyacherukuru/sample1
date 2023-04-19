old_name = input("Enter the old_name:")
search_word = input("Enter the search_word:")
if search_word in old_name:
    print("Search success")
else:
    print("unsuccess")
replace_word = input("Enter the replace_word:")
new_name = input("Enter the new_name:")
text1 = old_name.replace(replace_word , new_name)
print(text1)

                 
