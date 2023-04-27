import sys
print(sys.version)

import os
os.environ['ACTIVELOOP_TOKEN'] = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTY4MjQ1NTc1OCwiZXhwIjoxNjg4MTU4MDIwfQ.eyJpZCI6ImVkbXVuZGJlcmttYW5uIn0.vaP4o-zEc-NSuUJQher8iemlXd-cL_uibN_nfgPdWALEQTMPMgZttZZjOq1NUtsLWJZ_B8wRTgp2UhHGkUDFpg"

import deeplake

ds = deeplake.dataset('hub://Steelo/Steelo-dataset')




deeplake_path = 'hub://edmundberkmann/dataset_name' 

# Define an empty Deep Lake dataset 
ds = deeplake.empty(deeplake_path, token = <your_api_token>) 

with ds: 
	# Define tensors in the Deep Lake dataset 
	ds.create_tensor('tensor_1', htype = 'htype_1', sample_compression = 'compression_1') 
	ds.create_tensor('tensor_2', htype = 'htype_2', sample_compression = 'compression_2') 
	ds.create_tensor('tensor_3', htype = 'htype_3', sample_compression = 'compression_3') 

	# Iterate through the primary data (typically a list of files, like images) 
	for file in files: 
		metadata_1, metadata_2 = get_metadata_for_file(file) # Find the metadata correspoding to the primary data 

		# Append all data as a row(sample) in the Deep Lake dataset 
		ds.append({'tensor_1': deeplake.read(file),
		 'tensor_2': metadata_1,
		 'tensor_3': metadata_2})