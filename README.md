# Image Classification for a City Dog Show

## Project Description

Using a pre-trained image classifier to identify dog breeds.

## Program Outline

Run program **check_images.py in a terminal** with up to 3 arguments.
If the user fails to provide some or all of the 3 arguments, then the default 
values are used for the missing arguments. 

   Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg' (options: 'vgg', 'alexnet', 'resnet')
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'

If you want to run all 3 models, you can use the bash files in the terminal.
**run_models_batch.sh:** Runs all 3 models against pictures on drive. Outputs to a .txt file.
**run_models_batch_uploaded.sh:** Runs all 3 models against uploaded. Outputs to a .txt file.


## Other Python 

**adjust_results4_isadog.py:** script that adjusts the dictionary to determin if the classifier 
	correctly classified images 'as a dog' or 'not a dog'
**calculates_results_stats.py:** calculates statistics of the results using classifier's model 
	architecture to classifying pet images.
**classifier.py:** script that was provided along with the project
**classify_images.py:**
**get_input_args.py:**
**get_pet_labels.py:**
**print_functions_for_lab_checks.py:** script that was provided along with the project
**print_results.py:**
**test_classifier.py:**




1. **Time your program**
   - Use the Time module to compute program runtime.

2. **Get program Inputs from the user**
   - Use command line arguments to get user inputs.

3. **Create Pet Images Labels**
   - Use the pet images filenames to create labels.
   - Store the pet image labels in a data structure (e.g., dictionary).

4. **Create Classifier Labels and Compare Labels**
   - Use the Classifier function to classify the images and create the classifier labels.
   - Compare Classifier Labels to Pet Image Labels.
   - Store Pet Labels, Classifier Labels, and their comparison in a complex data structure (e.g., dictionary of lists).

5. **Classifying Labels as "Dogs" or "Not Dogs"**
   - Classify all Labels as "Dogs" or "Not Dogs" using `dognames.txt` file.
   - Store new classifications in the complex data structure (e.g., dictionary of lists).

6. **Calculate the Results**
   - Use Labels and their classifications to determine how well the algorithm worked on classifying images.
   - Print the Results.

