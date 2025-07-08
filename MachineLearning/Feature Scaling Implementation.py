#a Python function that performs feature scaling on a dataset using both standardization and min-max normalization. 
#The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. It should return two 2D NumPy arrays:
#one scaled by standardization and one by min-max normalization.
#Feature scaling is like translating all measurements to the same unit and scale, so theyâre on equal footing:

#Instead of comparing 5 m/min to 200 km/h, we transform them both into a range like 0 to 1, or a standard normal distribution (mean 0, std 1), both separately.
import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    samples,features = data.shape

    #axis=0: Down the rows (i.e., column-wise)
    #axis=1: Across the columns (i.e., row-wise)
    #'feature' scaling is column wise
    standardized_data=(data-data.mean(axis=0))/data.std(axis=0)
    normalized_data=(data-data.min(axis=0))/(data.max(axis=0)-data.min(axis=0))
	
	return standardized_data.round(4), normalized_data.round(4)
