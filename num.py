import numpy as np 
import matplotlib.pyplot as plt 

# Set random seed for reproducibility
np.random.seed(42)

# Step 1: Generate random exam scores for 50 students (scores between 0 and 100)
num_students = 50
scores = np.random.normal(loc=75, scale=15, size=num_students).astype(int)
# Ensure scores are within [0, 100]
scores = np.clip(scores, 0, 100)

# Step 2: Compute basic statistics
mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)
max_score = np.max(scores)
min_score = np.min(scores)

# Step 3: Identify top performers (scores >= 85)
top_performers = scores[scores >= 85]
num_top_performers = len(top_performers)

# Step 4: Print detailed results
print("=== Student Exam Score Analysis ===")
print(f"Total number of students: {num_students}")
print("\nBasic Statistics:")
print(f"Mean Score: {mean_score:.2f}")
print(f"Median Score: {median_score:.2f}")
print(f"Standard Deviation: {std_score:.2f}")
print(f"Maximum Score: {max_score}")
print(f"Minimum Score: {min_score}")
print("\nTop Performers (Score >= 85):")
print(f"Number of top performers: {num_top_performers}")
print(f"Top scores: {top_performers}")
print("\nAll Scores:")
print(scores)

# Step 5: Visualize the score distribution
plt.figure(figsize=(8, 5))
plt.hist(scores, bins=10, edgecolor='black', alpha=0.7)
plt.title('Distribution of Student Exam Scores')
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.axvline(mean_score, color='red', linestyle='--', label=f'Mean: {mean_score:.2f}')
plt.axvline(median_score, color='green', linestyle='--', label=f'Median: {median_score:.2f}')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()