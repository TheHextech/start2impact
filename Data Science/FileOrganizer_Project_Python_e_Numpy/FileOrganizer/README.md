# General info

This project consists of a few scripts for managing various types of files, with which you will put into practice your Python and numpy skills.

It is not **said that you already know all the constructs and libraries you will need to use to complete the project: it is part of the game!**


---

## Step 1
Start by creating, in a notebook, a Python script that iterates alphabetically on the files in the folder and, depending on the type (audio, document, image), move them to the relevant subfolder (see an example below). If the subfolder does not exist, your script will have to create it automatically.

During the cycle, the script must print the file information: name, type and size in bytes. This is the desired output:

	bw type:image size:94926B
	hello type:doc size:12B
	Daffodil type:image size:24657B
	eclipse type:image size:64243B
	foo type:doc size:8299B
	song1 type:audio size:1087849B
	song2 type:audio size:764176B
	trump type:image size:10195B

In addition to printing information as you move it, keep track of files by creating a document _recap.csv_ with the same information. Find an example in this folder.

The final structure of the files folder should be:

```
    - files                       
        - audio
            - song1.mp3
            - song2.mp3
        - docs
            - ciao.txt
            - foo.odt
        - images
            - bw.png
            - Daffodil.jpg
            - eclipse.png
            - trump.jpeg    
        - recap.csv

```

Comment the code with the steps you take. This also applies to the next Steps.

**Warning**: Every time the script is launched to move new files, it must _update_ (and not overwrite) the subfolders and the recap file. To check that everything is working properly, you can add more files to the files folder and do a test; or, you can split the 8 original files into two groups and leave one for testing.

**Tip**: You can use the libraries _os_, _shutil_ and _csv_.

So, in summary, you have to iterate alphabetically on the files of the files folder:
- Depending on the type, move them to its subfolder (if it does not exist, create it automatically)
- print the file info and store it in a recap.csv file
- the script launched must move new files, not just the sample ones, updating the subfolders and the recap file

---

## Step 2
Insert the script you created into a small executable (call it _addfile.py_ and place it in this folder, next to the notebook) with a command line interface (CLI).

The purpose of the executable is to move a single file (located in the files folder) to the relevant subfolder, updating the recap.

The interface of the executable has as its only argument (mandatory) the name of the file to be moved (including format, es: 'trump.jpeg'). In case the file passed as argument does not exist, the interface must notify the user.

**Tip**: In addition to the above, you can use the libraries _sys_ and _argparse_.

---

## Step 3

A grayscale image has only one color layer, an RGB has 3, an RGBA 4 (the last one is called the _alpha_channel).

The _Image_ module of the _PIL_ library allows you to load an image, which can be transformed into a numpy array through the _np.array_ function. From this array, you can see whether the loaded image is grayscale, RGB or RGBA.

Add a script to the Step 1 notebook that iterates on the _images_ subfolder and constructs a summary table like this (produced with the _tabulate_ library):

In addition to the file name, the table shows:

-   image height, in pixels
-   image width, in pixels
-   If the image is grayscale, the _grayscale_ column indicates the average of the values of the single color layer
-   If the image is in color, the other columns indicate the average of the values of each color level.

---

**Corrected on 2021-12-07.  Exceeded with 500/500**.