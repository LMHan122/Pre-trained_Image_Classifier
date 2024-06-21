def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results using classifier's model architecture
    to classifying pet images. Results statistics add to dictionary
    (results_stats_dic) so that it's returned for printing. The statistics
    calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics where the
                     key is the statistic's name (starting with 'pct' for percentage
                     or 'n' for count) and the value is the statistic's value.
    """        
    results_stats_dic = {'n_images': len(results_dic), 'n_dogs_img': 0, 'n_notdogs_img': 0, 'n_match': 0,
                         'n_correct_dogs': 0, 'n_correct_notdogs': 0, 'n_correct_breed': 0, 'pct_match': 0,
                         'pct_correct_dogs': 0, 'pct_correct_breed': 0, 'pct_correct_notdogs': 0}

    #number of dog imgs pet image label
    for value in results_dic.values():
        if value[3] == 1:
                results_stats_dic['n_dogs_img'] += 1
        else:  #not dogs
                results_stats_dic['n_notdogs_img'] +=1
    

    #number of matches between pet & classifier labels
    results_stats_dic['n_match'] = sum(1 for value in results_dic.values() if value[2] == 1)

    #number of correctly classified dog images
    results_stats_dic['n_correct_dogs'] = sum(1 for value in results_dic.values() if value[3] + value[4] == 2)

    #number of correctly classified NON-dog images
    results_stats_dic['n_correct_notdogs'] = sum(1 for value in results_dic.values() if value[3] + value[4] == 0)

    #number of correctly classified dog breeds
    results_stats_dic['n_correct_breed'] = sum(1 for value in results_dic.values() if value[2] + value[3] == 2)

    #pct_match - percentage of correct matches
    if results_stats_dic['n_images'] > 0:
        results_stats_dic['pct_match'] = 100 * (results_stats_dic['n_match']/results_stats_dic['n_images'])

    #pct_correct_dogs - percentage of correctly classified dogs
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = 100 * (results_stats_dic['n_correct_dogs']/results_stats_dic['n_dogs_img'])

    #pct_correct_breed - percentage of correctly classified dog breeds
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_breed'] = 100 * (results_stats_dic['n_correct_breed']/results_stats_dic['n_dogs_img'])

    #pct_correct_notdogs - percentage of correctly classified NON-dogs
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = 100 *  (results_stats_dic['n_correct_notdogs']/results_stats_dic['n_notdogs_img'])


    return results_stats_dic
