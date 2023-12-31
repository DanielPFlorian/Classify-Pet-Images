# Classify-Pet-Images
Classify-Pet-Images uses pretrained convolutional neural networks to classify dog breeds. The models are then evaluated to determine which CNN classifies dog breeds the best. The CNN models used are AlexNet, VGG and ResNet.

### Techniques Used

- Computing runtime costs using Time module to determine classifier efficiency
- Dictionary creation to store labels and hold classifier results
- Computing Classifier Result Statistics and printing the results
- PyTorch machine learning framework
- Shell Scripts
- ArgParse command-line app

### Command Line App Instructions

1. Clone [Classifying-Pet-Images repo](https://github.com/DanielPFlorian/classify-pet-images.git)
2. From main folder install requirements.txt with
```
pip3 install -r requirements.txt
```
3. Run commands from classify-pet-images folder with python:
```
usage: check_images.py --dir pet_images/

optional arguments:
--dir			path to folder of images
--arch			name of model architecture to use as image classifier(vgg,alexnet,or resnet)
--dogfile		name of text file with dog names
```

**Example:**
  ```
  python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
  ```
**Returns** command line output of pet label and classifier label as well as summary statistics including number of images, number of dog/not dog images, percent of correctly matched breeds and total runtime
```
Filename:Dalmatian_04017.jpg
Real:       dalmatian
Classifier: dalmatian, coach dog, carriage dog
PetLabelDog:   1
ClassLabelDog: 1

 Total Images 40 # Matches: 35 # NOT Matches: 5

 ** Statistics from calculates_results_stats() function:
N Images: 40  N Dog Images: 30  N NotDog Images: 10
Pct Corr dog: 100.0 Pct Corr NOTdog: 100.0  Pct Corr Breed:  93.3

 ** Check Statistics - calculated from this function as a check:
N Images: 40  N Dog Images: 30  N NotDog Images: 10
Pct Corr dog: 100.0 Pct Corr NOTdog: 100.0  Pct Corr Breed:  93.3


*** Results Summary for CNN Model Architecture VGG ***
N Images            :  40
N Dog Images        :  30
N Not-Dog Images    :  10

pct_match           : 87.50%
pct_correct_dogs    : 100.00%
pct_correct_breed   : 93.33%
pct_correct_notdogs : 100.00%

** Unformatted Total Elapsed Time: 6.671876430511475

** Total Elapsed Runtime: 0:0:7
```
