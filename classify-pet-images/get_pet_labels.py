#!/usr/bin/env python3
# -*- coding: utf-8 -*-                                                                      
# PROGRAMMER: Daniel Florian     
# DATE CREATED: 06/21/2023                           
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    # Creates list of files in directory
    filename_list = listdir(image_dir)

    # Creates empty dictionary for the results
    results_dic = dict()

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(filename_list), 1):

       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't a pet image file
       if filename_list[idx][0] != ".":

           # Check if filename doesn't already exist as key in dictionary, otherwise print 
           # an error message because indicates duplicate files (filenames)
           if filename_list[idx] not in results_dic:

               # Creates temporary label variable to hold pet label name extracted 
               pet_label = ""

               # Sets string to lower case letters
               filename_lower = filename_list[idx].lower()

               # Splits lower case string by "_" to break into words
               filename_split = filename_lower.split("_")

               # Loops to check if word in pet name is only alphabetic characters 
               # if true append word to pet_name separated by trailing space
               for word in filename_split:
                   if word.isalpha():
                       pet_label += word + " "
               
               # Strip off starting/trailing whitespace characters
               pet_label = pet_label.strip()

               # Add filename as key and pet_label as value to results_dic
               results_dic[filename_list[idx]] = [pet_label]

           else:
               print("** Warning: Key=", filename_list[idx], 
               "already exists in results_dic with value =", 
               results_dic[filename_list[idx]])
       else:
           print("Skipping {} because it is not a pet image file".format(filename_list[idx]))

    return results_dic
