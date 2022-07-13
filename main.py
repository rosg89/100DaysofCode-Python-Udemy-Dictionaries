#Sintaxis correcta del diccionario
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.", 
  "Loop": "The action of doing something over and over again",
}

#Imprimir algo del diccionario
print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["List"] = "Lists are one of 4 built-in data types in Python used to store collections of data."

print(programming_dictionary["List"])

#################

#Create empty dictionary
empty_dictionary = {}
#Le agrego un item
empty_dictionary["Gato"] = "es un mamífero carnívoro de la familia Felidae."

print(empty_dictionary)

#Wipe an existing dictionary
empty_dictionary={}
print(empty_dictionary)

#################

#Edit an item in a dictionary
programming_dictionary["Bug"]="A moth in your computer"
print(programming_dictionary["Bug"])

#Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

