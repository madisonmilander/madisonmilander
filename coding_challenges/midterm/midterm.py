# This is for the midterm
# This first part is selecting the town of South Kingston

import arcpy
arcpy.env.overwriteOutput = True

# This is the town selection of South Kingston, Rhode Island
arcpy.analysis.Select(
    in_features="towns.shp",
    out_feature_class=r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\midterm\midterm_528\towns_studyarea",
    where_clause="NAME = 'SOUTH KINGSTOWN'"
)

# Using the CLIP TOOl, the rivers and streams are narrowed down to the selected area (South Kingston)
arcpy.analysis.Clip(
    in_features="HYDRO_Rivers_and_Streams_24K.shp",
    clip_features="towns_studyarea.shp",
    out_feature_class=r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\midterm\midterm_528\HYDRO_Rivers_and_Stream_Clip2",
    cluster_tolerance=None
)

# Once clipped to the area, I buffered the rivers by 100 meters of any space around it --> created a riparian zone
arcpy.analysis.Buffer(
    in_features="HYDRO_Rivers_and_Stream_Clip2.shp",
    out_feature_class=r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\midterm\midterm_528\buffed_rivers",
    buffer_distance_or_field="100 Meters",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="ALL",
    dissolve_field=None,
    method="PLANAR"
)

print("Rivers are Buffered in South Kingston")


