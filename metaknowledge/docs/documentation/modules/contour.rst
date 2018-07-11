#####################
Contour
#####################

Two functions based on *matplotlib* for generating nicer looking graphs.

This is the only module that depends on anything besides *networkx*; it depends on |numpy|_, |scipy|_, and |matplotlib|_.

.. _numpy: http://www.numpy.org/
.. |numpy| replace:: *numpy*
.. _scipy: https://www.scipy.org/
.. |scipy| replace:: *scipy*
.. _matplotlib: http://matplotlib.org/
.. |matplotlib| replace:: *matplotlib*

**The contour module provides the following functions:**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**quickVisual**\ (G, showLabel=False)

Just makes a simple *matplotlib* figure and displays it, with each node coloured by its type. You can add labels with *showLabel*. This looks a bit nicer than the one provided my *networkx*'s defaults.

**Parameters**

| *G*\ : :code:`networkx Graph`
| The graph to view.

| *showLabel*\ : :code:`optional [bool]`
| Default :code:`False`, if :code:`True` labels will be added to the nodes giving their IDs.

********************

**graphDensityContourPlot**\ (G, iters=50, layout=None, layoutScaleFactor=1, overlay=False, nodeSize=10, axisSamples=100, blurringFactor=0.1, contours=15, graphType=coloured)

Creates a 3D plot giving the density of nodes on a 2D plane, as a surface in 3D.

Most of the options are for tweaking the final appearance. *layout* and *layoutScaleFactor* allow a pre-layout graph to be provided. If a layout is not provided the |networkx_spring_layout|_ is used after *iters* iterations. Then, once the graph has been laid out a grid of *axisSamples* cells by *axisSamples* cells is overlaid and the number of nodes in each cell is determined, a gaussian blur is then applied with a sigma of *blurringFactor*. This then forms a surface in 3 dimensions, which is then plotted.

If you find the resultant image looks too banded raise the the *contours* number to ~50.

**Parameters**

| *G*\ : networkx Graph
| The graph to be plotted

| *iters*\ : ``optional [int]``
| Default :code:`50`, the number of iterations for the spring layout if *layout* is not provided.

| *layout*\ : ``optional [networkx layout dictionary]``
| Default :code:`None`, if provided will be used as a layout of the graph, the maximum distance from the origin along any axis must also given as *layoutScaleFactor*, which is by default :code:`1`.

| *layoutScaleFactor*\ : ``optional [double]``
| Default :code:`1`, The maximum distance from the origin allowed along any axis given by *layout*, i.e. the layout must fit in a square centered at the origin with side lengths 2 * *layoutScaleFactor*

| *overlay*\ : ``optional [bool]``
| Default :code:`False`, if :code:`True` the 2D graph will be plotted on the X-Y plane at Z = 0.

| *nodeSize*\ : ``optional [double]``
| Default :code:`10`, the size of the nodes dawn in the overlay

| *axisSamples*\ : ``optional [int]``
| Default 100, the number of cells used along each axis for sampling. A larger number will mean a lower average density.

| *blurringFactor*\ : ``optional [double]``
| Default :code:`0.1`, the sigma value used for smoothing the surface density. The higher this number the smoother the surface.

| *contours*\ : ``optional [int]``
| Default 15, the number of different heights drawn. If this number is low the resultant image will look very banded. It is recommended this be raised above :code:`50` if you want your images to look good. **Warning**\ : this will make them much slower to generate and interact with.

| *graphType*\ : ``optional [str]``
| Default :code:`'coloured'`, if :code:`'coloured'` the image will have a destiny based colourization applied, the only other option is :code:`'solid'` which removes the colourization.

.. _networkx_spring_layout: https://networkx.github.io/documentation/latest/reference/generated/networkx.drawing.layout.spring_layout.html
.. |networkx_spring_layout| replace:: networkx.\ **spring_layout**\ ()

********************

