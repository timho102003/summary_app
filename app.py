import beam

app = beam.App(
    name="openai_summary_app",
    cpu=8,
    memory="8Gi",
    python_version="python3.9",
    python_packages="requirements.txt",
)

app.Trigger.RestAPI(
    inputs={"api_key": beam.Types.String(), 
            "article": beam.Types.String()},  # Accepts a base64-encoded string as input
    outputs={"response": beam.Types.String()},
    handler="run.py:call",
)