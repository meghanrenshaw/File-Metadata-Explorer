import os

# creates an empty dictionary
file_metadata = {}
# user can choose which path to explore
# use ./test to search small file provided
inputpath = input("")

for root, directories, files in os.walk(inputpath):
    for _file in files:
        full_path = os.path.join(root, _file)
        size = os.path.getsize(full_path)
# adds to metadata dict -> full_path is key, size is value
        file_metadata[full_path] = size
# debug checkpoint
#print(file_metadata)


largest_file = 0
# sorts the files sizes by largest to smallest
for path, size in sorted(file_metadata.items(), key=lambda x:x[1], reverse=True):
    if largest_file > 0:
# break loop after largest file is found
        break
    print(f"Size: {size} bytes Path: {path}")
    largest_file +=1