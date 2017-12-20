# Force-Directed-Graph-Drawing

Some of the most flexible algorithms for calculating layouts of simple undirected graphs
belong to a class known as force-directed algorithms.<br> Also known as spring embedders,<br>
such algorithms calculate the layout of a graph using only information contained within<br>
the structure of the graph itself, rather than relying on domain-specific knowledge.<br> Graphs
drawn with these algorithms tend to be aesthetically pleasing, exhibit symmetries, and tend
to produce crossing-free layouts for planar graphs


![alt text](https://github.com/svishrut93/Force-Directed-Graph-Drawing/blob/master/Examples%20of%20Force%20Directed%20Graphs.PNG)

The file Graph2.py , implements the following preliminary algorithm for force directed graph drawing : <br>

algorithm SPRING(G:graph);<br>
place vertices of G in random locations;<br>
repeat M times<br>
calculate the force on each vertex;<br>
move the vertex c4 ∗ (force on vertex)<br>
draw graph on CRT or plotter.<br>

Attractive Force is computed by using : Hooke's Law <br>
Repulsive Forces are computed by using : Coulomb's Law <br> 


Outputs<br> 

![alt text](https://github.com/svishrut93/Force-Directed-Graph-Drawing/blob/master/Outputs/Output1.PNG)

![alt text](https://github.com/svishrut93/Force-Directed-Graph-Drawing/blob/master/Outputs/Output2.PNG)
