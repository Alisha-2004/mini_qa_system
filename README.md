# Interactive Health QA System

An **interactive question-answering (QA) system** that provides **detailed answers** about mental health based on a given paragraph. Unlike extractive QA models that return short phrases, this system uses a **generative transformer model** to provide **paragraph-length, explanatory answers**.

---

## Features

- **Generative QA:** Uses the `google/flan-t5-base` model to generate detailed answers.
- **Interactive:** Ask questions dynamically in the terminal.
- **Health-focused:** Provides answers based on a context paragraph about mental health.
- **Easy to run:** Simple Python script, requires only a few libraries.
- **Customizable:** Update the context paragraph to cover other topics.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/interactive-health-qa.git
cd interactive-health-qa
