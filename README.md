Assessment aim: 
The aim is to check if the specimen/test piece dia is 6.0 mm or permissible or not and to print out the diameter value.

Approach: 
As the specimen is standing on a workbench/reference table. First, find the horizontal length, i.e., the bench's width, say w1 in pixels, and find the specimen's width/diameter, say w2. 
Also, we have several okay images having a diameter of precisely 6.0mm.  Referring to that, by finding the w2:w1 ratio, we found the bench width to be 38.739 mm roughly.
Considering these values, by calculating the w2/w1 value and bounding it, such that the specimen width/diameter lies in a specific range, say 5.925 mm to 6.075 mm, we can find if the specimen diameter is okay/permissible or not.

Libraries used:
- OpenCV
- OS

Dataset files:
I could not upload the entire dataset as there is a limit to upload less than 25MB of files only.

Features:
- The code can scan the specific required file.
- It can print out if the specimen diameter is permissible or not.
- It can print out the precise diameter of the specimen as calculated by the code.
- It can also show the images having the bounding rectangles as chosen, i.e., outlining the specimen and the bench.
- It will also print out the directory path it is currently working in
