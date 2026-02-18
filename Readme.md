<div dir="ltr">

# 🌌 Titan Advanced Core: Full-Stack API Ecosystem

![FastAPI](https://img.shields.io/badge/Backend-FastAPI-05998b?style=for-the-badge&logo=fastapi)
![Tailwind](https://img.shields.io/badge/Frontend-Tailwind_CSS-38bdf8?style=for-the-badge&logo=tailwind-css)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)

## 📖 Overview
Titan Advanced Core is a robust, full-stack application designed to demonstrate the interaction between a high-performance **FastAPI** backend and a reactive **Tailwind-based** frontend. The project focuses on real-time data tracking, state persistence, and modern UI/UX principles.



## 🛠 Technical Deep Dive

### 1. Backend Architecture (`main.py`)
The backend is built with FastAPI and features:
* **State Management**: Uses a global `stats` dictionary to persist request counts and server start time without a database.
* **CORS Middleware**: Fully configured to allow cross-origin requests, enabling the frontend to communicate with the API from any port.
* **Advanced Routing**: Implements Path parameters, Query parameters, and direct path handling.

### 2. Frontend Interface (`index.html`)
The frontend is a Single Page Application (SPA) that features:
* **Dynamic URL Construction**: A real-time JavaScript logic that builds and displays the exact API endpoint URL as the user types.
* **Visual Feedback**: Uses `Animate.css` for smooth transitions and a dedicated "Response JSON" console for clear data visualization.
* **Performance Tracking**: Measures the round-trip time (Latency) for every request in milliseconds.

## 📡 API Reference
| Endpoint | Method | Parameter Type | Logic |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | N/A | Returns system status and formatted server time. |
| `/hello/{name}` | `GET` | Path | Greets the user and analyzes the string length. |
| `/user` | `GET` | Query | Validates user activity with a minimum length constraint. |
| `/system/stats` | `GET` | N/A | Calculates and returns total hits and server uptime. |

</div>

---

<div dir="rtl">

# 🌌 اکوسیستم پیشرفته Titan Core

این پروژه یک راهکار کامل (Full-Stack) برای نمایش قدرت تعامل بین سرویس‌های بک‌اَند **FastAPI** و رابط‌های کاربری مدرن است. تمرکز اصلی این پروژه بر مانیتورینگ زنده، مدیریت وضعیت سرور و تجربه کاربری (UX) سطح بالاست.

## 🚀 ویژگی‌های برجسته فنی

### ۱. مدیریت هوشمند وضعیت (Backend Logic)
در فایل `main.py`، ما از دیتابیس مجازی استفاده کردیم:
* **محاسبه Uptime**: سیستم به محض اجرا، زمان شروع را ثبت کرده و در هر لحظه میزان دقیق فعالیت سرور را به ثانیه محاسبه می‌کند.
* **شمارنده درخواست‌ها**: تمامی تعاملات کاربر با تمام اندپوینت‌ها رصد شده و آمار تجمعی آن در حافظه RAM سرور نگهداری می‌شود.

### ۲. رابط کاربری تعاملی (Frontend Architecture)
فایل `index.html` فراتر از یک فرم ساده است:
* **ردیاب لحظه‌ای URL**: یکی از بخش‌های کلیدی، نمایش آنی URL ساخته شده است. این قابلیت به توسعه‌دهنده کمک می‌کند تفاوت دقیق بین `Path Parameter` و `Query Parameter` را به صورت بصری درک کند.
* **استایل شیشه‌ای (Glassmorphism)**: استفاده از `backdrop-filter` و گرادینت‌های نئونی برای ایجاد ظاهری کاملاً مدرن و حرفه‌ای.

## 💡 لیست آموخته‌ها و دستاوردهای پروژه
این بخش برای ارائه به منتور تهیه شده است:
* **درک عمیق CORS**: یادگیری نحوه باز کردن دسترسی‌های امنیتی برای اجازه تعامل مرورگر با سرور پایتونی.
* **ارتباط غیرهمزمان (Async/Await)**: پیاده‌سازی `fetch` در جاوااسکریپت به گونه‌ای که رابط کاربری هنگام انتظار برای پاسخ سرور، "قفل" نشود.
* **اعتبارسنجی داده‌ها**: استفاده از قابلیت‌های FastAPI برای اجباری کردن پارامترها و کنترل طول رشته‌های ورودی.

## 🚦 راهنمای راه‌اندازی سریع

۱. **نصب پیشنیازها**:
   `pip install fastapi uvicorn`
   
۲. **اجرای هسته مرکزی**:
   `uvicorn main:app --reload`
   
۳. **دسترسی به پنل**:
   فایل `index.html` را باز کرده و از داشبورد نئونی برای تست اندپوینت‌ها استفاده کنید.



</div>