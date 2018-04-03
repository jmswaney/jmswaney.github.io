Neural Organoids: a New Platform for Human Brain Research
##########################################################

:date: 2018-04-02 09:19
:modified: 2018-04-02 09:19
:tags: brain, organoid, vascular
:og_image: images/hela_cells.jpg
:slug: organoid-intro
:authors: Justin Swaney
:summary: Neural organoids are a new biological model for the human brain


Neural Organoids are Mini-Brains Grown *In Vitro*
**************************************************

Neural organoids are a new biological model for the developing human brain. You can think of them as mini-brains grown in a dish. To make these mini brains, we take induced pluripotent stem cells (iPSCs), form them into spheres called embryoid bodies, and then culture them in special media to encourage differentiation into neural progenitor cells and neurons. After a month or two of being cultured in a spinning bioreactor, neural organoids can grow to about 3 mm in diameter with multiple regions resembling the developing human brain.


.. figure:: images/lancaster_protocol.png
	:figwidth: 90 %
	:align: center
	:alt: neural-organoid-protocol

	Adapted from Lancaster, M. (2013) *Nature*.

	(Left) Organoids are derived from iPSCs by first forming embryoid bodies and then then embedding in Matrigel. The organoids are then grown under constant stirring to improve nutrient transport. (Right) Neural organoids typically reach around 3 mm in diameter and contain protein expression patterns that are reminiscent of a developing human brain.

|

An interesting property of organoids is that they are patient specific. We can take cells from a patient, reprogram them into iPSCs, and then create our organoids from those patient-derived cells. This personalized feedback creates therapeutic potential for disease modeling, drug testing, and—maybe not in the case of the brain—organ replacement.

.. figure:: images/lancaster_personalized_medicine.png
	:figwidth: 70 %
	:align: center
	:alt: organoid-personalized-medicine

	Adapted from Lancaster, M. (2014) *Science*.

|

Neural organoids have been shown to recapitulate phenotypes of several neurological disorders including microcephaly, Autism, Rett syndrome, Zika, and Alzheimer’s. In light of these recent successes, pharmaceutical companies such as Novartis_ have begun to explore organoid models for drug development.

.. _Novartis: http://www.biopharmadive.com/press-release/20161110-novartis-explore-novel-approaches-to-disease-modelling-and-organoid-technol

Neural Organoids are an Imperfect Model
***************************************

One major limitation of neural organoids is that they do not develop their own vascular system. Without any vascular system, nutrients are forced to diffuse in from the organoid surface. At the same time, cells are consuming these nutrients. Recent literature shows that apoptosis increases dramatically 250um from the organoid surface, suggesting that there is inadequate transport of some limiting nutrient. The impact that these nutrient gradients and regions of apoptosis have on the ability of neural organoids to recapitulate higher-order brain functions is not well understood.

.. figure:: images/raja_cell_death.png
	:figwidth: 90 %
	:align: center
	:alt: organoid-cc3-apoptosis

	Adapted from Raja, W. (2016) *PLOS ONE*.

	(Left) A confocal image of the edge of a neural organoid. Hoechst (blue) shows all nuclei and CC3 (white) shows which cells are undergoing apoptosis. (Right) The number of apoptotic cells as a function of distance away from the orgnaoid surface.

These transport problems do not exist in vivo. In the human brain, the vascular system is pervasive—it has to be because the brain demands so much energy. It is also surprisingly small in terms of total volume. This makes recreating the vascular system a very difficult engineering problem, and it has been for a long time.

.. youtube:: r4M5kSojF3Q

|

The tissue engineering community has developed many approaches to *in vitro* vascularization—I'll just summarize two recent ones. First, Jennifer Lewis’ group at Harvard is currently using 3D bio-printing to create vasculature. They extrude cell-laden inks to create vascular molds and then flow in endothelial cell to create blood vessels. However, the resulting blood vessels are about 650um wide. The other approach called Extravasation is from Roger Kamm’s group at MIT. Extravasation relies on the ability to endothelial cells to form blood vessels naturally under flow conditions. However, there is little control over the resulting network geometry and patterning.


.. figure:: images/vascularization_techniques.png
	:figwidth: 100 %
	:align: center
	:alt: vascularization-techniques

	Adapted from Lewis, J. (2016) *PNAS* and Kamm, R. (2016) *PNAS*.

	(Left) 3D Bio-printing. (Right) Endothelial cell extravasation.

These techniques leave much to be desired when compared to what we see *in vivo*. 3D bio-printing allows complete control of our vascular geometry, but it doesn't have sufficient resolution to print unobtrusive vessels. Extravasation allows us to create very intricate capillary systems, but we lose the ability to control our vascular geometry. Is there a way to get the best of both worlds?

The lack of a vascular system is just one of many issues that researchers are addressing with neural organoids. The payoff is huge if we can address these limitations. As we continue to improve on our most complex biological models, we may be able to better understand healthy development of human tissues and develop new therapeutics.
