.. _overset_overview:

########################
Optimization with OpenVSP, OpenMDAO and Overset-Meshes
########################
This tutorial will mainly explain how overset meshes for ADFlow are generated. We will use OpenVSP to create 
the geometry, generate a surface mesh with Pointwise (subject to charge) and extrude the volume mesh with pyhyp.

OpenVSP does not only provide the geometry, it can also be hooked up with pygeo. This means, the mesh 
can be warped based on OpenVSP variables thus allowing optimization without the hassle of generating an FFD control
box. As this possibility exists, there will be a small optimization in the end.

We will do this process on the `ONERA M6 Wing <https://www.grc.nasa.gov/WWW/wind/valid/m6wing/m6wing.html>`_. It is a common example to validate flow solvers in the transonic regime
and is backed with experimental data. 

Table of Contents
=================

.. toctree::
   :maxdepth: 1

   overset_theory
   overset_vsp



Directory Structure
===================
::

    overset
    |-- geo
    |   |-- onera_m6.vsp
    |   |-- profile_m6.dat