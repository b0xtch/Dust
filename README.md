# Dust
Dust is a python program that predicates weather conditions given a set of images as well as a set if weather.

## Installation
**Requirements(python modules):**
 
`Python 3``Sklearn``OpenCV``Pandas``Numpy``Glob`


---


**Usage**

```bash
python3 dust.py <weather_dir> <image_dir>
```
The command will trigger the module class dust.py that relies on the other two module/classes: etl.py and atom.py. There will be a log in the command line to for updates.

---


**Output**

There will be an output folder that contains two files, one png image (sample.png) with a random sample of predicated images and a csv file (summary.csv) with a summary of the results.

