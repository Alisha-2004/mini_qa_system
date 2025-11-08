# Install the required libraries first
# pip install transformers torch

from transformers import pipeline

# Load a pretrained QA model
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Context paragraph
context = """
Mental health is an essential component of overall well-being. It affects how individuals think, feel, and behave in daily life. Mental health problems are common, ranging from anxiety and depression to severe psychiatric disorders. Factors such as genetics, environment, and lifestyle contribute to mental health. Regular physical activity, a balanced diet, adequate sleep, and strong social connections are protective factors that promote mental well-being. Early recognition and intervention are critical for managing mental health issues effectively. Therapy, medication, or a combination of both are standard treatment options. Additionally, awareness campaigns and educational programs help reduce stigma associated with mental health. Workplace initiatives, school programs, and community support groups play a crucial role in fostering a supportive environment for mental health. Understanding the importance of mental health and incorporating preventive measures into daily life can significantly improve the quality of life. Digital tools, such as mental health apps and online therapy platforms, are becoming increasingly popular for providing accessible mental health support. However, while technology offers convenience, professional guidance remains essential for proper diagnosis and treatment. Overall, prioritizing mental health alongside physical health ensures a holistic approach to wellness, enhancing resilience, productivity, and personal fulfillment.
"""

# Function to ask questions
def ask_question(question):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Example questions
questions = [
    "What factors contribute to mental health?",
    "What are standard treatment options for mental health issues?",
    "Why is early recognition important?",
    "How do digital tools help in mental health?"
]

# Run QA
for q in questions:
    print(f"Q: {q}")
    print(f"A: {ask_question(q)}\n")
