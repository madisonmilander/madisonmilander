import arcpy

# Define the input shapefile
input_shapefile = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\coding_challenge_9\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"

# Define the field names
photo_field = "PHOTO"
species_field = "SPECIES"

# Create lists to hold the records with and without photos
records_with_photos = []
records_without_photos = []

# Count variables
count_with_photos = 0
count_without_photos = 0

# Set workspace
arcpy.env.workspace = r"C:\output\directory"

# Iterate through the input shapefile
with arcpy.da.SearchCursor(input_shapefile, [photo_field, species_field]) as cursor:
    for row in cursor:
        # Check if the record has a photo
        if row[0]:
            count_with_photos += 1
            records_with_photos.append(row)
        else:
            count_without_photos += 1
            records_without_photos.append(row)

# Print counts
print("Number of records with photos:", count_with_photos)
print("Number of records without photos:", count_without_photos)

# Create output shapefiles
output_with_photos = "Sites_With_Photos.shp"
output_without_photos = "Sites_Without_Photos.shp"

# Use the first row's spatial reference for output shapefiles
spatial_ref = arcpy.Describe(input_shapefile).spatialReference

# Delete output shapefiles if they already exist
for output_shapefile in [output_with_photos, output_without_photos]:
    if arcpy.Exists(output_shapefile):
        arcpy.Delete_management(output_shapefile)

# Create output shapefiles
try:
    arcpy.CreateFeatureclass_management(arcpy.env.workspace, output_with_photos, "POINT", spatial_reference=spatial_ref)
    arcpy.CreateFeatureclass_management(arcpy.env.workspace, output_without_photos, "POINT", spatial_reference=spatial_ref)
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))  # Print any error messages
except Exception as e:
    print(e)  # Print other exceptions

# Add fields to the output shapefiles
for output_shapefile in [output_with_photos, output_without_photos]:
    if arcpy.Exists(output_shapefile):
        arcpy.AddField_management(output_shapefile, photo_field, "TEXT")
        arcpy.AddField_management(output_shapefile, species_field, "TEXT")

# Define the fields to be added
fields = [photo_field, species_field, "SHAPE@XY"]

# Insert features into output shapefiles
for output_shapefile, records in [(output_with_photos, records_with_photos), (output_without_photos, records_without_photos)]:
    if arcpy.Exists(output_shapefile):
        with arcpy.da.InsertCursor(output_shapefile, fields) as cursor:
            for record in records:
                cursor.insertRow(record)

print("Shapefiles created successfully.")
