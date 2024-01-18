# DAMASK
Useful scripts for DAMASK Cristal Plastisity

DAMASK simulation include three steps:
Pre-processing
1. Create geom.vti
Necessary scripts and software: Neper, polycristalmaker.ipynb, Paraview. 
  -----------------
  1. Use polycristalmaker to make a grid with necessary size, cells and origin. 

  2. Use Neper to create specific geometry and sort grains if needed. 

  3. Use Paraview to convert .vti from polycristalmaker to .vtk in ASCII and conver Binary .vtk to ASCII .vtk. 

  4. Copy table from Neper .vtk to the polycristalmaker .vtk

  5. Convert .vtk to .vti with polycristalmaker.ipynb
  ----------------
3. Create load.yaml
  ----------------
  
  ----------------

4. Create material.yaml

Processing
1. For Grid solver:
DAMASK_grid --material material.yaml --geom geom.vti --load load.yaml
2. For Mesh solver:
3. Additional options:

Post-processing
1. 
