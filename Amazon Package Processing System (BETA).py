#Christopher Chong
#Student ID: 260976714


def package_in_box_fitter (box_w, box_d, box_h, pack_w, pack_d, pack_h):
    """
    Input Arguments: book_fits_in_box (int, int, int, int, int, int)
    
    Description: determines if the book of given dimensions can fit in the box of given dimensions; returns True if it can fit, False otherwise 
    
    >>> package_in_box_fitter (15, 2, 2, 2, 15, 2)
    True
    
    >>> package_in_box_fitter (10, 10, 10, 3, 15, 3)
    False
    
    >>> package_in_box_fitter (1, 1, 1, 1, 1, 1)
    True
    
    """
    if (box_w >= pack_w and box_d >= pack_d and box_h >= pack_h)  or  (box_d >= pack_w and box_h >= pack_d and box_w >= pack_h)  or  (box_h >= pack_w and box_w >= pack_d and box_d >= pack_h): # ensures package fits in box in any orientation, returns True if it fits, otherwise the function returns False
        return(True)
    
    else:
        return(False)







def retrieve_smallest_box_for_package (pack_w, pack_d, pack_h):
    """
    Input Arguments: get_smallest_box_for_book (int, int, int)
    
    Description: returns a string referring to smallest box size (out of small, medium, or large) in which a package with the given integer dimensions can fit. If the book can't fit into any size, function returns an empty string
    
    >>> retrieve_smallest_box_for_package (12, 12, 2)
    medium
    
    >>> retrieve_smallest_box_for_package  (10, 10, 1)
    small
    
    >>> retrieve_smallest_box_for_package  (15, 12, 4)
    large

    """
    if book_fits_in_box (9, 9, 1, pack_w, pack_d, pack_h): # determines if package can fit in box of "small" size 
        return ("small")
    
    elif book_fits_in_box (14, 14, 2, pack_w, pack_d, pack_h): # determines if package can fit in box of "small" size 
        return ("medium") 
    
    elif book_fits_in_box (19, 19, 3, pack_w, pack_d, pack_h): # determines if package can fit in box of "small" size 
        return ("large")
        
    else: # returns empty string if package doesn't fit in any box size 
        return ("")
        
    
        
def retrieve_num_pack_for_box (box_w, box_d, box_h, pack_w, pack_d, pack_h):
    """
    Input Arguments: get_num_books_for_box (int, int, int, int, int, int)
    
    Description: returns the maximum number of copies of a book of provided integer dimensions that are able to fit into a box of provided integer dimensions as an integer (without rotating the book)
    
    >>> retrieve_num_pack_for_box (10, 5, 5, 5, 5, 2)
    4
    
    >>> retrieve_num_pack_for_box (10, 10, 5, 2, 10, 5)
    5
    
    >>>  retrieve_num_pack_for_box (5, 3, 1, 1, 1, 1)
    15

    """
    if (box_w >= book_w and box_d >= book_d and box_h >= book_h): # since package has a fixed orientation, this determines if and how many copies of a book of given integer dimensions can fit into a box of given integer dimensions
        num_w = box_w // pack_w
        num_d = box_d // pack_d
        num_h = box_h // pack_h
        return (num_w * num_d * num_h)
        
    else:
        return ("") #returns empty string if package can't fit into box 



