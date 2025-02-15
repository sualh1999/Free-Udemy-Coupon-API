=============================
Free Udemy Courses API

A Django REST Framework (DRF) project that provides free Udemy courses with coupon details. Users must authenticate using a custom token to fetch available courses.

🚀 Current Features:

✅ GET /api/courses/ - Fetch a list of free Udemy courses (requires a token).
✅ GET /api/generate-token/ - To generate token(since there's no authentication it doesn't work)

🔧 Setup Instructions:

1️⃣ Clone the repository:

   git clone https://github.com/sualh1999/Free-Udemy-Coupon-API.git
   cd free-udemy-api

2️⃣ Install dependencies:

   pip install -r requirements.txt

3️⃣ Apply migrations:

   python manage.py migrate

4️⃣ Run the development server:

   python manage.py runserver



🛠 To-Do List (Planned Features):

✅ Implement token-based authentication.

⏳ Add signup & login functionality.

⏳ Allow users to generate their own tokens.

⏳ Implement user roles & permissions.

⏳ Create an admin panel for managing courses & users.

⏳ Add a frontend UI for easier interaction.



📩 Contact:

Have questions? Reach out via [https://t.me/huam3]

