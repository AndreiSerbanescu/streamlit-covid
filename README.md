# streamlit-covid



### Streamlit container
Contains front-end code and coordination between
    all the other worker containers
    
### Covid Lesion Detection
Need to copy the directories code, model and output directories in
    ```covid_lesion_detection/files/source/```
    
Follow README in ```covid_lesion_detection```
   
### Covid Lesion Detection Segmentation
Need to copy the directories code, examples, model and output directories in
    ```covid_lesion_detection_seg/files/source/```
    
Follow README in ```covid_lesion_detection_seg```

### CT Muscle Segmentation
Generates mask for muscles.
    Need to copy NIH repo in the ```CTMuscleSegmentation/files/source/``` directory
    
Follow README in ```CTMuscleSegmentation```

### CT Visceral Fat
   Generates report of visceral and subcutaneous fat.
    Need to copy NIH repo in the ```CTVisceralFat/files/source``` directory
    
Follow README in ```CTVisceralFat```

### Lungmask
Generates mask for lungs.

### Lungmask - Convert
Converts dcm volumes into nifti volumes.