import arcpy
# from arcpy.sa import
import os

# Set environment workspace
arcpy.env.workspace = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\coding_challenge_5"
arcpy.env.overwriteOutput = True

# Input CSV file containing species data
input_csv = "CC 5  - Sheet1.csv"

# Output directory for heat map files
output_dir = "heatmaps.output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
def generate_heatmap(input_data, output_heatmap, cell_size):
    # arcpy.management.KernelDensity(input_data, output_heatmap, "0.21", cell_size, "SQUARE_KILOMETERS", "PLANAR")


# Read the CSV file and separate species data


    scientificName1 = [(13.6, 67.82), (-179.3693, 62.2688), (-147, 60.3), (166.1405, 54.9648), (-147, 60.3), (30.37, 70.68), (3.02, 60), (51.8726, -46.4234), (-147, 60.3), (-147, 60.3)]
    scientificName2 = [(152.26, -32.61), (151.38, -33.95), (152.31, -32.57), (150.17, -36.26), (150.21, -36.26), (153.6, -28.9), (153.18, -30.21), (151.37, -33.94), (150.17, -36.26), (151.783,-32.583)]
##########

species_data = "CC 5  - Sheet1.csv"
species1_data = "scientificName1.csv"
species2_data = "scientificName2.csv"
print("separating species data")

arcpy.management.CopyRows(species_data, species1_data, "Species = 'Scientific Name 1'")
arcpy.management.CopyRows(species_data, species2_data, "Species = 'Scientific Name 2'")
print(" species data separated")
############

#Create a fishnet to define the extent of the heatmap
cell_size = 0.21
fishnet = arcpy.management.CreateFishnet(os.path.join(output_dir, "fishnet.shp"),
                                          "-180 -90", "180 -90", cell_size, cell_size, 1, 1, "#",
                                          "NO_LABELS", "#", "POLYGON")

print("fishnet files generated")

# Generate heatmap for species 1
heatmap_scientificName1 = "heatmap_scientificName1.tif"
generate_heatmap(species1_data, heatmap_scientificName1, cell_size)

print("Heatmap for species 1 generated.")

# Generate heatmap for species 2
heatmap_scientificName2 = "heatmap_scientificName2.tif"
generate_heatmap(species2_data, heatmap_scientificName2, cell_size)

print("Heatmap for species 2 generated.")

print("All heatmaps generated successfully.")