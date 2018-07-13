Find: <code class="highlighter-rouge">([^<>]*)</code>
Replace: :code:`$1`


Switching italics from md to rst
Find: _([^ ]*)_
Replace: *$1*

Switching code from md to rst
Find:  `([^ ]*)`
Replace: :code:`$1`

Linking to an ID:

|paragraph|_

.. _paragraph: #my-id
.. |paragraph| replace:: **paragraph**

.. container::
    :name: my-id

    a paragraph
