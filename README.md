# 🎓 Campus Placement Management System

A comprehensive Django-based web application for managing student placements, job applications, and company interactions.

## 🌐 Live Demo

**Visit the live application:** [https://placement-management-system-g7on.onrender.com/](https://placement-management-system-g7on.onrender.com/)

## ✨ Features

### 🎯 **Student Portal**
- **Profile Management**: Complete student profile with personal, academic, and family details
- **Job Applications**: Browse and apply for up to 3 job positions
- **Application Tracking**: Real-time status updates (Accepted, Rejected, Rounds, Placed)
- **Requirements Check**: Automatic eligibility verification (CGPA, supply count, percentages)
- **Document Upload**: Profile image and resume upload functionality

### 🏢 **Company Portal**
- **Job Posting**: Create detailed job listings with requirements
- **Application Management**: Review and manage student applications
- **Status Updates**: Update application status through multiple rounds
- **Company Profile**: Upload company logos and maintain company information
- **Hiring Process**: Complete workflow from application to placement

### 👨‍💼 **Admin Panel**
- **User Management**: Create and manage all user types (Students, Companies, Staff)
- **Statistics Dashboard**: Manual entry of placement statistics and charts
- **System Control**: Enable/disable job application periods using button controls
- **Data Import**: CSV import functionality for bulk student registration
- **System Monitoring**: View all activities and manage system settings

### 👥 **Staff Management**
- **Department Coordination**: Department-wise student management
- **Student Registration**: Handle student onboarding and profile creation
- **Placement Coordination**: Coordinate between students and companies
- **Data Management**: Maintain student records and academic information

### 📊 **Dashboard Features**
- **Interactive Charts**: Manually entered statistics displayed as charts
- **Real-time Updates**: Dynamic dashboard with live data
- **Placement Analytics**: Comprehensive placement statistics
- **User Activity Tracking**: Monitor system usage and activities

### 🎨 **Modern UI/UX**
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Professional Styling**: Modern gradient designs and clean interfaces
- **Intuitive Navigation**: Easy-to-use navigation with clear user roles
- **Visual Feedback**: Status indicators and progress tracking

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Icons**: Font Awesome
- **Deployment**: Render.com

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AshwinSajiKumar/Placement-Management-System.git
   cd Placement-Management-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open browser and go to: http://127.0.0.1:8000

## 👥 User Roles & Access

### Admin
- **Username**: admin
- **Password**: admin123
- **Access**: Full system management, statistics entry, button controls

### Staff Users (Password: 123456)
- **IT_HOD** - Information Technology Head
- **CE_HOD** - Civil Engineering Head  
- **ECE_HOD** - Electronics & Communication Engineering Head
- **CSE_HOD** - Computer Science Engineering Head
- **ME_HOD** - Mechanical Engineering Head
- **EEE_HOD** - Electrical & Electronic Engineering Head
- **AIDS_HOD** - Artificial Intelligence & Data Science Head
- **AEI_HOD** - Applied Electronics & Instrumentation Head

### Company Users (Password: 123456)
- **Wipro** - Wipro Limited
- **Infosys** - Infosys Limited
- **Amazon** - Amazon Web Services
- **TCS** - Tata Consultancy Services
- **People10** - People10 Technologies
- **Mindtree** - Mindtree Limited
- **Microsoft** - Microsoft Corporation
- **HCL** - HCL Technologies
- **Cognizant** - Cognizant Technology Solutions

### Student Users (Password: 123456)
- **Ashwin_IT** - Ashwin (Information Technology)
- **Ashleen_IT** - Ashleen (Information Technology)
- **Mishal_CSE** - Mishal (Computer Science Engineering)

### New Users
- **Students & Companies**: Register through the respective portals
- **Use the registration forms** to create new accounts

## 🎯 **Key System Features**

### **Application Control System**
- **Admin-controlled buttons**: Enable/disable job applications during placement seasons
- **Application limits**: Students can apply for maximum 3 jobs
- **Eligibility checks**: Automatic verification of CGPA, supply count, and percentages
- **Status tracking**: Real-time application status updates

### **Dashboard Analytics**
- **Manual statistics entry**: Admin can enter placement data manually
- **Interactive charts**: Visual representation of placement statistics
- **Real-time updates**: Dynamic dashboard with live data
- **Comprehensive analytics**: Complete placement overview

### **File Management**
- **Image uploads**: Profile pictures and company logos
- **Document handling**: Resume and document uploads
- **Media organization**: Structured file storage system

### **Security Features**
- **Role-based access**: Different permissions for different user types
- **Session management**: Secure login and logout functionality
- **Data protection**: Secure handling of sensitive information

## 📁 Project Structure

```
Placement-Management-System/
├── stdplacement/          # Main Django project
├── register/              # User registration app
├── std_app/               # Student app
├── company/               # Company app
├── staff_app/             # Staff app
├── student_import/        # CSV import functionality
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── media/                 # User uploaded files
└── requirements.txt       # Python dependencies
```

## 🌟 Advanced Features

- **CSV Import**: Bulk student registration through CSV files
- **Application Workflow**: Complete hiring process management
- **Status Management**: Multiple application statuses (Accepted, Rejected, Rounds, Placed)
- **Requirement Validation**: Automatic eligibility checking
- **Button Controls**: Admin-controlled application periods
- **Statistics Dashboard**: Manual data entry for analytics
- **Responsive Design**: Mobile-friendly interface
- **Professional UI**: Modern, clean design with gradients

## 📝 Usage Guide

### **For Students:**
1. Register and complete profile
2. Fill academic and personal details
3. Browse available job openings
4. Apply for up to 3 positions
5. Track application status

### **For Companies:**
1. Register company profile
2. Post job openings with requirements
3. Review student applications
4. Update application status
5. Manage hiring process

### **For Admin/Staff:**
1. Manage all user accounts
2. Control application periods
3. Enter placement statistics
4. Monitor system activities
5. Import student data via CSV

## 🔧 Configuration

The application is configured for both development and production environments. Key settings are managed through environment variables:

- `DEBUG`: Set to False in production
- `SECRET_KEY`: Use environment variable in production
- `ALLOWED_HOSTS`: Configured for Render deployment

