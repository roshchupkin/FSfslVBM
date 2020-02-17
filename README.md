# FSfslVBM
Small wrapper for running voxel-based morphometry (VBM) based on FreeSurfer segmentation 

1) Using git, clone this repository git clone https://github.com/roshchupkin/FSfslVBM.git
 
2) Here is the dropbox folder: https://www.dropbox.com/sh/q6lfaft0xx50zq7/AADjW99S8kHWQaJzOxNfkxE0a?dl=0
Download everything to the main folder of repository from (1) 
 
3) You need to run fsl_vbm_pipeline.sh script for all images like this (if you have cluster just run one job per image):

sh fsl_vbm_pipeline.sh \   
-i ${aseg.mgz image from freesurfer segmentation} \   
-f ${FreeSurfer system path} \   
-v ${path to folder with VBM pipeline scripts, template, mask } \  
-o ${path to save results} \   
-n ${uniq name for image} \  



As the result, save folder should contain several files per image, the main result *_GM_mod_s3.nii.gz file. This is subject GM image in MNI space smoothed with 3mm kernel. The FSL registration could take some time (several hours per image).  

4) In dropbox folder, there is a file HOWTO prepare phenotypes. Just follow the instruction. NOTE, that last step requires HASE to be installed (see first step from genetics part). 

 
After that steps you can use data yourself, for VBM (https://github.com/roshchupkin/VBM) or for vGWAS if you have genetics.  
 
