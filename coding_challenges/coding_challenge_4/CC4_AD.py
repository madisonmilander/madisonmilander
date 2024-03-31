# This is for coding challenge 4
# For this, I used the reclassify tool for the land cover of Rhode Island in 2016
# I took the developed land, forest areas, shrub, and woody wetland areas viable, and all other areas null

## AD - all your code was commented out so I had to uncomment it to run, please revise your version so it is
## uncommented, below I place some comments but essentially, you need to ensure that running the code is easy for
## a user, right now, I have to dig deep into the out_raster variable to get this code to run on my machine.
## See below for my fix and compare it with yours.

import arcpy
import os

print("Reclassify tool started")

output_directory = r"H:\NRS528_2024\Madison_Milander\coding_challenges\coding_challenge_4"
output_raster = os.path.join(output_directory, "Reclass_NLCD1.tif")

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("3D")
arcpy.ddd.Reclassify(
    in_raster="NLCD_2016.img",
    reclass_field="NLCD_Land",
    remap="'Open Water' 0;'Developed, Open Space' 1;'Developed, Low Intensity' 1;'Developed, Medium Intensity' 1;'Developed, High Intensity' 1;'Barren Land' 0;'Deciduous Forest' 1;'Evergreen Forest' 1;'Mixed Forest' 1;Shrub/Scrub 1;Herbaceuous 1;Hay/Pasture 0;'Cultivated Crops' 0;'Woody Wetlands' 1;'Emergent Herbaceuous Wetlands' 0;' ' 0;NODATA -1",
    out_raster=output_raster,
    missing_values="DATA"
)

print("Reclassify tool complete")

# After running the tool, only the developed land, forest, shrub, and woody wetlands will show up/marked
