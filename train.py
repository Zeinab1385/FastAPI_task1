from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import time

app = FastAPI(title="Titan Advanced Core")

# فعال‌سازی CORS برای اتصال به UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# دیتابیس مجازی برای ذخیره آمار
stats = {"requests_count": 0, "start_time": time.time()}

@app.get("/")
def read_root():
    stats["requests_count"] += 1
    return {
        "status": "Online",
        "message": "Welcome to Titan API",
        "server_time": datetime.now().strftime("%H:%M:%S")
    }

@app.get("/hello/{name}")
def say_hello_name(name: str):
    stats["requests_count"] += 1
    return {
        "greeting": f"Hello, {name}!",
        "length": len(name),
        "timestamp": datetime.now().isoformat()
    }

@app.get("/user")
def say_user(name: str = Query(..., min_length=2)):
    stats["requests_count"] += 1
    return {"user_status": f"{name} is active", "access_level": "Standard"}

@app.get("/system/stats")
def get_system_stats():
    uptime = time.time() - stats["start_time"]
    return {
        "total_requests": stats["requests_count"],
        "uptime_seconds": int(uptime),
        "version": "2.1.0"
    }

@app.get("/{name}")
def direct_path(name: str):
    return {"message": f"Direct access to: {name}", "method": "Direct Path"}