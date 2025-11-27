# 📰 Tripura News – Django + Tailwind News Website

A modern and responsive news website built using **Django** and **Tailwind CSS**.  
This project includes a beautiful mobile-friendly navbar, animated breaking-news ticker, sidebar updates, and a two-column layout for headlines and full news content.

---

## 🚀 Features

- ✔️ Django backend with models & dynamic data  
- ✔️ Tailwind CSS (CDN) for modern UI  
- ✔️ Fully mobile responsive  
- ✔️ Mobile hamburger menu  
- ✔️ Animated breaking news ticker (right → left)  
- ✔️ Latest news sidebar  
- ✔️ Search functionality  
- ✔️ Beautiful background images and colorful layout  
- ✔️ Django admin panel for managing news  

---

## 📂 Project Structure

```
news_project/
│── manage.py
│── README.md
│
├── news/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── static/news/
│   │     └── ticker.js
│   └── templates/news/
│         ├── base.html
│         └── home.html
│
└── news_project/
    ├── settings.py
    └── urls.py
```

---

## 🛠 Installation

### 1️⃣ Create Virtual Environment
```
python -m venv env
```

### 2️⃣ Activate Environment  
**Windows**
```
env\Scripts\activate
```
**Mac/Linux**
```
source env/bin/activate
```

### 3️⃣ Install Requirements
```
pip install django pillow
```

---

## 🗄 Database Setup

### Run Migrations
```
python manage.py migrate
```

### Create Superuser
```
python manage.py createsuperuser
```

---

## ▶️ Run the Server

```
python manage.py runserver
```

Visit:  
**http://127.0.0.1:8000/**

---

## 📰 Django Model (News)

```python
class News(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```

---

## 🎨 Frontend Notes (Tailwind + Background Images)

- Tailwind loaded using CDN (no npm required)
- Fully responsive layout
- Mobile hamburger navigation menu
- Background image support
- Animated ticker
- Clean UI with Tailwind components

---

## 🔁 Breaking News Ticker (ticker.js)

```javascript
document.addEventListener("DOMContentLoaded", function () {
  const ticker = document.querySelector(".ticker");
  ticker.innerHTML += " • " + ticker.innerHTML;
});
```

---

## 🌐 URLs

### app `news/urls.py`
```python
urlpatterns = [
    path("", home, name="home"),
]
```

### main `urls.py`
```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("news.urls")),
]
```

---

## 📸 Screenshots  
(Add screenshots when project runs)

---

## 📄 License
This project is free for personal and educational use.

---

## 👨‍💻 Author
**Developed by:** David Kudrot  
**Technology:** Django + Tailwind  

---
