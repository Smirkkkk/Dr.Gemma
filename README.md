# Dr.Gemma

The goal of this research is to develop a model based on deep learning. This model can provide reliable medical knowledge through a question-answering system (similar to ChatGPT). This model will focus on the medical field and provide help to a wide range of people, especially students and practitioners in the medical field or people in resource-poor areas. This project uses a dataset called MedQA, a collection of test questions based on a real medical exam (USMLE). This dataset includes many open-domain questions. This is also a difficult point in real-world situations.

## Model

In this task, we use MedQA to finetune Gemma2 2B. Gemma is a series of open-source lightweighted language models, developed by Google Deepmind. We choose the 2B version that has been pretrained on 2 trillion tokens, able to handle most of the text to text tasks.
