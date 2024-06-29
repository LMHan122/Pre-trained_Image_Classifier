def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog'.
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items:
                        index 0 = pet image label (string)
                        index 1 = classifier label (string)
                        index 2 = 1/0 (int)  where 1 = match between pet image
                        classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files.
    Returns:
           None - results_dic is mutable data type so no return needed.
    """     
    with open(dogfile, 'r') as f:
      lines = f.readlines()
    
    #creating dict
    dognames_dict = dict([key.strip(), 1] for key in lines)

    #comparing to pet image label
    for value in results_dic.values():
      if value[0] in dognames_dict:
        value.append(1)
      else:
        value.append(0)
        
    #comparing to classifier label
    for value in results_dic.values():
      if value[1] in dognames_dict:
        value.append(1)
      else:
        value.append(0)
