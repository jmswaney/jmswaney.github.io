Introduction 
############

:date: 2018-04-01 01:09
:modified: 2018-04-01 20:09
:tags: first, initial
:slug: initial-commit
:authors: Justin Swaney
:summary: Greetings! This post summarizes what you may find on this website

I created this website using `Github Pages`_ today to serve as a sort of blog / professional portfolio. In addition to some links and contact info, you may find more detailed posts about the minutiae of some projects that I've been involved with. These more detailed posts may include step-by-step walkthroughs or progress updates with open-ended future work. If I find that I'm rambling too much, I may create a page dedicated to distilling down the more *stream-of-consciousness* posts. In this post, I'd like to introduce the some of my research topics at a high level.

Two-photon Stereolithography
****************************
At MIT, I built a custom 3D printer for fabricating biocompatible microfluidics. I was fortunate enough to have an expensive Ti:Sapphire laser at my disposal, and `two-photon stereolithography`_ (2p SLA) offered better resolution than traditional UV curing-based printing technologies. I'd like to share my approach as well as it's limitations at some point.

.. figure:: images/3d_printer.jpg
   :figwidth: 80 %
   :align: center
   :alt: custom 2p SLA printer

   The 2p SLA printer that I built for direct writing of biocompatible microfluidics. It works in much the same way as a confocal microscope.

3D Biological Image Analysis in Intact Tissues
***********************************************
I built the aforementioned 2p SLA printer to give `brain organoids`_ a synthetic vascular system. In order to compare avasclular and vascularized brain organoids, I had (and still have) many questions. Many of these questions could be answered after labeling the brain organoids for specific proteins and imaging with confocal microscopy. My lab actually pioneers new clearing technologies like CLARITY_, so we do these staining and imaging steps all in 3D with cleared tissues. After imaging, we just have some pretty images, so we're often faced with non-trivial image processing tasks. In the case of a whole mouse brain, these 3D images can be upwards of 1TB, so sometimes the data doesn't even fit into a single computer's memory. I'll post updates as I work on these computational challenges too.

.. figure:: images/embryoid_body.jpg
   :figwidth: 80 %
   :align: center
   :alt: mini-brain

   A confocal image of a mini-brain grown in our lab

Other Tips and Tricks
*********************
I leave this here as a sort of wildcard for cool tid-bits that I've learned after hours and hours of digging for answers on Github / Stack Overflow / actual libraries. Many of the specific problems encountered during my research touch upon broader topics in programming, machine learning, and computer vision. I'll inevitably feel like I did these topics an injustice if I don't address them more completely.

.. References
.. _`Github Pages`: https://pages.github.com/
.. _`two-photon stereolithography`: https://www.youtube.com/watch?v=wThtfAtB5U8
.. _`brain organoids`: https://www.technologyreview.com/s/535006/brain-organoids/
.. _CLARITY: https://www.youtube.com/watch?v=c-NMfp13Uug
