gmt211_2220674068: Douglas-Peucker Line Simplification Framework
===============================================================

.. image:: https://readthedocs.org/projects/douglas-peucker-algorithm-elfkc/badge/?version=latest
   :target: https://douglas-peucker-algorithm-elfkc.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Welcome to the formal technical documentation for the **gmt211_2220674068** Python package. This library offers a high-performance, pure Python implementation of the classic **Douglas-Peucker (DP) algorithm** for polyline simplification and spatial line generalization.

Introduction
--------------------
This package was designed, tested, and packaged as a final project component for the course **GMT 211: Data Structures and Algorithms** within the Department of Geomatics Engineering, Faculty of Engineering at **Hacettepe University**.

Formal Problem Definition
-------------------------
In spatial data analysis, cartography, and Geographic Information Systems (GIS), digital curves or polylines are frequently represented as an ordered sequence of vertices. Real-world spatial captures (such as high-resolution coastlines or raw GPS trajectories) often exhibit a significant surplus of coordinates. This high density increases computational overhead, spatial storage requirements, and map-rendering latency.

Mathematically, given an initial polyline :math:`P` defined as an ordered sequence of :math:`n` distinct Cartesian points:

.. math::

   P = \{p_1, p_2, \dots, p_n\}

where each vertex :math:`p_i = (x_i, y_i)`. The primary objective of line generalisation is to compute an approximate polyline :math:`P'` consisting of a subset of the original vertices:

.. math::

   P' = \{p'_1, p'_2, \dots, p'_m\} \quad (m \le n)

such that the global geometric shape and topological characteristics of the original line are preserved, ensuring that the spatial deviation of any omitted point does not exceed a user-specified threshold or tolerance parameter, denoted as epsilon (:math:`\epsilon`).

The Algorithmic Workflow
------------------------
The Douglas-Peucker algorithm employs a top-down, recursive divide-and-conquer strategy to prune redundant vertices. The structural workflow proceeds as follows:

1. **Base Case Verification:** If the input sequence contains two or fewer points (:math:`n \le 2`), no further simplification is mathematically possible. The segment is returned immediately.
2. **Baseline Anchor Establishment:** A temporary linear segment is constructed by connecting the terminal anchors: the initial vertex (:math:`p_1`) and the final vertex (:math:`p_n`).
3. **Perpendicular Distance Computation:** The algorithm iterates through all intermediate vertices :math:`p_i` (where :math:`1 < i < n`) and computes their exact perpendicular distance to the baseline chord :math:`\overline{p_1 p_n}`.
4. **Maximum Offender Isolation:** The vertex exhibiting the maximum perpendicular distance (:math:`d_{max}`) from the baseline is isolated, and its index is cached:
   
   .. math::

          d_{max} = \max_{1 < i < n} \text{distance}(line(p_1, p_n), p_i)

5. **Threshold Evaluation & Recursive Splitting:**
   * **If** :math:`d_{max} > \epsilon`: The isolated vertex represents a critical structural feature that cannot be discarded. The original line is split into two sub-polylines at the index of this vertex: a left-hand segment spanning from :math:`p_1` to :math:`p_{index}`, and a right-hand segment spanning from :math:`p_{index}` to :math:`p_n`. The algorithm recursively invokes itself independently on both sub-segments.
   * **Else** (:math:`d_{max} \le \epsilon`): All intermediate vertices along the current segment lie within the acceptable spatial tolerance boundary. Consequently, all intermediate vertices are safely discarded, and the simplified segment collapses to a simple straight line consisting solely of the anchors :math:`[p_1, p_n]`.

Algorithmic Limitations & Greedy Behavior
-----------------------------------------
While computationally efficient and highly intuitive, the Douglas-Peucker algorithm is categorized as a **greedy heuristic** and suffers from several well-documented limitations:

* **Lack of Global Optimality:** Because the algorithm prioritizes the single "worst offender" first at each recursive tier, it makes localized greedy selections. It does not evaluate combinations of point omissions that might yield an even smaller subset of points while still satisfying :math:`\epsilon`.
* **Sensitivity to Positional Noise:** A single anomalous coordinate or spike caused by spatial sensor noise will force a line split, completely altering the recursive structure down the chain.
* **Oversimplification of Critical Features:** It can sometimes inadvertently smooth out highly narrow but topologically critical sharp features if their perpendicular distance to a distant baseline falls slightly below the epsilon limit.

**Case Study Example (Greedy Failure Mode)**

Consider a sequence of five points with a spatial tolerance threshold of :math:`\epsilon = 0.5`:

+-------+-------------------+
| Point | Coordinates (x,y) |
+=======+===================+
| A     | (0, 0)            |
+-------+-------------------+
| B     | (1, 0.9)          |
+-------+-------------------+
| C     | (2, 0.1)          |
+-------+-------------------+
| D     | (3, 1.0)          |
+-------+-------------------+
| E     | (4, 0)            |
+-------+-------------------+

* **Douglas-Peucker Execution Sequence:**
  
  1. Baseline connected from :math:`A \rightarrow E`.
  2. Distance evaluation identifies vertex :math:`D` as the maximum offender with :math:`d = 1.0`.
  3. Since :math:`1.0 > 0.5`, point :math:`D` is kept, splitting the process into :math:`A \rightarrow D` and :math:`D \rightarrow E`.
  4. Processing segment :math:`A \rightarrow D` yields vertex :math:`B` as the maximum outlier with :math:`d = 0.9`. Since :math:`0.9 > 0.5`, :math:`B` is kept.
  5. The final DP output yields **4 vertices**: `[A, B, D, E]`.

* **The Globally Optimal Solution:**
  
  An optimal alternative baseline configuration exists by selecting only segment points `[A, B, E]`. If you evaluate intermediate points :math:`C` and :math:`D` against the segments :math:`\overline{AB}` and :math:`\overline{BE}`, their deviations are :math:`0.36` and :math:`0.40` respectively. Because both deviations fall strictly below :math:`\epsilon = 0.5`, they could be completely eliminated, yielding a valid simplified chain of only **3 vertices** `[A, B, E]`. Douglas-Peucker fails to find this globally optimal setup due to its greedy nature.

Pure Python Dependency Restrictions
-----------------------------------
In alignment with strict engineering constraints, this package is engineered from the ground up without relying on advanced vectorization toolkits (such as NumPy, SciPy, or Shapely). All coordinate transformations, linear algebra projections, and Euclidean metrics are processed using core Python standard library capabilities (`math` and `json`).

Industrial Applications
-----------------------
* **GIS Map Generalization:** Downscaling geometric datasets for performance optimization across diverse visualization scales.
* **Cartographic Web Servers:** Dynamically adjusting vertex counts to fit variable web map zoom levels.
* **Trajectory Compression:** Reducing large-scale spatial traces gathered via global positioning receivers (such as marine vessels cruising the **Ilıca Bay** coastlines).

Package API Reference
---------------------
Below is the automated programmatic interface documentation compiled directly from the package source code docstrings:

.. automodule:: dp.dp_algo
   :members:
   :undoc-members:
   :show-inheritance:

.. toctree::
   :maxdepth: 2
   :caption: Contents: