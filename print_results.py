def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
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
      results_stats_dic - Dictionary that contains the results statistics
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: 'resnet', 'alexnet', 'vgg'
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None
    """    
    print()
    print()
    print("*** Results Summary for CNN Model Architecture ", model,
          "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))
    print()
    print()

    for key, value in results_stats_dic.items():
        if key.startswith('pct_'):
                print("{:20}: {:.3f}%".format(key, results_stats_dic[key]))

    print('\n\n\n')
    
    if (print_incorrect_dogs and ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
          != results_stats_dic['n_images'] )):
          
          print("*Incorrect Dog/Not Dog Assignments:")
          print('')
          for value in results_dic.values():
                if sum(value[3:]) == 1:
                        print("{:15}: {:15}".format(value[0], value[1]))

    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        
        print('\n')
        print('*Incorrect Dog Breed Assignments:')
        print('')
        for value in results_dic.values():
                if sum(value[3:]) == 2 and value[2] == 0:
                        print("{:15}: {:15}".format(value[0], value[1]))

        





                
