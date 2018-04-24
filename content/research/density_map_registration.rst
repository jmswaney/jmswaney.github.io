Large point cloud registration using density cross-correlation
##############################################################

.. :date: 2018-04-02 20:50
.. :modified: 2018-04-02 20:50
.. :tags: point, cloud, image, registration, cell, density
.. :og_image: images/hela_cells.jpg
.. :slug: cell-density-registration
.. :authors: Justin Swaney
.. :summary: A fast method for rigid registration of large point clouds without correspondences


.. In this post, I'll discuss the first part of our Phathom image processing pipeline: *image registration*.
..
.. **TL;DR:** Many off-the-shelf algorithms for rigid point cloud registration
.. either do not meet our functional requirements for computational complexity
.. or robustness to missing points. We've borrowed from theory in Kernel
.. Density Estimation to pose our coarse registration problem probablistically.
.. By considering the density of points rather than the points themselves,
.. our algorithm is inherently more robust against missing points. The point
.. density may be estimated in a multi-bandwidth manner, allowing us to tune
.. how coarse or fine grained the registration is.
..
.. 1nd Approach: Geometric Hashing and SVD
.. ****************************************
..
..
.. 2nd Approach: Iterative Closest Point
.. ****************************************
..
.. The Iterative Closest Point (ICP) algorithm is a classic approach to point cloud
.. registration without known correspondences. It assumes that closests points
.. are matches and forms a cost function based on the sum of squared distances
.. between these correspondences. The closest points may change as this cost
.. function is minimized using gradient descent, so they need to be calclated
.. on every iteration. Derivatives of ICP have modified every aspect of it's
.. inner workings, from how the correspondences are found to the definition of
.. the cost function.
..
..
.. 3rd Approach: Density cross-correlation optimization
.. ******************************************************
..
.. Notes
.. ********
.. Current density registration is not rotating the input image.
..
.. Indicies are ALWAYS with respect to the top-upper-left (TUP)
..
.. Perform the following for both the fixed and moving images:
..
.. peak_local_max -> (N, 3) array of nuclei indicies
.. nuclei indicies -(voxel dimensions)-> nuclei coords in um wrt TUP
.. nuclei coords in um wrt TUP -(CoM calculation)-> nuclei CoM in um wrt TUP
.. nuclei coords in um wrt TUP -(CoM)-> nuclei coords in um wrt CoM
.. image shape in voxels -(voxel dimensions)-> image bounds in um wrt TUP
.. image bounds in um wrt TUP -(CoM)-> image bounds in um wrt CoM (hist bounds)
.. image bounds in um wrt TUP -(bin width)-> bins
.. coords in um wrt CoM -(bins, bounds)-> density map
..
.. With the fixed and moving density maps, perform rigid registration:
..
.. GOAL: Find a rigid mapping from original fixed image to original moving image
.. GIVEN: original images, nuclei point clouds, and low-res density maps
..
.. Q: If we have a rigid mapping for low-res densities, can we relate that to
..    the rigid mapping for the original images?
..
.. The original images will be much larger than the density images in terms of
.. voxels, but it's the same physical dimension in micron.
.. Therefore, the same rigid mapping in physical space will work for both the
.. density map and the original image registraion.
.. However, map_coordinates requires us to supply coordinates in voxel units
.. In order to actually apply our transformation we can:
..   1) Relate the rigid transformation in space to that wrt voxels (hard if anisotropic)
..   2) Convert the indices to phyiscal coordinates wrt CoM before applying the transformation
..      Convert the resulting physical coordinates back to indices
..
.. fixed CoM: offset in um from TUP to the CoM in fixed image
.. moving CoM: offset in um from TUP to the CoM in moving image
..
.. This shold work for both the density images and the original images
.. as long as the right voxel_dims are used:
..
.. Transform moving image
..   fixed coords in voxels -(voxel dims)-> fixed coords in um wrt TUP
..   fixed coords in um wrt TUP -(fixed-to-moving offset)-> fixed coords in um wrt CoM
..   fixed coords in um with CoM -(rotation)-> rotated coords in um wrt CoM
..   rotated coords in um wrt CoM -(moving-to-fixed offset)-> moving coords in um wrt TUP
..   moving coords in um wrt TUP -(voxel dims)-> moving coords in voxels
