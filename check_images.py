from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    #measures total program runtime by collecting start time
    start_time = time()
    
    #This function retrieves 3 command line arguments from user as input from
    #the user running the program from a terminal window.
    in_arg = get_input_args()

    #function that checks command line arguments using in_arg
    check_command_line_arguments(in_arg)

    #calls get_pet_labels function within the file get_pet_labels.py
    results = get_pet_labels(in_arg.dir)

    #calls function that checks Pet Images in the results Dictionary using results
    check_creating_pet_image_labels(results)

    #calls classify_images function within the file classiy_images.py
    classify_images(in_arg.dir, results, in_arg.arch)

    #function that checks Results Dictionary using results
    check_classifying_images(results)    

    #calls adjust_results4_isadog function within the file adjust_results4_isadog.py
    adjust_results4_isadog(results, in_arg.dogfile)

    #function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)

    # This function creates the results statistics dictionary that contains a
    # summary of the results statistics (this includes counts & percentages).
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)


    #calls print_results function within the file print_results.py
    print_results(results, results_stats, in_arg.arch, True, True)
    
    #measure total program runtime by collecting end time
    end_time = time()
    
    #computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time #calculate difference between end time and start time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
