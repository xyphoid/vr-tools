# 
# For rotating equirectangular images. Extracting two parts AB then stitch them together as BA
# 
# A is [width]x[height]+0+0'
# B is [totalwidth - width]x[heigh]+[width]+0

import sys,os

# find image height/width - TODO
width = 5906
height = 2953

if len(sys.argv) != 3:
  print("Usage: reorient.py [image] [pixels]")
  exit()

divider = int(sys.argv[2])
read = sys.argv[1]

# Read file.jpg, write out file_offset1000.jpg 
parts = read.split(".")
write = parts[0] + '_offset' + ("%d"%divider) + "." + parts[1]

cmd = "convert  \( -extract \"%dx%d+%d+0\" %s \) \( -extract \"%dx%d+0+0\" %s \) +append %s" % (width - divider,height,divider,read,divider,height,read,write)

print(cmd) # debugging purposes
os.system(cmd)


