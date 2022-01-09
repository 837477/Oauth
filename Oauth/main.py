import uvicorn
from app import create_app
from config import config

app = create_app()
if __name__ == "__main__":
    print(config)
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=config.PORT,
        reload=config.RELOAD
    )
