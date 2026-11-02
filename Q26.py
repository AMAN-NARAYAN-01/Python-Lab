import matplotlib.pyplot as plt

def visualize_study_scores():
    # Data definition
    students = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10']
    study_hours = [8, 10, 12, 15, 18, 20, 7, 14, 16, 22]
    exam_scores = [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]

    # Create a figure with 1 row and 3 columns for subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))

    # 1. Histogram: Distribution of Study Hours
    ax1.hist(study_hours, bins=5, color='skyblue', edgecolor='black')
    ax1.set_title('Distribution of Study Hours')
    ax1.set_xlabel('Study Hours / Week')
    ax1.set_ylabel('Frequency')
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    # 2. Histogram: Distribution of Exam Scores
    ax2.hist(exam_scores, bins=5, color='lightgreen', edgecolor='black')
    ax2.set_title('Distribution of Exam Scores')
    ax2.set_xlabel('Exam Score')
    ax2.set_ylabel('Frequency')
    ax2.grid(axis='y', linestyle='--', alpha=0.7)

    # 3. Scatter Plot: Relationship between Study Hours and Exam Scores
    ax3.scatter(study_hours, exam_scores, color='purple', s=100, alpha=0.8, edgecolors='black')
    ax3.set_title('Study Hours vs. Exam Scores')
    ax3.set_xlabel('Study Hours / Week')
    ax3.set_ylabel('Exam Score')
    ax3.grid(True, linestyle='--', alpha=0.7)
    
    # Annotate points with student labels
    for i, txt in enumerate(students):
        ax3.annotate(txt, (study_hours[i], exam_scores[i]), 
                     textcoords="offset points", xytext=(0, 10), ha='center')

    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()

# Execute the visualization function
visualize_study_scores()
