# coding challenge number 8
import arcpy


def describe_shapefile(towns, attribute_fields):
    # Describe the shapefile
    desc = arcpy.Describe('towns.shp')
    print("Describing: " + str('towns.shp'))
    if arcpy.Exists('towns.shp'):
        if desc.dataType == "ShapeFile":
            print("Feature Type:  " + desc.shapeType)
            print("Coordinate System Type:  " + desc.spatialReference.type)
            print("Coordinate System used:  " + desc.spatialReference.GCSName)

            # List attribute fields and their data types
            print("Attribute Fields:")
            fields = arcpy.ListFields('towns.shp')
            for field in fields:
                if field.name in attribute_fields:
                    print({field.name})
        else:
            print("Input data not ShapeFile..")
    else:
        print("Dataset not found, please check the file path..")



input_shapefile = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\coding_challenge_8"
attribute_fields = ["Field1", "Field2", "Field3"]
describe_shapefile('towns.shp', attribute_fields)
