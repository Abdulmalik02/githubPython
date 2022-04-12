def all_subsets(S):
    """@Brief:
    A function that takes a set of integers and returns a list of all the possible subsets

    @Param:
    S       ->  A set of integers
    
    @Return:
    results ->  A list containing all the possible subsets of 'S', including {} 
    """
    #Check if S is iterable, otherwise raise an error
    try:
        iter(S)
    except:
        raise ValueError('Input is not iterable')
    # Check if S is a set, otherwise raise an error
    try:
        set(S)
    except:
        raise ValueError('Input is not a set')
    if len(S)!=len(set(S)):
        raise ValueError('Input is not a set')
    #Initialise results list
    results=list()
    #Add empty set
    results.append([])
    #Cycle through the input set
    for integer in S:
        #Check if S contains integers, otherwise raise an error
        try:
            int(integer)
        except:
            raise ValueError('Input does not contain integers')
        nextentry=list()
        #Cycle through previously calculated subsets
        for result in results:
            #Add the current integer to each previously calculated subset
            nextentry+=[result+[integer]]
        #Add the subset to the list of results
        results+=nextentry
    return results