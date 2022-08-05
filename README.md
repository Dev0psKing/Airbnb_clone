AirBnB Clone License: MIT Build Status
HBnB Logo

Contents
Description
Environment
Further Information
Requirements
Repo Contents
Installation
Usage
Built with
Acknowledgements
## Description 📄
This is the first phase of a four phase project, to create a basic clone of the AirBnB web app. In this first phase a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.

## Environment 💻
The console was developed in Ubuntu 20.04LTS using python3 (version 3.4.3).

Further information 📑
For further information on python version, and documentation visit python.org.

## Requirements 📝
Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 14.04, python3 and pep8 style corrector.

## Repo Contents 📋
This repository constains the following files:

## File	Description
AUTHORS             Contains info about authors of the project
base_model.py   	Defines BaseModel class (parent class), and methods
user.py 	        Defines subclass User
amenity.py	        Defines subclass Amenity
city.py	            Defines subclass City
place.py        	Defines subclass Place
review.py	        Defines subclass Review
state.py	        Defines subclass State
file_storage.py	    Creates new instance of class, serializes and deserializes data
console.py	        creates object, retrieves object from file, does operations on objects,      updates attributes of object and destroys object

test_base_model.py	unittests for base_model
test_user.py	    unittests for user
test_amenity.py	    unittests for amenity
test_city.py	    unittests for city
test_place.py	    unittests for place
test_review.py	    unittests for review
test_state.py	    unittests for state
test_file_storage.pyunittests for file_storage
test_console.py	    unittests for console
## Installation 🛠️
Clone the repository and run the console.py

$ git clone https://github.com/------/AirBnB_clone.git
## Usage 🔧
Method	Description
create	Creates object of given class
show	Prints the string representation of an instance based on the class name and id
all	Prints all string representation of all instances based or not on the class name
update	Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
destroy	Deletes an instance based on the class name and id (save the change into the JSON file)
count	Retrieve the number of instances of a class
help	Prints information about specific command
quit/ EOF	Exit the program
Example No.1
➜  AirBnB_clone git:(feature) ✗ ./console.py
(hbnb) create User
bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) show User bb4f4b81-7757-460b-9263-743c9ea6fef6
[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) update User bb4f4b81-7757-460b-9263-743c9ea6fef6 name Betty
['User', 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name', 'Betty']
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name': 'Betty', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) destroy User bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) all User
[]
(hbnb) show User
** instance id missing **
(hbnb)



# Acknowledgements 🙌
To all the peers that contribuited with their knowledge

# Authors 🖋️
Chidozie Ogwalu @gentomacine
Israel Adenuga @adexino0606
