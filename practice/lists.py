
#2D list generation

list_a=["hello",1.5,5,"world"]
list_b=["this","place","is",6.7]
list_c=[12,"grand",8,-1]
list_d=["great","scott",11,"world"]

list_all=[list_a,list_b,list_c,list_d]




#function to find a interger in a list and display list


def find_integer_in_list_of_list(list_to_search, integer):

    if (isinstance(integer,int)==False):
        print(" {0} is not an integer. Please choose an integer to look for".format(integer))
        return False
    elif(isinstance(list_to_search,list)==False):
        print(" That does not appear to be a list. Please choose a list to search")
        return False
        
    for lists in list_to_search:
        for element in lists:
            if(element ==integer):
                print("found")
                print(lists)
                return True
            
    print("Integer was not in the list")
    return False
                

#Unit Tests

find_integer_in_list_of_list(list_all, 2.2)
find_integer_in_list_of_list(5, 2)
find_integer_in_list_of_list(list_all, 10)
find_integer_in_list_of_list(list_all, 11)    
    
    
    
