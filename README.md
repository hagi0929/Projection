# Projection
## how to use
### Class
#### Projection - has two paramemter VertexListOfPolyhedron and ThreeCoordinateListOfThePlain and one method execute.
#### parameters
VertexListOfPolyhedron - list of the Polyhedron's coordinate
ThreeCoordinateListOfThePlain - list (len: 3) of the three coordinate that can form a plain 
### Methods
#### execute - a method which reterns list of the Polyhedron's coordinate projected on plain. has no parameter 
### Example
```
test = Projection( VertexListOfPolyhedron, ThreeCoordinateListOfThePlain)
for coordinate in test.execute():
  print(coordinate)
```
## demonstration
This is a program that displays a coordinate of the vetex of a polyhedron projected in to a plain on euclidean space.
This is the demonstration of this program.
lets say we have hexahedron (can be any figure as long as there is no colliding line segment) in the euclidean space defined by coordinates O{(4,5,5),(1,5,5),(1,1,5),(4,1,5),(4,5,1),(1,5,1),(1,1,1),(4,1,1)} and this hexahedron would look like this. 
![image](https://user-images.githubusercontent.com/72693376/179253448-a4455547-c823-4125-8cc6-d44e9f71d9e3.png)then we are going to display 2d plain where the vertexs of the polyhedron be displayed. lets say a plain would be defined by three points L, M, N = [(0,4,0), (4,0,0), (0,0,1)] then the plain would look like this
![image](https://user-images.githubusercontent.com/72693376/179253621-8fe5ec5e-1628-4323-a540-5d79952e562b.png)knowing that our goal is to find a coordinate of these vertexs when it is diaplayed in the 2d plain. we are going to visualize the projection. (the values that we are going to get are P in the figure below)
![image](https://user-images.githubusercontent.com/72693376/179253178-5730c910-0928-4b19-baa8-76eacabf395e.png)
this is the result made from mathlab (this values can't be wrong) 
![image](https://user-images.githubusercontent.com/72693376/179256066-0d366799-e87f-403b-9d07-127b2bc65477.png)

This is the execution of my code inputting the same value as the mathlab, and by comparing both datas we can say both of the values are identical (assuming that both datas are going to be round off to the tenth values)
![image](https://user-images.githubusercontent.com/72693376/179254458-580af51c-fe8c-4af5-8142-8b9a48a6a1fc.png)
![image](https://user-images.githubusercontent.com/72693376/179254487-3d3777e5-1083-4995-b018-843b628f9304.png)

## solution
[handwritten solution](https://github.com/hagi0929/Projection/files/9122123/Solution.pdf)
