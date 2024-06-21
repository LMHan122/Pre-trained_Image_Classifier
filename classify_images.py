from classifier import classifier
import os.path


def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary.
    PLEASE NOTE: This function uses the classifier() function defined in
    classifier.py.

    Parameters:
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a list containing:
                        index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                        classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: 'resnet', 'alexnet', 'vgg'
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    for key, value in results_dic.items():
        model_label = classifier(os.path.join(images_dir, key), model)
        model_label = model_label.lower().strip()

        truth = value[0]

        #if pet labels match classifier labels
        if truth in model_label:
            results_dic[key] = [truth, model_label, 1]
        #if the labels don't match
        else:
            results_dic[key] = [truth, model_label, 0]

      

      
