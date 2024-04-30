def analyze_waterfall_model(diagram_name):
    steps = [
        "Communication and Project Initiation",
        "Requirements Gathering",
        "Planning with Blocks of Hours",
        "Estimating Development Package Hours",
        "Design and Feedback",
        "Prototype Development and Feedback (Iterative)",
        "Build, Implementation, and Feedback (Iterative)",
        "Testing, User & Stakeholder Testing, Quality Assurance, and Feedback (Iterative)",
        "User Acceptance and Approval",
        "Deployment and Release",
        "Monitoring and Support",
        "Feedback and Continuous Improvement"
    ]
    num_steps = len(steps)
    return steps, num_steps

# Input the name of the diagram
diagram_name = input("Enter the name of the diagram: ")

# Analyze the waterfall model
steps, num_steps = analyze_waterfall_model(diagram_name)

# Output the steps in a list form
print("Steps:")
for step in steps:
    print("-", step)

# Output the number of steps
print("Number of steps:", num_steps)
