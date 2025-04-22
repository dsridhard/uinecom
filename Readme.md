# 🛍️ Unified Commerce Django Project

A modular Django-based e-commerce backend that supports product listings, customer management, order processing, payments, and reviews.

---

## 📦 Project Structure

```bash
unifedcom/
├── manage.py
├── unifedcom/         # Main Django project folder
├── unified/           # Product management
├── customer/          # Customer data and profiles
├── orders/            # Order and shipping info
├── payments/          # Payment and transaction tracking
├── reviews/           # Product reviews and ratings
🧱 Apps and Models
🔹 unified app
Handles product listings and inventory.

Models:

Product: title, description, price, stock, etc.

Category: name, description

Inventory: stock level, SKU, warehouse location

🔹 customer app
Manages customer details and profiles.

Models:

Customer: name, email, phone, etc.

Address: line1, city, state, country, postal code

CustomerProfile: gender, date_of_birth, loyalty_points, etc.

🔹 orders app
Handles order creation and shipping.

Models:

Order: customer, ordered_date, is_paid, total_amount, status, etc.

OrderItem: product, quantity, price

ShippingAddress: address_line1, city, country, etc.

🔹 payments app
Handles payment information.

Models:

Payment: order, amount, method

Transaction: status, transaction_id, gateway_response

🔹 reviews app
Manages customer feedback on products.

Models:

Review: product, customer, content

Rating: product, customer, rating (1-5 stars)

⚙️ Setup Instructions
Clone the repository:

Step 1:
git clone https://github.com/your-username/unifedcom.git
cd unifedcom
Create a virtual environment & activate it:

Step 2:
python -m venv venv
venv\Scripts\activate    # On Windows
Install dependencies:

Step 3:
pip install -r requirements.txt
Apply migrations:

Step 4:
python manage.py makemigrations
python manage.py migrate
Run the development server:

Step 5:

python manage.py runserver
Access the site:
Open your browser and go to: http://localhost:8000

📋 Admin Access
To access the Django admin panel:

#Run Command
python manage.py createsuperuser
Then login at: http://localhost:8000/admin

✅ Features
Modular architecture with multiple Django apps

Full CRUD operations for products, customers, and orders

Payment and transaction tracking

Reviews and ratings on products

Time-stamped record creation and updates

🚀 Future Enhancements
Add user authentication via JWT or OAuth

Integrate external payment gateways (Razorpay, Stripe)

Implement API with Django Rest Framework

Add product search and filtering

Add Celery for background order processing

🧑‍💻 Developed By
Sridhar
GitHub | LinkedIn