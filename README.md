# 🕐 Digital Clock

A clean and responsive digital clock web application that displays the current time and date in real time.

## 📸 Preview

```
  ┌─────────────────────────────┐
  │                             │
  │      12 : 45 : 30  PM       │
  │   Thursday, March 12, 2026  │
  │                             │
  └─────────────────────────────┘
```

## ✨ Features

- Real-time clock that updates every second
- Displays hours, minutes, and seconds
- AM/PM format (12-hour) or 24-hour format toggle
- Shows current day, date, and month
- Responsive design — works on desktop and mobile
- Clean, minimal UI

## 🛠️ Tech Stack

- **HTML5** — Structure
- **CSS3** — Styling and animations
- **JavaScript (Vanilla)** — Clock logic using `Date` object and `setInterval`

## 📁 Project Structure

```
digital-clock/
├── index.html       # Main HTML file
├── style.css        # Styles and layout
├── script.js        # Clock logic
└── README.md        # Project documentation
```

## 🚀 Getting Started

### Prerequisites

No dependencies or installations required. Just a modern web browser.

### Running the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/digital-clock.git
   ```

2. **Navigate to the project folder**
   ```bash
   cd digital-clock
   ```

3. **Open in browser**
   ```bash
   open index.html
   ```
   Or simply double-click `index.html` to open it in your default browser.

## 🧠 How It Works

The clock uses JavaScript's built-in `Date` object to retrieve the current time:

```javascript
function updateClock() {
  const now = new Date();
  const hours = now.getHours();
  const minutes = now.getMinutes();
  const seconds = now.getSeconds();
  // Update DOM elements with formatted values
}

setInterval(updateClock, 1000); // Refresh every second
```

`setInterval` calls `updateClock()` every 1000 milliseconds (1 second) to keep the display in sync.

## 🎨 Customization

You can customize the clock by editing `style.css`:

| Property        | What to Change                   |
|-----------------|----------------------------------|
| Font family     | Change the clock typeface        |
| Background color| Adjust the page/card background  |
| Text color      | Change digit color               |
| Font size       | Make the clock larger or smaller |

## 📱 Responsive Design

The layout adapts to different screen sizes using CSS media queries, ensuring the clock looks great on phones, tablets, and desktops.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork this repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

**Your Name**  
GitHub:o https://github.com/Akshay0078-eng/Digital_clock.git

---

> Made with ❤️
