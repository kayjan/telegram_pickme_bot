import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.app_init:app",
        reload=True,
        reload_dirs=["src"],
    )
