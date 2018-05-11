Pystripe: a Python Package for Removing Streaks from Light-Sheet Images
########################################################################

:date: 2018-05-11 14:10
:modified: 2018-05-11 14:10
:tags: pystripe, python, microscopy, light-sheet, SPIM
:og_image: images/hela_cells.jpg
:slug: pystripe-summary
:authors: Justin Swaney
:summary: Pystripe is a new package that can clean up streaky light-sheet images


The Problem: Streaks in Light-Sheet Fluorescence Microscopy
************************************************************

Light-sheet fluorescence microscopy (LSFM_) is a high-speed imaging technique
that is gaining popularity in biological imaging. LSFM actually has many different
types of subtechnologies, such as selective plane illumination microscopy (SPIM).
In SPIM, a light-sheet is artificially created by quickly scanning a laser across
the field of view using a galvo mirror.

.. _LSFM: https://en.wikipedia.org/wiki/Light_sheet_fluorescence_microscopy

.. figure:: images/spim_vs_confocal.jpg
	:figwidth: 70 %
	:align: center
	:alt: spim-vs-confocal

	From Bruker and Newswire.

	(Left) SPIM illuminates a single plane of the sample at a time, reducing the
	potential for fluorophore bleaching. The detection is performed using wide-field
	cameras, which is faster than point scanning. (Right) Confocal single-photon
	excitation illuminates the entire sample along the axial dimension.
	Only a single pixel within the focal plane is recorded at a time.


|

While SPIM has many advantages over confocal, it has some complications that
do not exist in confocal microscopy. Due to wide-field detection, achieving a
flat field image is more challenging with SPIM. Such perfect illumination may
not even be possible without adaptive optical elements. A common manifestation
of this is seen when a sample of uneven refractive index is imaged using SPIM.
The small changes in refractive index within the sample scatter the light-sheet,
resulting in streaks and cast shadows. Some microscopes try to compensate for
this as well as laser attenuation by using illumination "arms" on both sides
of the sample. While this may drastically reduce cast shadows near the sample
surface, it cannot compensate for scattering near the core of large samples.

Here is an example of this streaking artifact from our lab's SPIM:

.. figure:: images/streaky_image.jpg
	:figwidth: 70 %
	:align: center
	:alt: streaky-image

	Raw mouse brain image using SPIM



The Solution: Pystripe
***********************

There is still valuable, biologically-relevant information in the midst of the
stripe artifacts. Any filtering that we perform to remove the stripes should
selectively remove the stripes rather than our "true" signal. So the question
is how do we filter the streaks without disrupting the underlying signal?

In order to filter the stripes from the image, we need a method for isolating
that part of the original signal. We can first notice that the stripes are always
approximately horizontal. This is due to the fact that the illumination light
path is oriented horizontally across the field of view.

We can exploit the stripe characteristics in our filtering strategy. To
use the fact that all stripes are oriented horizontally, we can use the
discrete wavelet transform (DWT). If we apply the DWT once, the original
image is decomposed into four images at 1/4 the original resolution (same overall
number of coefficients): a downsampled "approximation" image and three detail
coefficient images (horizontal, vertical, and diagonal). These images large
obtained via a decimated filter bank. We can continue to apply the DWT to the
approximation image, resulting in another decomposition "level". Since the
approximation image was downsampled, the same wavelet basis functions span a
larger physical length. That is, subsequent DWT levels focus on larger spatial
scales.

Since the stripes manifest as horizontal fluctuations in intensity, their
power spectrum will be mostly oriented vertically. We could apply a notch
filter without performing the DWT (while preserving the DC component), but
this wouldn't take advantage of the spatial decomposition that the DWT offers.
Therefore, a simple FFT filter will probably remove more of the original signal
than a combination DWT-FFT based filter.

To combine an FFT filter with our DWT decomposition, we can use the same FFT
notch filter on the horizontal detail coefficients. In this case, we need not
preserve the DC component of the DWT coefficients because the approximation
image contains most of that information. Since the stripes are not perfectly
horizontal, the filter should have some tunable *bandwidth* to adjust how
far from the vertical axis we filter the power spectrum. In my case, I used a
guassian filter where the standard deviation represented the bandwidth.

The result is shown below side-by-side with the original image:

.. figure:: images/streaks_before_after.jpg
	:figwidth: 90 %
	:align: center
	:alt: streaks-before-after

	Raw (left) and filtered (right) mouse brain image using SPIM and pystripe


In implementing pystripe, I've created a command-line interface (CLI) so that
multiple images in a directory can be batch processed using all the cores on
a single machine. In our lab, we can destripe a whole mouse brain (about 150 GB
of image data) in about 30 minutes. In `a similar method`_, MATLAB code based on
the `countourlet transform`_ took just about as long for a single image, so this
performance was a huge improvement.

.. _`a similar method`: https://aip.scitation.org/doi/full/10.1063/1.5016546
.. _`countourlet transform`: https://en.wikipedia.org/wiki/Contourlet
