# streamlit-covid

There is a need for medical imaging processing tools in order to aid front-line care and research during the ongoing SARS-CoV-2 pandemic. Quantitative image-derived information can be used for the better understanding of the Covid-19 disease, for the better development of treatments and ultimately as a help for clinical decision-making.

We have built an application that interfaces clinicians with powerful state- of-the-art machine learning algorithms, which can be securely deployed in a hospital’s in-house software infrastructure, providing an easy-to-use, web-based graphical interface and being simple to integrate in a clinical workflow. Our application provides automatic lesion detection and segmentation of the lungs, segmentation of muscle tissue, lung density information and measurements of subcutaneous and visceral fat.

We believe our application could become an important tool for clinicians to use in managing the SARS-CoV-2 pandemic. It could pave the way for future developments in software platforms for medical imaging, helping the translation of algorithms from research into the clinical context.


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
