import os
import nipy
import numpy as np
import argparse

import time

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs


def tissue_segmentation(save_path,segmented_image, type, info):

    if info=='freesurfer' and type=="GM":
        # FreeSurfer gray matter regions
        # SupraGMV=LeftCerebralCortex+RightCerebralCortex+SubcorticalGMV
        region=np.array([42,3,10,11,12,13,17,18,26,49,50,51,52,53,54,58])


        S=nipy.load_image(segmented_image)
        name="GM_"+ os.path.basename(segmented_image)
        index=np.in1d(S._data, region).reshape(S._data.shape) # coordinates of voxels with values = values from region array
        S._data[index]=1 # set voxels values to 1
        index=np.logical_not(index) #get coordinates of voxels with values not = values from region array
        S._data[index]=0 # set voxels values to 0
        nipy.save_image(S, os.path.join(save_path,name))
    else:
        raise ValueError('Not implemented!')




if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Tissue segmentation')
    parser.add_argument("-o",required=True, type=str, help="path to save result folder")
    parser.add_argument("-s",required=True, type=str, help="segmented image")
    parser.add_argument("-type",required=True, type=str,choices=['GM'], help="segmentation type")
    parser.add_argument("-info",choices=['freesurfer'],type=str, help="type of info data")
    args = parser.parse_args()
    print args

    with Timer() as t:
        tissue_segmentation(args.o, args.s,args.type, args.info)
    print "=> time: for segmentation  %s s" %(t.secs)
