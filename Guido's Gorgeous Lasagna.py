EXPECTED_BAKE_TIME = 40 #expected bake time is 40mins. Define constant
PREPARATION_TIME = 2 #2mins per layer. Define constant

def preparation_time_in_minutes(number_of_layers): #takes input arguments
    
    """"
    calculates total preparation time
    """
    
    return PREPARATION_TIME * number_of_layers

def bake_time_remaining(elapsed_bake_time): 
    """calculate the total bake time remaining"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time): 
    """calculate the totalnumber of elapsed minutes including prep time and baking time"""
    return ((number_of_layers * PREPARATION_TIME) + elapsed_bake_time)
