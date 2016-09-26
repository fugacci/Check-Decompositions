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
the number of vertices and of top simplices of the simplicial complex in input, 
the information about the 1-homology of the intersection of each standard decomposition,
the time required to perform the computation.

<br />

#####File Formats


Simple ASCII file containing the explicit representation of vertices and triangles


```
ply
format ascii 1.0
element vertex 2903                         %number of vertices    
property float32 x
property float32 y
property float32 z
element face 5804                           %number of triangles
property list uint8 int32 vertex_indices
end_header
0.605538 0.183122 -0.472278                 %x y z coordinates
0.649223 0.1297 -0.494875
0.601082 0.105512 -0.533343
0.691245 0.0569483 -0.524762
.
.
.
3 0 1 2                                    %number of vertices per face and
3 1 3 4                                    %index of each vertex composing
3 5 6 2                                    %the face
3 6 7 8
3 7 9 10
3 1 0 11
3 9 7 12
3 12 7 6
```

######.json

JSON file containing the persistence pairs to be visualized

```
{"pairs": [                                 %two arrays containing for each pair
  {"h0":[368,569,                           %coordinates in the scatterplot  
         0.0772813,0.0281013,-0.0100251,    %coordinates of vertex1
         0.0472315,0.00624197,-0.00777435]  %coordinates of vertex2
  },
  {"h1":[1153,1356,
         0.0488116,0.00942118,0.00385671,
         0.0777883,0.0312677,0.00995619,
         1638,1640,
         -0.00850592,0.0874782,0.0400173,
         -0.00703915,0.0241465,0.039699]
 }
]}
```
<br /><br />


####Attribution
***

If you use our package in your project we encourage you to cite our work.
The visualization tool has been published in:

```
  @article{VisualizePH,
    author       = {D. Bolognini, U. Fugacci},
    title        = {Persistent homology: a step-by-step introduction for newcomers},
    month        = September,
    year         = 2016
  }
```
