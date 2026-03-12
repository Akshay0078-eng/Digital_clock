import tkinter as tk
from tkinter import font as tkfont
from datetime import datetime
import math

# ─── THEMES ───────────────────────────────────────────────────────────────────
THEMES = {
    "Retro": {
        "bg":           "#1a0a00",
        "clock_bg":     "#0d0500",
        "fg":           "#ff6a00",
        "accent":       "#ff9500",
        "dim":          "#7a3200",
        "date_fg":      "#cc5500",
        "seconds_fg":   "#ff9500",
        "border":       "#ff6a00",
        "shadow":       "#7a3200",
        "label_fg":     "#cc5500",
        "font_time":    ("Courier", 80, "bold"),
        "font_date":    ("Courier", 18, "bold"),
        "font_label":   ("Courier", 11),
        "scanlines":    True,
        "glow":         "#ff6a0040",
        "dot_char":     "◆",
    },
    "Modern": {
        "bg":           "#f0f4f8",
        "clock_bg":     "#ffffff",
        "fg":           "#1a1a2e",
        "accent":       "#4361ee",
        "dim":          "#a0aec0",
        "date_fg":      "#4361ee",
        "seconds_fg":   "#4361ee",
        "border":       "#e2e8f0",
        "shadow":       "#cbd5e0",
        "label_fg":     "#718096",
        "font_time":    ("Helvetica", 80, "bold"),
        "font_date":    ("Helvetica", 18),
        "font_label":   ("Helvetica", 11),
        "scanlines":    False,
        "glow":         "#4361ee20",
        "dot_char":     "•",
    },
    "Dark Mode": {
        "bg":           "#0f0f0f",
        "clock_bg":     "#1a1a1a",
        "fg":           "#e2e8f0",
        "accent":       "#7c3aed",
        "dim":          "#4a4a4a",
        "date_fg":      "#a78bfa",
        "seconds_fg":   "#7c3aed",
        "border":       "#2d2d2d",
        "shadow":       "#000000",
        "label_fg":     "#6b7280",
        "font_time":    ("Helvetica", 80, "bold"),
        "font_date":    ("Helvetica", 18),
        "font_label":   ("Helvetica", 11),
        "scanlines":    False,
        "glow":         "#7c3aed30",
        "dot_char":     "●",
    },
    "Neon": {
        "bg":           "#020014",
        "clock_bg":     "#050020",
        "fg":           "#00ffff",
        "accent":       "#ff00ff",
        "dim":          "#003333",
        "date_fg":      "#ff00ff",
        "seconds_fg":   "#00ff88",
        "border":       "#00ffff",
        "shadow":       "#003333",
        "label_fg":     "#00aaaa",
        "font_time":    ("Courier", 80, "bold"),
        "font_date":    ("Courier", 18, "bold"),
        "font_label":   ("Courier", 11),
        "scanlines":    True,
        "glow":         "#00ffff40",
        "dot_char":     "★",
    },
    "Minimal": {
        "bg":           "#fafafa",
        "clock_bg":     "#fafafa",
        "fg":           "#222222",
        "accent":       "#222222",
        "dim":          "#cccccc",
        "date_fg":      "#888888",
        "seconds_fg":   "#cccccc",
        "border":       "#eeeeee",
        "shadow":       "#eeeeee",
        "label_fg":     "#aaaaaa",
        "font_time":    ("Georgia", 80, "bold"),
        "font_date":    ("Georgia", 18),
        "font_label":   ("Georgia", 11),
        "scanlines":    False,
        "glow":         "#22222210",
        "dot_char":     "·",
    },
}

DAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]


class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.resizable(False, False)
        self.current_theme_name = "Retro"
        self.theme = THEMES[self.current_theme_name]
        self._build_ui()
        self._apply_theme()
        self._tick()

    # ── BUILD ──────────────────────────────────────────────────────────────────
    def _build_ui(self):
        # Outer frame
        self.outer = tk.Frame(self, padx=30, pady=20)
        self.outer.pack(fill="both", expand=True)

        # Title bar
        title_bar = tk.Frame(self.outer)
        title_bar.pack(fill="x", pady=(0, 12))

        self.title_label = tk.Label(title_bar, text="⏰  DIGITAL CLOCK", font=("Courier", 12, "bold"), anchor="w")
        self.title_label.pack(side="left")

        # Theme buttons
        self.theme_frame = tk.Frame(title_bar)
        self.theme_frame.pack(side="right")

        self.theme_buttons = {}
        for name in THEMES:
            btn = tk.Button(
                self.theme_frame,
                text=name,
                width=8,
                relief="flat",
                cursor="hand2",
                bd=0,
                padx=8,
                pady=4,
                command=lambda n=name: self._set_theme(n),
            )
            btn.pack(side="left", padx=3)
            self.theme_buttons[name] = btn

        # Clock card
        self.card = tk.Frame(self.outer, relief="flat", bd=2, padx=40, pady=30)
        self.card.pack(fill="both", expand=True)

        # Time display  HH : MM
        time_row = tk.Frame(self.card)
        time_row.pack()

        self.hours_label = tk.Label(time_row, text="00", width=3, anchor="e")
        self.hours_label.pack(side="left")

        self.colon1 = tk.Label(time_row, text=":")
        self.colon1.pack(side="left", padx=2)

        self.minutes_label = tk.Label(time_row, text="00", width=3, anchor="w")
        self.minutes_label.pack(side="left")

        # Seconds
        self.seconds_label = tk.Label(self.card, text=": 00")
        self.seconds_label.pack()

        # Divider
        self.divider = tk.Frame(self.card, height=2)
        self.divider.pack(fill="x", padx=20, pady=12)

        # Date row
        self.date_label = tk.Label(self.card, text="")
        self.date_label.pack()

        # AM/PM + day indicator row
        self.ampm_label = tk.Label(self.card, text="")
        self.ampm_label.pack(pady=(6, 0))

        # Progress bar for seconds
        self.progress_canvas = tk.Canvas(self.card, height=6, highlightthickness=0)
        self.progress_canvas.pack(fill="x", padx=20, pady=(14, 0))

        # Status bar
        self.status = tk.Label(self.outer, text="", anchor="center", pady=6)
        self.status.pack(fill="x", pady=(10, 0))

    # ── THEME ──────────────────────────────────────────────────────────────────
    def _apply_theme(self):
        t = self.theme
        self.configure(bg=t["bg"])
        self.outer.configure(bg=t["bg"])

        # Title
        self.title_label.configure(bg=t["bg"], fg=t["dim"], font=t["font_label"])

        # Theme buttons
        for name, btn in self.theme_buttons.items():
            if name == self.current_theme_name:
                btn.configure(bg=t["accent"], fg=t["bg"],
                              font=(t["font_label"][0], 9, "bold"))
            else:
                btn.configure(bg=t["border"], fg=t["dim"],
                              font=(t["font_label"][0], 9))

        self.card.configure(bg=t["clock_bg"], highlightbackground=t["border"],
                            highlightthickness=2)

        self.hours_label.configure(bg=t["clock_bg"], fg=t["fg"],
                                   font=t["font_time"])
        self.colon1.configure(bg=t["clock_bg"], fg=t["accent"],
                              font=t["font_time"])
        self.minutes_label.configure(bg=t["clock_bg"], fg=t["fg"],
                                     font=t["font_time"])
        self.seconds_label.configure(bg=t["clock_bg"], fg=t["seconds_fg"],
                                     font=(t["font_date"][0], 24, "bold"))
        self.divider.configure(bg=t["border"])
        self.date_label.configure(bg=t["clock_bg"], fg=t["date_fg"],
                                  font=t["font_date"])
        self.ampm_label.configure(bg=t["clock_bg"], fg=t["label_fg"],
                                  font=t["font_label"])
        self.progress_canvas.configure(bg=t["clock_bg"])
        self.status.configure(bg=t["bg"], fg=t["dim"], font=t["font_label"])

        # Rebuild all card child frames
        for w in self.card.winfo_children():
            if isinstance(w, tk.Frame):
                w.configure(bg=t["clock_bg"])

    def _set_theme(self, name):
        self.current_theme_name = name
        self.theme = THEMES[name]
        self._apply_theme()
        self._update_progress(datetime.now().second)

    # ── TICK ───────────────────────────────────────────────────────────────────
    def _tick(self):
        now = datetime.now()
        h = now.hour
        m = now.minute
        s = now.second
        ampm = "AM" if h < 12 else "PM"
        h12 = h % 12 or 12

        # Blink colon
        colon_char = ":" if s % 2 == 0 else " "
        self.colon1.configure(text=colon_char)

        self.hours_label.configure(text=f"{h12:02d}")
        self.minutes_label.configure(text=f"{m:02d}")
        self.seconds_label.configure(text=f"  {self.theme['dot_char']} {s:02d}s")

        day_name = DAYS[now.weekday()]
        month_name = MONTHS[now.month - 1]
        self.date_label.configure(
            text=f"{day_name}, {month_name} {now.day}, {now.year}"
        )
        self.ampm_label.configure(text=f"{ampm}  ·  {now.strftime('%Z')}  ·  Week {now.isocalendar()[1]}")

        self._update_progress(s)

        self.status.configure(
            text=f"Theme: {self.current_theme_name}   ·   {now.strftime('%H:%M:%S')} (24h)"
        )

        self.after(500, self._tick)

    def _update_progress(self, second):
        t = self.theme
        c = self.progress_canvas
        c.delete("all")
        self.update_idletasks()
        w = c.winfo_width() or 300
        h = 6
        # Background track
        c.create_rectangle(0, 0, w, h, fill=t["border"], outline="")
        # Fill
        filled = int((second / 60) * w)
        if filled > 0:
            c.create_rectangle(0, 0, filled, h, fill=t["accent"], outline="")
        # Dot at current position
        if filled > 4:
            c.create_oval(filled - 5, 0, filled + 1, h, fill=t["fg"], outline="")


# ── MAIN ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = DigitalClock()
    # Center on screen
    app.update_idletasks()
    sw = app.winfo_screenwidth()
    sh = app.winfo_screenheight()
    w, h = 700, 420
    app.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")
    app.mainloop()
