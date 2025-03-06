# Free Udemy Courses API

[![Django](https://img.shields.io/badge/Django-5.0+-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.15.2-red.svg)](https://www.django-rest-framework.org/)
[![HTMX](https://img.shields.io/badge/HTMX-1.9+-blue.svg)](https://htmx.org/)
[![Django-Allauth](https://img.shields.io/badge/Django--Allauth-64.1+-purple.svg)](https://django-allauth.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A Django REST Framework (DRF) project that provides free Udemy courses with coupon details. This API allows developers to integrate free educational content into their applications, websites, or bots.

## 📋 Table of Contents

- [Features](#-features)
- [API Endpoints](#-api-endpoints)
- [Authentication](#-authentication)
- [Setup Instructions](#-setup-instructions)
- [Usage Examples](#-usage-examples)
- [Dashboard](#-dashboard)
- [Rate Limits](#-rate-limits)
- [Contact](#-contact)

---

## 🌐 Want to Explore Courses?

If you’re looking to explore free Udemy courses rather than using the API, visit the [Explore Page](https://couponhub.srachn.com/explore). Alternatively, you can use the [UdemyBot](https://t.me/Udemy_corse_bot) to get notified whenever courses you're interested in become available.

## 🚀 Features

- **Real-time Coupon Updates**: Access the latest free Udemy courses
- **Detailed Course Information**: Get comprehensive course details including ratings, student count, and content length
- **Custom Token Authentication**: Secure API access with custom tokens
- **User Activity Tracking**: Monitor API usage with detailed analytics
- **Web Dashboard**: Visualize your API usage and available coupons
- **Course Search**: Find specific courses by title or description(in '/explore' endpoint)

## 🔌 API Endpoints

| Endpoint | Method | Description | Authentication |
|----------|--------|-------------|----------------|
| `/api/courses/` | GET | Fetch a list of free Udemy courses | Required |
| `/api/courses/<id>/` | GET | Get details for a specific course | Required |

## 🔑 Authentication

All API requests require authentication using a custom token:

```
token: your_api_token
```

To obtain your token:
1. Register for an account on the platform
2. Log in to your account
3. Your API token will be displayed on the home page

## 🔧 Setup Instructions

### Prerequisites

- Python 3.8+

### Installation

1️⃣ Clone the repository:

```sh
git clone https://github.com/sualh1999/Free-Udemy-Coupon-API.git
cd free-udemy-api
```

2️⃣ Install dependencies:

```sh
pip install -r requirements.txt
```

3️⃣ Apply migrations:

```sh
python manage.py migrate
```

4️⃣ Run the development server:

```sh
python manage.py runserver
```

## 📘 Usage Examples

### Python

```python
import requests

url = "https://your-api-domain.com/api/courses/"
headers = {"token": "your_api_token"}

response = requests.get(url, headers=headers)
courses = response.json()

for course in courses['results']:
    print(f"Course: {course['title']}")
    print(f"Link: {course['link']}?couponCode={course['coupon']['coupon_str']}")
    print("---")
```

### JavaScript

```javascript
fetch('https://your-api-domain.com/api/courses/', {
  headers: {
    'token': 'your_api_token'
  }
})
.then(response => response.json())
.then(data => {
  data.results.forEach(course => {
    console.log(`Course: ${course.title}`);
    console.log(`Link: ${course.link}?couponCode=${course.coupon.coupon_str}`);
    console.log('---');
  });
});
```

## 📊 Dashboard

The API includes a web dashboard that provides:

- Visual analytics of your API usage
- Number of active coupons
- Total request count
- Historical usage data

Access the dashboard at `/dashboard` after logging in.

## ⏱ Rate Limits

To ensure fair usage, the API implements rate limiting. If you exceed the limit, you'll receive a response with a `Retry-After` header indicating when you can resume making requests.

## 🤝 Contribute

Want to contribute to this project? We welcome contributions of all kinds! Whether you're fixing bugs, improving documentation, or proposing new features, your help is appreciated.

### TODO

- Optimize HTML templates to reduce the HTML percentage in the repository (currently >65%), as GitHub is classifying this as an HTML project rather than Python/Django
- Add more API endpoints for filtering courses by category
- Improve test coverage

## 📩 Contact

Have questions or need support? Reach out via [Telegram: @huam3](https://t.me/huam3)

---


