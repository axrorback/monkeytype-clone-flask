**README.md**

# Monkeytype Clone (Typing Speed Test App)

A fully functional web application inspired by [Monkeytype](https://monkeytype.com/) built with **Flask**, **JavaScript**, **Bootstrap 5**, and **Plotly**. This app allows users to test their typing speed, accuracy, and provides visual results after completion.

## 🚀 Features

- 🧠 Difficulty Levels: Easy, Medium, Hard
- 🎯 Accuracy, WPM, Mistake count, and Keystroke tracking
- ⏱️ Countdown Timer and Live Progress
- 📊 Result visualization using Plotly.js
- 💾 Autosave & Share Results
- 🖼️ Screenshot export with branding and timestamp
- 📱 Responsive UI with Bootstrap 5 & CSS3 animations

## 📁 Project Structure

```
monkeytype-app/
├── static/
│   ├── css/
│   ├── js/
│   └── exports/           # Screenshots or saved images
├── templates/
│   ├── index.html
│
├── app.py
├── utils.py              # Python code execution and result handling
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔧 Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/axrorback/monkeytype-clone-flask.git
cd monkeytype-clone-flask
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the app:**

```bash
python app.py
```

5. **Visit the app:**

Open your browser and navigate to `http://localhost:5000`

## 🛠 Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML5, Bootstrap 5, JavaScript
- **Charting:** Plotly.js
- **Screenshot Export:** HTML2Canvas (if used)

## 📸 Screenshot Feature

Every result page includes a button to export the result section as a styled image with:
- Current Date & Time
- Header: "Acharya University Digital Code Lab"
- Footer: "Powered by Ahrorjon"

## 📬 Contact

**Developer:** Ahrorjon  
📧 Email: axrorback@gmail.com  
📲 Telegram: [@axrorback](https://t.me/axrorback)

---

> Built with ❤️ using Flask + JS + Plotly for fast & fun typing practice!
