# 🎓 Placement Management System

A comprehensive Django-based web application for managing student placements, job applications, and company interactions.

## 🚀 Features

- **Student Portal**: Profile management, job applications, status tracking
- **Company Portal**: Job posting, application management, hiring process
- **Admin Panel**: User management, statistics, system administration
- **Staff Management**: Department-wise student coordination
- **Modern UI**: Professional, responsive design with gradient styling

## 🛠️ Technology Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite3 (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Icons**: Font Awesome
- **Deployment**: Gunicorn, WSGI

## 📋 Prerequisites

- Python 3.8+
- pip
- Git

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Placement-Management-System-main
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Home: http://localhost:8000
   - Admin: http://localhost:8000/admin

## 👥 Default Users

### Admin Users
- **Username**: `admin` | **Password**: `admin123`

### Staff Users (Password: `123456`)
- `IT_HOD`, `CE_HOD`, `ECE_HOD`, `CSE_HOD`, `ME_HOD`, `EEE_HOD`, `AIDS_HOD`, `AEI_HOD`

### Company Users (Password: `123456`)
- `Wipro`, `Infosys`, `Amazon`, `TCS`, `People10`, `Mindtree`, `Microsoft`, `HCL`, `Cognizant`

### Student Users (Password: `123456`)
- `Ashwin_IT`, `Ashleen_IT`, `Mishal_CSE`


## 📁 Project Structure

```
Placement-Management-System-main/
├── stdplacement/          # Main Django project
├── register/             # User registration & auth
├── std_app/             # Student functionality
├── company/             # Company portal
├── staff_app/           # Staff management
├── student_import/      # CSV import functionality
├── templates/           # HTML templates
├── static/              # CSS/JS files
├── media/               # Uploaded files
├── requirements.txt     # Python dependencies
├── Procfile            # Deployment configuration
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables

- `DEBUG`: Set to `False` in production
- `SECRET_KEY`: Django secret key
- `DATABASE_URL`: Database connection string (for production)

### Static Files

Static files are configured to be served from the `static/` directory and collected to `static_root/` for production.

### Media Files

Uploaded files (images, documents) are stored in the `media/` directory.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Contact the development team

---

**Made with ❤️ for better placement management**
