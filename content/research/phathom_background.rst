Phathom: A Distributed Image Processing Framework for Whole Brain Mapping
##############################################################################

:date: 2018-04-02 22:26
:modified: 2018-04-02 22:26
:tags: phathom, image, processing, brain, mapping
:og_image: images/hela_cells.jpg
:slug: phathom-background
:authors: Justin Swaney
:summary: The background and motivation for the phathom python package

In this post, I want to explain the motivations behind the creation of Phathom_ and clearly lay out the problems that it tries to solve. I'll add links to posts on specific parts of Phathom as I continue to develop it.

.. _Phathom: https://github.com/chunglabmit/phathom

Background
***********

Phathom is an image processing project born from the challenges faced when trying to analyze 3D biolgocal images of cleared tissue samples. In the following subsections, I'll provide some background to help understand this context.

Tissue Clearing
----------------

Tissue clearing refers to a set of new tissue processing techniques that render a tissue sample optically transparent. The most well-known clearing technique is CLARITY_. CLARITY-processed tissue samples retain all the proteins of the original tissue but are optically transparent, which permits us to visualize them in 3D with conventional light microscopy techniques. In the case of the brain, this removes the need to cut the whole brain into thin sections, preserving all the neuronal connections for 3D imaging. For this reason, CLARITY is most commonly applied to brains, but it can be used to clear other organs as well.

.. _CLARITY: https://www.youtube.com/watch?v=c-NMfp13Uug

.. figure:: images/clarity.jpg
	:figwidth: 70 %
	:align: center
	:alt: cleared mouse brains

	A CLARITY-processed mouse brain from Chung, K. (2013) *Nature*.

CLARITY works by removing lipids (including cell membranes) with a detergent. Since the lipids scatter light very effectively, the tissue becomes more transparent when they are removed. Unfortunately, the tissues also become extremely fragile because the membranes add a lot of structural support. CLARITY uses paraformaldehyde (PFA) and an acrylamide hydrogel (which is also clear) to support the tissue through this clearing process. The result is a transparent tissue-hydrogel hybrid that retains the original sample's endogenous proteins and nucleic acids in their original place.

Immunostaining
---------------

Since the endogenous proteins and nucleic acids are still present in the cleared sample, they can be 'stained' using conventional dyes, probes, and antibodies. For quick summary on how we hijack antibodies from the immune system to label specific proteins, check out immunohistochemistry_ (IHC). Here's a quick list of some probes that we use often with cleared brain samples:

.. _immunohistochemistry: https://en.wikipedia.org/wiki/Immunohistochemistry

- **DAPI**: DNA / nucleus (dye)
- **Syto16**: DNA / nucleus (dye)
- **Lectin**: blood vessels stain (lectin protein)
- **NeuN**: neurons (antibody)
- **SMI-312**: neuronal projections (antibody)
- **Parvalbumin, Calretinin, Calbindin**: interneurons (antibody)
- **GFAP**: astrocytes (antibody)
- **Iba1**: microglia (antibody)
- **Bassoon**: a presynaptic marker (antibody)
- **Homer1**: a postsynaptic marker (antibody)

When we stain and image wth these markers, we can visualize how their targets are spatially dsitributed throughout the brain. Typically, we assign each target a color and overlay them like this:

.. figure:: images/switch.jpg
	:figwidth: 90 %
	:align: center
	:alt: multicolor immunostaining image

	A multichannel image resulting from multiple rounds of protein labeleling and imaging. From Murray, E. (2015) *Cell*.

While this image is in 2D for presentation, we actually acquire many stacks of 2D images to create a 3D volume. We can do this using confocal microscopy or, if we need to image larger samples, light sheet microscopy.

Light Sheet Microscopy
-------------------------

Selective Plane Illumination Microscopy (SPIM) is a light sheet microscopy technique that is much faster than traditional point scanning techniques like confocal microscopy. A SPIM microscope typically consists of at least two microscope objectives positioned perpendicular to each other. The *illumination objective* is responsible for creating a light sheet by scanning a laser across the sample. The *detection objective* collects the light emitted from excited fluorophores for multiple cameras to record. After collecting an image at a single plane, either objectives move or the sample itself moves for the next image.

.. figure:: images/spim.jpg
	:figwidth: 70 %
	:align: center
	:alt: SPIM microscope

	From the Laser Analytics Group, University of Cambridge.

	(Left) Illumination objective forming a ligh sheet in the focal plane of the detection objective within a fluorescent solution. (Right) Detection objective collecting light emitted within the fluorescent solution.


Since the light sheet only excites the focal plane of the detection objective, SPIM limits out-of-focus light collection. This allows us to *optically section* our cleared tissue samples and stack our 2D images into sharp 3D images. SPIM has other advantages in terms of acquisition speed and limited *photobleaching* as well.


Motivation
************

Turning CLARITY into a quantitative technique for neuroscience
---------------------------------------------------------------

Neuroscientists often use CLARITY to create visually appealing figures—I've heard some refer to it as a *qualitative method for making pretty pictures*. That is, CLARITY is rarely used by a broader set of researchers as a central tool through which they study the brain. Several tried-and-true methods in electrophysiology, thin-section IHC, and optogenetics are used for the "heavy-lifting". I think this is a shame since many of these methods could be complimented quite well with the spatial information that CLARITY provides. So, why isn't this being done?

To take CLARITY from qualitative to quantitative, we need to turn our huge 3D images into some meaningful data. At a very basic level, the data that we are interested in gathering might include the location of every cell in the brain and which of these cells are neurons, glia, etc. It may also include brain region information for each cell (amygdala, VTA, etc). The challenge is to develop to compuational algorithms for extracting this information from large, somewhat noisy images.

If we can provide a tool for extracting meaningful biological information from images of cleared tissues, then CLARITY may be used to quantitatively compare different experimentatl conditions. Since these comparisons would be done with whole brains, the experimental comparisons are less biased than conventional sectioning techniques. One problem with section-based IHC is that researcher already have a brain region in mind when designing experiments. While this makes it easier to confirm your original hypothesis, it limits our ability to see the bigger picture. Using CLARITY quantitatively, we may be able to discover things that we never knew to look for.


Prior Art
***********

Large-scale image analysis is not a new problem in biological image processing. Here are some links to recent advances in the field:

- https://www.nature.com/articles/s41593-018-0109-1#Sec10
- https://www.sciencedirect.com/science/article/pii/S0959438815000756
- https://www.nature.com/articles/s41593-017-0027-7

Specific Aims of Phathom
***************************

Aim 1: Align multiple imaging rounds into a single global coordinate system
-----------------------------------------------------------------------------

Since we can only image 4 proteins at a particular time, we resort to a multiround staining and imaging approach. However, when we restain the tissue sample and return it to the microscope, we can't return the sample to *exactly* the same position as the previous imaging round. Therefore, we need a method for aligning multiple rounds of imaging in order to integrate all of the protein expression information into a single multicolor image. Coupled with this aim is the alignment to a `reference atlas`_ so that we can also know the brain region of each cell.

.. _`reference atlas`: http://mouse.brain-map.org/static/atlas

Aim 2: Detect all cells within the brain
------------------------------------------

As a starting point, we're interested in knowning where all the cells in the brain are. This can serve as a sort of "single-cell atlas" for each brain sample.

Aim 3: Classify individual cell types based on protein expression
-------------------------------------------------------------------

If we know where all the cells are, we may also be able to classify each cell type based on protein expression information. For example, parvalbumin postive cells may be classified as interneurons, and GFAP positive cells may be classified as astrocytes. By classifying each cell, we can start to compare specific cell populations between experiments.


Discussion
***********

There are many challenges when trying to accomplish the above aims. The first is the image size, which can be upwards of 1TB for a single mouse brain. This is larger than a sigle machine's RAM, so we need to process the image in smaller chunks and avoid reading the whole image. The image size also constrains our image processing algorithms since we need to prioirtize low computational complexity. Standard open-source tools like `Cell Profiler`_ are inadequate for this task for many reasons. First, they often assume that the image should be loaded into memory. Second, they are often implemented as a desktop app without the capability of distributed execution. Ideally, Phathom could take advantage of many cores across many nodes in a computing cluster (if they are available). That means that Phathom should come with support for common resource management systems like SLURM_.

Lastly, I'll state that visualization is beyond the scope of Phathom. Of course, visualizing the results that Phathom creates would be extremely informative, but we are actually developing a separate tool for visualization. Our visualization tool is called Nuggt_ and it is based on Neuroglancer_.

.. _`Cell Profiler`: http://cellprofiler.org/
.. _SLURM: https://slurm.schedmd.com/
.. _Nuggt: https://github.com/chunglabmit/nuggt
.. _Neuroglancer: https://github.com/google/neuroglancer
