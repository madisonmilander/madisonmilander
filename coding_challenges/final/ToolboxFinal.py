# this is for the final toolbox challenge

import arcpy

# this toolbox will allow you to buffer, merge, and copy the shapefiles "RIDOTrds16.shp" and "towns.shp"

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "ToolboxFinal"
        self.alias = "Toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Buffer, Merge, Copy]

# The buffer class is buffering the roads
class Buffer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Buffer"
        self.description = "Creates a buffer around input features."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_features = arcpy.Parameter(name="input_features",
                                         displayName="Input Features",
                                         datatype="DEFeatureClass",
                                         parameterType="Required",
                                         direction="Input")
        input_features.value = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\RIDOTrds16.shp"
        params.append(input_features)
        buffer_distance = arcpy.Parameter(name="buffer_distance",
                                          displayName="Buffer Distance",
                                          datatype="GPDouble",
                                          parameterType="Required",
                                          direction="Input")
        params.append(buffer_distance)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output")
        output.value = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\road_buffer.shp"
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def execute(self, parameters, messages):
        """Buffer input features."""
        input_features = parameters[0].valueAsText
        buffer_distance = parameters[1].valueAsText
        output = parameters[2].valueAsText

        arcpy.Buffer_analysis(in_features=input_features,
                              out_feature_class=output,
                              buffer_distance_or_field=buffer_distance)
        return
print("Buffer Output Complete")

# this tool is allowing the merging of the road file and the towns of Rhode Island
class Merge(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Merge"
        self.description = "Merges multiple feature classes into one."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_features = arcpy.Parameter(name="input_features",
                                         displayName="Input Features",
                                         datatype="DEFeatureClass",
                                         parameterType="Required",
                                         direction="Input",
                                         multiValue=True)
        input_features.values = [r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\RIDOTrds16.shp", r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\towns.shp"]
        params.append(input_features)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output")
        output.value = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\road_town_merge.shp"
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def execute(self, parameters, messages):
        """Merge input feature classes."""
        input_features = parameters[0].valueAsText
        output = parameters[1].valueAsText

        # Check that inputs are shapefiles - arcpy.Describe..
        # if(filetype == "Shapefile"):
        # if not then exit
        # add some arcpy.AddMessages

        arcpy.Merge_management(inputs=input_features,
                                output=output)
        return
print("Merging of Road and Town in Rhode Island Complete")

class Copy(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Copy"
        self.description = "Copies input features to a new location."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_features = arcpy.Parameter(name="input_features",
                                         displayName="Input Features",
                                         datatype="DEFeatureClass",
                                         parameterType="Required",
                                         direction="Input")
        input_features.value = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\RIDOTrds16.shp"
        params.append(input_features)
        output_folder = arcpy.Parameter(name="output_folder",
                                        displayName="Output Folder",
                                        datatype="DEFolder",
                                        parameterType="Required",
                                        direction="Input")
        output_folder.value = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\copy_output_folder"
        params.append(output_folder)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def execute(self, parameters, messages):
        """Copy input features to output folder."""
        input_features = parameters[0].valueAsText
        output_folder = parameters[1].valueAsText

        arcpy.CopyFeatures_management(in_features=input_features,
                                      out_feature_class=output_folder)
        return
print("Copy Complete")

# # This code block allows you to run your code in a test-mode within PyCharm.
# def main():
#     tool = Buffer()  # Choose the tool you want to test
#     tool.execute(tool.getParameterInfo(), None)
#
# if __name__ == '__main__':
#     main()
