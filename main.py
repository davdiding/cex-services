from fastapi import FastAPI
import uvicorn
app = FastAPI()

# Import and register your routers here
# Example:
# from .routers import users, products
# app.include_router(users.router)
# app.include_router(products.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)