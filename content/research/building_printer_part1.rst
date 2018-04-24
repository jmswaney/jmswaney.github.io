Building a Two-Photon Stereolithography 3D Printer: Part I
############################################################

:date: 2018-04-23 08:03
:modified: 2018-04-23 22:37
:tags: Printing, stereolithography, LabVIEW
:og_image: images/hela_cells.jpg
:slug: building_printer_part1
:authors: Justin Swaney
:summary: Part I in a series summarizing my steps to build a 3D printer

In this series of posts, I'm going to cover the steps that I took to build a laser-scanning 3D printer. Before discussing the optics and programming details, I'd like to first explain why commercially-avaiable 3D printers were not suitable for my research project.

Commercially-available 3D printing technologies
************************************************

Many different types of 3D printing technologies have been commerciallized, such as fused deposition modeling (FDM), stereolithography (SLA), and selective laser sintering (SLS). Each technology has its own advantages and disadvantages and is, therefore, commonly seen in particular manufacturing contexts.

Fused deposition modeling
--------------------------
FDM is a simple additive manufacturing technique where a thermoplastic filament is extruded from a heated nozzle. When the thermoplastic exits the nozzle, it cools and solidifies, offering support for the next layer to be extruded on top of it.

At its core, FDM requires a few relatively cheap hardware components:

    - An extrusion nozzle
    - A heating element
    - A thermoplastic material
    - A few stepper motors

Being built from these cheap components, FDM printers are the most affordable commercially-available "Desktop 3D Printers". Hobbyists can purchase FDM printers for less than $200, and an online community of shared 3D models, optimal printer settings, and even cusutom printer firmware has emmerged.

In addition to being affordable, FDM printers can print with a variety of different colors and materials, often simultaneously. Dual-extrusion FDM printers allow users to print two materials within a single print. Sometimes this feature is used to incorporate two colors into the printed prototype. More often, dual-extusion is used to print support structures for models with problematic geometries (overhangs, holes, thin walls). Typically, the support material is sacraficial and can be dissolved. For example, polylactic acid (PLA) is often supported by polyvinyl alcohol (PVA). As the name suggests, PVA is hydrophilic and soluble in water. On the other hand, PLA is not water-soluble, so the PVA can be safely washed away leaving the final PLA part. It's also important to note that PLA and PVA have similar extrusion and bed temperatures (at the molecular weights in the filaments). This is important because the printer can only maintain a single temperature setpoint--printing materials with vastly different glass transistion temperatures is impractical. For this reason, acrylonitrile butadiene styene (ABS) is often printed with high impact polystyrene (HIPS) because they have similar glass transistion temperatures that are higher than that of PLA/PVA. As a side note, the PLA/PVA printing combintation is much easier to work with in my experience.

Stereolithography
------------------
SLA is a laser-based additive manufacturing technology. Instead of using a solid filament material, SLA printers rely on a light-sensitive liquid resin that undergoes photopolymerization to form a solid. In SLA, a laser beam is directed onto the resin by a pair of motorized mirrors. These mirrors, called **galvanometers** (or just **galvos**), are positioned orthogonally so that the pair can scan the laser beam over a theoretical XY plane on the resin. After scanning the mirrors over a single XY plane, a platform in the resin is moved to make room for the fresh resin to be cured on the last layer.

Selective laser sintering
--------------------------
SLS is another laser-based additive manufacturing technology. Rather than using photopolymerization to turn a liquid into a solid, SLS printers use a strong laser to melt a powdered thermoplastic into a solid part.
