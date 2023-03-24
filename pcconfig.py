import pynecone as pc

config = pc.Config(
    app_name="OnlyPython_Website",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
