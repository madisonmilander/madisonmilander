import arcpy
import os

# Set environment workspace
arcpy.env.workspace = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\coding_challenge_5"
arcpy.env.overwriteOutput = True

# Input CSV file containing species data
input_csv = "CC 5  - Sheet1.csv"

# Output directory for heatmap files
output_dir = "heatmaps_output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to generate heatmap
def generate_heatmap(input_data, output_heatmap, cell_size):
    arcpy.management.XYTableToPoint(input_data, "species_points", "decimalLongitude", "decimalLatitude")
    arcpy.management.PointToRaster("species_points", "OBJECTID", output_heatmap, "MOST_FREQUENT", "", cell_size)
    print(f"Heatmap {output_heatmap} generated.")

# Read the CSV file and separate species data
scientificName1 = [(13.6, 67.82), (-179.3693, 62.2688), (-147, 60.3), (166.1405, 54.9648), (-147, 60.3), (30.37, 70.68), (3.02, 60), (51.8726, -46.4234), (-147, 60.3), (-147, 60.3)]
scientificName2 = [(152.26, -32.61), (151.38, -33.95), (152.31, -32.57), (150.17, -36.26), (150.21, -36.26), (153.6, -28.9), (153.18, -30.21), (151.37, -33.94), (150.17, -36.26), (151.783, -32.583)]

species1_data = "scientificName1.csv"
species2_data = "scientificName2.csv"

# Write species data to CSV files
with open(species1_data, 'w') as file:
    file.write("decimalLongitude,decimalLatitude\n")  # Write header
    for lon, lat in scientificName1:
        file.write(f"{lon},{lat}\n")

with open(species2_data, 'w') as file:
    file.write("decimalLongitude,decimalLatitude\n")  # Write header
    for lon, lat in scientificName2:
        file.write(f"{lon},{lat}\n")

print("Species data separated and saved as CSV files.")

# Create a fishnet to define the extent of the heatmap
cell_size = 0.21
fishnet = arcpy.management.CreateFishnet(os.path.join(output_dir, "fishnet.shp"),
                                          "-180 -90", "180 -90", cell_size, cell_size, 1, 1, "#",
                                          "NO_LABELS", "#", "POLYGON")
print("Fishnet file generated.")

# Generate heatmap for species 1
heatmap_scientificName1 = os.path.join(output_dir, "heatmap_scientificName1.tif")
generate_heatmap(species1_data, heatmap_scientificName1, cell_size)

# Generate heatmap for species 2
heatmap_scientificName2 = os.path.join(output_dir, "heatmap_scientificName2.tif")
generate_heatmap(species2_data, heatmap_scientificName2, cell_size)

print("All heatmaps generated successfully.")

# Provide feedback
print("Code executed successfully. Please ensure that the heatmaps are correctly generated and meet the requirements.")
