Large point cloud registration using density cross-correlation
##############################################################

.. :date: 2018-04-02 20:50
.. :modified: 2018-04-02 20:50
.. :tags: point, cloud, image, registration, cell, density
.. :og_image: images/hela_cells.jpg
.. :slug: cell-density-registration
.. :authors: Justin Swaney
.. :summary: A fast method for rigid registration of large point clouds without correspondences


In this post, I'll discuss the first part of our Phathom image processing pipeline: *image registration*.

**TL;DR:** Many off-the-shelf algorithms for rigid point cloud registration
either do not meet our functional requirements for computational complexity
or robustness to missing points. We've borrowed from theory in Kernel
Density Estimation to pose our coarse registration problem probablistically.
By considering the density of points rather than the points themselves,
our algorithm is inherently more robust against missing points. The point
density may be estimated in a multi-bandwidth manner, allowing us to tune
how coarse or fine grained the registration is.

1nd Approach: Geometric Hashing, RANSAC, and SVD
**************************************************


2nd Approach: Iterative Closest Point
****************************************

The Iterative Closest Point (ICP) algorithm is a classic approach to point cloud
registration without known correspondences. It assumes that closests points
are matches and forms a cost function based on the sum of squared distances
between these correspondences. The closest points may change as this cost
function is minimized using gradient descent, so they need to be calclated
on every iteration. Derivatives of ICP have modified every aspect of it's
inner workings, from how the correspondences are found to the definition of
the cost function.


3rd Approach: Density cross-correlation optimization
******************************************************
