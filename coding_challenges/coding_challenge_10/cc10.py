import arcpy
from arcpy.sa import *

# Set workspace
arcpy.env.workspace = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\coding_challenge_10"

# List all Landsat files
landsat_files = arcpy.ListRasters()

# Output directory for NVDI
output_dir = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\coding_challenge_10"

# Loop through each Landsat file
for raster in landsat_files:
    # Extract month from file name
    month = raster.split("_")[1]

    # Set output NVDI raster name
    output_raster = os.path.join(output_dir, "NVDI_" + month)

    # Calculate NVDI
    nir = Raster(raster + "\Band_5")
    vis = Raster(raster + "\Band_4")
    nvdi = (nir - vis) / (nir + vis)

    # Save NVDI raster
    nvdi.save(output_raster)

# Visualize NVDI patterns in ArcMap
# You can manually create a layout in ArcMap and export it as a PDF
# showing the patterns for an area of interest in Rhode Island.
