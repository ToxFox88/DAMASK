# DAMASK
Useful scripts for DAMASK Cristal Plastisity

DAMASK simulation include three steps:
Pre-processing
1. Create geom.vti
Necessary scripts and software: Neper, polycristalmaker.ipynb, Paraview.

  -----------------
  This file could be generated in two ways: the easiest way is to create the necessery grid with polycrystalmaker.ipynb script but the quantity of such a grid could be unacceptable. The second way is generate it with Neper software: 

  1. Use Neper to create specific geometry and sort grains if needed. 

  2. Convert .vtk to .vti with Geom.ipynb
  ----------------
  
2. Create load.yaml
  
  ----------------
  Feel free to change load.yaml as you wish but there are some notices:
  1. N is the number of incremets (kind of iterations) which affects on the precision of solving.

  2. dot_F matrix components can be changed to increase or decrease deformation which affects on the material per unit of time.

  3. t is the number of units of time the deformation affects the material. It can be increased in order to achieve larger deformation ratio as well as the dot_F matrix components value.

  4. Notice that DAMASK does not allow to get large deformation (usually more than 40-50%) in one simulation. 
  ----------------

3. Create material.yaml
   
  ----------------
  This file can also be changed by hands but you should be careful and always compare your file with material.yaml template.
  1. phase: here must be indicated all of the phases you use in simulation. Each phase must have it`s lattice (cF for FCC, cI for BCC, or hP for HCP) and mechanical parameters.

  2. elastic: here must be elastic constants which you can find in papers. Theese constants are specific for each phase and can change due to component comtent changing.

  3. plastic: there are some specific plastic parameters. Some of them could be found in papers (e.g. N_sl, h_0_sl-sl, xi_0_sl, xi_inf_sl and ot_gamma_0_sl) but some should be adjusted.

  4. material: material is the same thing as orientation. It could be created from experimantal data with MakeMaterial.ipynb (orient.txt) or could be randomly (or almos randomly) simulated by CreateTexture.ipynb or analogous soft. 
  
  ----------------

Processing
1. For Grid solver:
DAMASK_grid --material material.yaml --geom geom.vti --load load.yaml
2. For Mesh solver:
3. Additional options:
**tbd**

Post-processing
1. Modificate HDF5 result file with Dereviedquant.yaml in order to add necessary parameters for visualisation: IPF, Mises stress, Cauchy stress and export .vti files.
2. Visualize .vti files in Paraview (set necessary parameter e.g. IPF and Surface mod) also use "Warp by vector" function to visualize deformation.
3. Export orients in Euler by ConverttoEuler.yaml
4. Build pole figures with post.m MTEX script.
5. Enjoy. 
