# This is for coding challenge 4
# For this, I used the reclassify tool for the land cover of Rhode Island in 2016
# I took the developed land, forest areas, shrub, and woody wetland areas viable, and all other areas null

# import arcpy
#
# arcpy.env.overwriteOutput = True
# arcpy.CheckOutExtension("3D")
# arcpy.ddd.Reclassify(
#     in_raster="NLCD_2016.img",
#     reclass_field="NLCD_Land",
#     remap="'Open Water' 0;'Developed, Open Space' 1;'Developed, Low Intensity' 1;'Developed, Medium Intensity' 1;'Developed, High Intensity' 1;'Barren Land' 0;'Deciduous Forest' 1;'Evergreen Forest' 1;'Mixed Forest' 1;Shrub/Scrub 1;Herbaceuous 1;Hay/Pasture 0;'Cultivated Crops' 0;'Woody Wetlands' 1;'Emergent Herbaceuous Wetlands' 0;' ' 0;NODATA -1",
#     out_raster=r"C:\Users\mmilander\OneDrive - University of Rhode Island\Documents\ArcGIS\Projects\coding_challenge_4\Reclass_NLCD1.tif",
#     missing_values="DATA"
# )

# After running the tool, only the developed land, forest, shrub, and woody wetlands will show up/marked
