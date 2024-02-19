import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    try:
        uvicorn.run(
            app=str(os.getenv("APP", "backend.app:app")),
            port=int(os.getenv("PORT", 8000)),
            app_dir=str(os.getenv("APP_DIR", "backend")),
            reload=bool(True),
        )
    except:
        raise Exception("Error in uvicorn.run")