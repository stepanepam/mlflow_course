import mlflow
import openai
import pandas as pd
import os

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
mlflow.set_experiment("GPT4")

system_prompt = (
    "The following is a conversation with an AI assistant."
    + "The assistant is helpful and very friendly."
)

mlflow.start_run()
mlflow.log_param("system_prompt", system_prompt)

logged_model = mlflow.openai.log_model(
    model="gpt-4o-mini",
    task=openai.ChatCompletion,
    artifact_path="model",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "{question}"},
    ],
)

# Evaluate the model on some example questions
questions = pd.DataFrame(
    {
        "question": [
            "How do you create a run with MLflow?",
            "How do you log a model with MLflow?",
            "What is the capital of France?",
        ]
    }
)
mlflow.evaluate(
    model=logged_model.model_uri,
    model_type="question-answering",
    data=questions,
)
mlflow.end_run()
