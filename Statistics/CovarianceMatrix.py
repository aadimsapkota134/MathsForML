#a Python function to calculate the covariance matrix for a given set of vectors.
#The function should take a list of lists, where each inner list represents a feature with its observations, and return a covariance matrix as a list of lists.

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    features_count = len(vectors) #represents row.
    # each row is a feature vector. each column is a feature.
    elements_count = len(vectors[0]) #represents column

    #Calculate the mean of each feature
    means = [sum(feature) / elements_count for feature in vectors]

    #Given a dataset with n features, the covariance matrix is constructed as n*n. this is because a covariance matrix is designed to capture the relationships
  #between pairs of features in a dataset. Since each feature needs to be compared with every other feature (including itself), the matrix must be nÃÂn to 
  #accommodate all these comparisons
    cov_matrix = [[0.0]* features_count for _ in range(features_count)]
    for i in range(features_count): # i is for the first feature
        for j in range(features_count): #j is for the second feature
            covariance=0.0
            for k in range(elements_count):
			
