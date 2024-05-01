# Rhode Island Buildings and Towns Toolbox
## NRS 528 Final Toolbox 

This Python Toolbox contains a collection of tools designed for geoprocessing and file management operations. 

Overview
The toolbox offers a set of simple tools implemented using Python and the ArcPy library. These tools facilitate various spatial analysis tasks and streamline file management operations.

Installation
To use this toolbox, follow the steps below:

Clone or download this repository to your local machine.
Open ArcGIS Pro or ArcMap.
Add the Python Toolbox file (ToolboxFinal.pyt) to your project.

Tools

**1. Buffer**

This tool creates a buffer around input features.

*Input Features*: r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\buildingFootprints18.shp"

Buffer Distance: Enter the desired buffer distance.

*Output*: r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\building_buffer.shp"

**2. Merge**

The Merge tool combines multiple feature classes into a single feature class.

*Input Features*: [r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\buildingFootprints18.shp", r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\towns.shp"]

*Output*: r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\building_town_merge.shp"

**3. Copy**

Copy tool duplicates input features to a new location.

*Input Features*: r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\buildingFootprints18.shp"

*Output Folder*: r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\githubrepository\coding_challenges\final\copy_output_folder"

**Example Data**
- buildingFootprints18.shp
- towns.shp
Collected through RIGIS.org


Usage
Follow these steps to use the toolbox:

Open ArcGIS Pro or ArcMap.
Add the Python Toolbox (ToolboxFinal.pyt) to your project.
Double-click on a tool to launch its dialog box.
Input the required parameters and click "OK" to execute the tool.
