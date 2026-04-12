# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

#Convert list into tuple
shelf1_update_tuple = tuple(shelf1_update)
#Concatenate
shelf1_concat = shelf1 + shelf1_update_tuple
#Count
celery_count = shelf1_concat.count("celery")
#Index
celery_index = shelf1_concat.index("celery")

print("Updated Shelf #1:", shelf1_concat)
print("Number of Celery:", celery_count)
print("Celery Index:", celery_index)
