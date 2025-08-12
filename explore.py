import os, glob
from collections import Counter
labels = glob.glob("dataset_yolo/labels/train/*.txt") + glob.glob("dataset_yolo/labels/val/*.txt")
cnt = Counter()
for f in labels:
    with open(f) as fh:
        for line in fh:
            cls = int(line.split()[0]); cnt[cls]+=1
print("Per-class object counts:", cnt) 


