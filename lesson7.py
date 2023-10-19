# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 7 - Dictionaries & Sets
# Timestamp: 2:17:00

def lesson7():
    # Dictionaries
    # Used to store data values that are in key/value pairs

    band = {  # dictionaries use curly braces
        "vocals": "Plant",
        "guitar": "Page"
    }

    band2 = dict(vocals="Plant", guitar="Page")  # Using the dictionary constructor

    print(band)  # {'vocals': 'Plant', 'guitar': 'Page'}
    print(band2)  # {'vocals': 'Plant', 'guitar': 'Page'}
    print(type(band))  # <class 'dict'>
    print(len(band))  # 2 (key pairs)

    # Access items
    print(band["vocals"])  # Plant
    print(band.get("guitar"))  # Page

    # List all keys
    print(band.keys())  # dict_keys(['vocals', 'guitar'])

    # List all values
    print(band.values())  # dict_values(['Plant', 'Page'])

    # List of key/value pairs as tuples
    print(band.items())  # dict_items([('vocals', 'Plant'), ('guitar', 'Page')])

    # Verify a key exists
    print("guitar" in band)  # True
    print("triangle" in band)  # False

    # Change values
    band["vocals"] = "Coverdale"  # changed vocals to Coverdale
    band.update({"bass": "JPJ"})  # Added a new key/value pair

    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}

    # Removing items
    print(band.pop("bass"))  # returns JPJ (removes last key/value pair)
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}

    band["drums"] = "Bonham"  # Add key/value pair
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Bonham'}

    # removes last key/value pair added to the dictionary
    print(band.popitem())  # returns tuple ('drums', 'Bonham')

    # Delete and clear items
    band["drums"] = "Bonham"  # Add key/value pair
    del band["drums"]  # removes tuple ('drums', 'Bonham')
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}

    band2.clear()  # clears all key/value pairs in dictionary
    print(band2)  # {}

    del band2  # completely deletes dictionary

    # Copy dictionaries
    # How not to copy dictionaries
    band2 = band  # creates reference (which means they share memory. Modifying one modifies both.)
    print("Bad copy!")
    print(band2)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}

    band2["drums"] = "Dave"  # Adds key/value pair to both
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}

    # How to copy dictionaries
    band2 = band.copy()  # The proper way to make a dictionary copy
    band2["drums"] = "Dave"  # Adds key/value pair to both
    print("Good copy!")
    print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}
    print(band2)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}

    # Or use the dictionary constructor function
    band3 = dict(band)  # Create copy using dict constructor function
    print("Good copy!")
    print(band3)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}

    # Nested dictionaries
    # This means a key/value pair in a dictionary can be another dictionary

    member1 = {
        "name": "Plant",
        "instrument": "vocals"
    }
    member2 = {
        "name": "Page",
        "instrument": "guitar"
    }
    band = {
        "member1": member1,  # member1 dictionary as value
        "member2": member2  # member2 dictionary as value
    }
    print(band)  # {'member1': {'name': 'Plant', 'instrument': 'vocals'}, 'member2': {'name': 'Page', 'instrument': 'guitar'}}
    print(band["member1"]["name"])  # Plant (member1 is the first level deep. name is the second level deep.)

    # Sets

    nums = { 1, 2, 3, 4 }  # create set

    nums = set(( 1, 2, 3, 4 ))  # create set using set constructor function

    nums2 = set ((1,2,3,4))  # create set using set constructor function

    print(nums)  # {1, 2, 3, 4}
    print(nums2)  # {1, 2, 3, 4}
    print(type(nums))  # <class 'set'>
    print(len(nums))  # 4

    # No duplicates allowed
    nums = { 1, 2, 2, 3}  # Tried to create set with a duplicate
    print(nums)  # {1, 2, 3}

    # True is a dupe of 1 and False is a Dupe of zero
    nums = {1, True, 2, False, 3, 4, 0 }
    print(nums)  # {False, 1, 2, 3, 4} (notice it is sorted)

    # Check if a value is in a set
    print(2 in nums)  # True

    # but you cannot refer to an element in the set with an index position or a key
    # Time stamp 2:40:54

    # Add a new element to a set
    nums.add(8)
    print(nums)  # {False, 1, 2, 3, 4, 8}

    # Add elements from one set to another
    morenums = {5, 6, 7}
    nums.update(morenums)  # Adding elements from morenums to nums
    print(nums)  # {False, 1, 2, 3, 4, 5, 6, 7, 8}

    # You can use update with lists, tuples, and dictionaries, too.
    # 2:42:54

    # Merge two sets to create a new set
    one = {1, 2, 3}
    two = {5, 6, 7}

    mynewset = one.union(two)
    print(mynewset)  # {1, 2, 3, 5, 6, 7}

    # Keep only duplicates from the two sets
    one = {1, 2, 3}
    two = {2, 3, 4}
    one.intersection_update(two)
    print(one)  # {2, 3}

    # Keep everything except the duplicates
    one = {1, 2, 3}
    two = {2, 3, 4}
    one.symmetric_difference_update(two)
    print(one)  # {1, 4}
    return


if __name__ == '__main__':
    lesson7()
