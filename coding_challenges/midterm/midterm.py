# This is for the midterm
# This first part is selecting the town of South Kingston

import arcpy

arcpy.env.overwriteOutput = True

arcpy.analysis.Select(
    in_features="staCons18",
    out_feature_class=r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\midterm\midterm_528\study_area",
    where_clause="NAME = 'Cioe/Tillinghast' Or NAME = 'Robert Pratt / 4400274.tif'"
)
