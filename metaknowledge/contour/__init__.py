#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015


"""Two functions based on *matplotlib* for generating nicer looking graphs.

This is the only module that depends on anything besides *networkx*; it depends on |numpy|_, |scipy|_, and |matplotlib|_.

.. _numpy: http://www.numpy.org/
.. |numpy| replace:: *numpy*
.. _scipy: https://www.scipy.org/
.. |scipy| replace:: *scipy*
.. _matplotlib: http://matplotlib.org/
.. |matplotlib| replace:: *matplotlib*
"""


# """Two functions based on _matplotlib_ for generating nicer looking graphs
#
# This is the only module that depends on anything besides _networkx_, it depends on [_numpy_](http://www.numpy.org/), [_scipy_](https://www.scipy.org/) and [_matplotlib_](http://matplotlib.org/).
# """

from .plotting import graphDensityContourPlot, quickVisual
