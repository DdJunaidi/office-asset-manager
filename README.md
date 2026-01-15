# 🖥️ Home Office Asset Manager

A lightweight, full-stack web application designed to help users track hardware and office equipment. This project focuses on **Zero-Maintenance** and **Portability**.

## 🌟 Key Features
- **Full CRUD Functionality:** Create, Read, Update, and Delete office assets.
- **Inventory Tracking:** Manage quantities and equipment status (In Use, Storage, Broken).
- **Portable Database:** Uses SQLite, requiring no complex server setup or costs.
- **Responsive UI:** Built with Bootstrap 5 for a clean, professional look.

## 🛠️ Tech Stack
- **Backend:** Python 3 + Flask Framework
- **Database:** SQLite (Relational)
- **Frontend:** HTML5 + Bootstrap 5

## 🚀 Quick Start for Recruiters
1. **Clone the project:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/office-asset-manager.git](https://github.com/YOUR_USERNAME/office-asset-manager.git)
   cd office-asset-manager

   ---

## 📈 Development Log & Lessons Learned

Every software project has its hurdles. Below are the technical challenges I faced during the creation of this Asset Manager and how I solved them:

### 1. Environment & Path Issues
- **Challenge:** On my Windows environment, the standard `python` command was not recognized, leading to "command not found" errors.
- **Solution:** I identified that the Python Launcher (`py`) was the active alias on my machine. I adjusted my workflow to use `py -m pip` and `py app.py`, ensuring consistent execution.

### 2. Git & File System Ownership
- **Challenge:** Encountered a `dubious ownership` error when initializing Git on a secondary drive partition (G:).
- **Solution:** I used `git config --global --add safe.directory` with double quotes to handle the spaces in the directory path, allowing Git to safely track the project files.

### 3. Database Schema Evolution
- **Challenge:** I needed to add a `quantity` column after the database was already created.
- **Solution:** I implemented a robust `init_db()` function in Flask that ensures the table structure is created automatically on the first run. I learned the importance of "dropping" a local SQLite database when making structural changes during development.

---