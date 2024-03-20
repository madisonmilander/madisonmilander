# # part one of coding challenge 3
# # use these directory trees to create tree
#
# import os
#
# os.workspace = r"C:\Users\mmilander\OneDrive - University of Rhode Island\NRS 528\coding_challenge_3\codingchallenge3"
#
#
# def create_directory_tree():
#     try:
#         os.mkdir("draft_code/pending")
#         os.mkdir("draft_code/complete")
#         os.mkdir("includes")
#         os.mkdir("layouts/default")
#         os.mkdir("layouts/post/posted")
#         os.mkdir("site")
#         print("Directory tree created successfully")
#     except OSError as e:
#         print("Error: {e.strerror}")
#
#
# # shutil.rmtree will delete the sub directory and tree without the entire hard drive
#
# import shutil
#
# def delete_directory_tree():
#     try:
#         shutil.rmtree("draft_code")
#         shutil.rmtree("includes")
#         shutil.rmtree("layouts")
#         shutil.rmtree("site")
#         print("Directory tree deleted successfully")
#     except OSError as e:
#         print("Error: {e.strerror}")
#
#
# if __name__ == "__main__":
#     create_directory_tree()
#     # delete directory tree
#     delete_directory_tree()
