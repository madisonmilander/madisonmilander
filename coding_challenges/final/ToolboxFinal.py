import arcpy
import os


# this toolbox will allow you to buffer, merge, and copy the shapefiles "buildingFootprints18.shp" and "towns.shp"

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Town and Building's of Rhode Island Toolbox"
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
        arcpy.Describe(
            r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\buildingFootprints18.shp")
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
        output.value = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\building_buffer.shp"
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
        arcpy.AddMessage("Buffer Complete")
        return


# this tool is allowing the merging of the Building file and the towns of Rhode Island
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
        arcpy.Describe(
            r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\buildingFootprints18.shp",
            r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\towns.shp")
        params.append(input_features)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output")
        output.value = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\building_town_merge.shp"
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def execute(self, parameters, messages):
        """Merge input feature classes."""
        input_features = parameters[0].valueAsText
        output = parameters[1].valueAsText

        arcpy.Merge_management(inputs=input_features,
                               output=output)
        arcpy.AddMessage("Merging of Building and Town in Rhode Island Complete")
        return


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
        arcpy.Describe(
            r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\buildingFootprints18.shp")
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
<<<<<<< Updated upstream

        arcpy.AddMessage("Copy Complete")
        return

=======
>>>>>>> Stashed changes

        arcpy.AddMessage("Copy Complete")
        return



def main():
    # Create instances of the tools
    buffer_tool = Buffer()
    merge_tool = Merge()
    copy_tool = Copy()

    # Get parameter information for the Buffer tool
    buffer_params = buffer_tool.getParameterInfo()
    merge_params = merge_tool.getParameterInfo()
    copy_params = copy_tool.getParameterInfo()

    # Set parameters for Buffer tool
    buffer_params[0].value = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\buildingFootprints18.shp"
    buffer_params[1].value = 100
    buffer_output_path = buffer_params[2].value
    if arcpy.Exists(buffer_output_path):
        arcpy.Delete_management(buffer_output_path)

    # Execute the Buffer tool
    buffer_tool.execute(buffer_params, None)

    # Set parameters for Merge tool
    merge_params[0].values = [r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\buildingFootprints18.shp", r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\towns.shp"]
    merge_output_path = merge_params[1].value
    if arcpy.Exists(merge_output_path):
        arcpy.Delete_management(merge_output_path)

    # Execute the Merge tool
    merge_tool.execute(merge_params, None)



if __name__ == '__main__':
    main()

