gmt211_2220674068: Douglas-Peucker Line Simplification
======================================================

.. image:: https://readthedocs.org/projects/douglas-peucker-algorithm-elfkc/badge/?version=latest
   :target: https://douglas-peucker-algorithm-elfkc.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Welcome to the official documentation for the **gmt211_2220674068** Python package. 

This package provides a pure Python implementation of the **Douglas-Peucker algorithm** for polyline simplification and line generalization. It is designed to reduce the complexity of spatial data (such as coastlines or trajectories) while preserving its overall geometric shape based on a user-defined threshold.

Project Context
---------------
This project has been developed as part of the **GMT 211: Data Structures and Algorithms** course at **Hacettepe University**, Faculty of Engineering, Department of Geomatics Engineering, under the supervision of **Dr. Berk Anbaroğlu**.

Applications
------------
* **GIS Map Generalization:** Reducing spatial vertex intensity for efficient rendering.
* **Cartography:** Managing multi-scale zoom levels.
* **Trajectory Compression:** Handling massive GPS or marine tracking traces.

Installation
------------
You can install this package directly from Test PyPI using the following command:

.. code-block:: bash

   pip install -i https://test.pypi.org/simple/ gmt211-2220674068

Quick Start & Usage
-------------------
To simplify spatial vectors (such as GeoJSON files or coordinate text files), you can use the main execution pipeline. Below is an example demonstrating how to compress the **Ilıca Bay** coastline dataset:

.. code-block:: python

   from dp.dp_algo import execute_douglas_peucker

   # Define dataset files and threshold configuration
   input_file = "ilica_bay.geojson"
   out_file = "out.geojson"
   epsilon = 0.01  # A higher epsilon value leads to greater simplification

   # Execute the simplification framework
   execute_douglas_peucker(input_file, out_file, epsilon)

Core API Documentation
----------------------
The package automatically extracts and formats python docstrings to render clear technical structural tables.

.. automodule:: dp.dp_algo
   :members:
   :undoc-members:
   :show-inheritance:

.. toctree::
   :maxdepth: 2
   :caption: Contents: