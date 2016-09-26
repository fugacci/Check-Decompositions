# Check Decompositions
Tool for checking if a simplicial 2-complex with non-null top homology is non-trivially decomposable.

####Quick Start
***

The Python code can be simply executed by writing the following command line:

```
python CheckDecompositions.py
```

Then, the user has to enter the file name of the simplicial complex to be tested. For instance: 

```
Enter name of file in input: ProjectivePlane
```

Program returns as output:
* the number of vertices and of top simplices of the simplicial complex in input, 
* the information about the 1-homology of the intersection of each standard decomposition,
* the time required to perform the computation.

Example:

```
Number of vertices is 6
Number of top simplices is 4
There exist both decompositions having intersection with null 1-homology and decompositions having intersection with non-null 1-homology
Required time: 0.0 seconds
```


####File Formats
***

Simplicial 2-complexes in input have to be expressed in a text file.
Accepted input files have to contain the number of vertices of the simplicial complex as long as the list of its top 2-simplices.  For instance:


```
6              %number of vertices 
1 2 4
1 2 5
1 3 5
1 3 6
1 4 6
2 3 4
2 3 6
2 5 6
3 4 5
4 5 6
```


####Attribution
***

If you use our package in your project we encourage you to cite our work.
Please use the following reference:

```
  @article{VisualizePH,
    author       = {D. Bolognini, U. Fugacci},
    title        = {Betti splitting from a topological point of view},
    month        = {September},
    year         = {2016}
  }
```
