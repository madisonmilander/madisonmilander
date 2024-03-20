import arcpy
from arcpy.sa import *
import os

# Set environment workspace
arcpy.env.workspace = r"/Users/madisonmilander/Library/CloudStorage/OneDrive-UniversityofRhodeIsland/NRS 528/coding challenge 5"
arcpy.env.overwriteOutput = True

# Input CSV file containing species data
input_csv = "CC 5  - Sheet1.csv"

# Output directory for heatmap files
output_dir = "heatmaps.outout"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read the CSV file and separate species data
# Replace this with your actual code to read and process the CSV file
# For demonstration purposes, I'll create dummy data
scientificName1 = [(13.6, 67.82), (-179.3693, 62.2688), (-147, 60.3), (166.1405, 54.9648), (-147, 60.3), (30.37, 70.68), (3.02, 60), (51.8726, -46.4234), (-147, 60.3), (-147, 60.3)]
scientificName2 = [(152.26, -32.61), (151.38, -33.95), (152.31, -32.57), (150.17, -36.26), (150.21, -36.26), (153.6, -28.9), (153.18, -30.21), (151.37, -33.94), (150.17, -36.26), (151.783,-32.583)]

# Create a fishnet to define the extent of the heatmap
cell_size = 0.21
fishnet = arcpy.management.CreateFishnet(os.path.join(output_dir, "fishnet.shp"),
                                          "-180 -90", "180 -90", cell_size, cell_size, 1, 1, "#",
                                          "NO_LABELS", "#", "POLYGON")

print("Fishnet file generated.")
#
# # Convert species data to point feature classes
# species_fc_1 = arcpy.management.XYTableToPoint(input_csv, os.path.join(output_dir, "species1.shp"),
#                                                "Longitude", "Latitude", "#", "#", "#")
# species_fc_2 = arcpy.management.XYTableToPoint(input_csv, os.path.join(output_dir, "species2.shp"),
#                                                "Longitude", "Latitude", "#", "#", "#")
#
# print("Species data converted to point feature classes.")

# Generate heatmaps for both species
heatmap_1 = arcpy.sa.KernelDensity(scientificName1, "NONE", cell_size)
heatmap_1.save(os.path.join(output_dir, "heatmap_species1.tif"))

heatmap_2 = arcpy.sa.KernelDensity(scientificName2, "NONE", cell_size)
heatmap_2.save(os.path.join(output_dir, "heatmap_species2.tif"))

print("Heatmaps generated for both species.")
