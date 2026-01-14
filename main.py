# ============================================================
# MULTI FUNCTION CLOCK
# A Multifunction Digital Clock Application
# ============================================================
# 
# Add your clock code here!
# 
# Suggested features:
# - Digital clock display
# - Multiple time zones
# - Alarm functionality
# - Stopwatch
# - Timer/Countdown
# - Date display
# - Theme customization
#
# ============================================================

def main():
    """Main entry point for the Multi Function Clock application."""
    print("🕐 Multi Function Clock - Starting...")
    # Your code goes here!
    pass


if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import font as tkfont
from datetime import datetime
import math
import winsound
import threading

class BambangSplitFlapClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Bambang Split-Flap Display Clock")
        self.root.configure(bg='#1a1a1a')
        
        # State variables
        self.mode = 'clock'
        self.running = False
        self.stopwatch_time = 0
        self.timer_time = 300000
        self.alarm_enabled = False
        self.prev_values = ['0'] * 8
        self.timer_settings = {'hours': 0, 'minutes': 5, 'seconds': 0}
        
        # Create main frame
        main_frame = tk.Frame(root, bg='#2d2d2d', padx=40, pady=40)
        main_frame.pack(padx=20, pady=20, expand=True, fill='both')
        
        # Title
        title = tk.Label(main_frame, text="BAMBANG SPLIT FLAP CLOCK", 
                        font=('Arial', 24, 'bold'), 
                        bg='#2d2d2d', fg='#00ff41')
        title.pack(pady=(0, 20))
        
        # Settings section (Alarm + Timer Settings)
        settings_frame = tk.Frame(main_frame, bg='#2d2d2d')
        settings_frame.pack(pady=(0, 20))
        
        # Alarm switch
        alarm_frame = tk.Frame(settings_frame, bg='#2d2d2d')
        alarm_frame.pack(side='left', padx=20)
        
        self.alarm_switch = tk.Canvas(alarm_frame, width=80, height=120, 
                                     bg='#4a5563', highlightthickness=2, 
                                     highlightbackground='#374151')
        self.alarm_switch.pack()
        
        self.alarm_indicator = self.alarm_switch.create_oval(30, 15, 50, 35, fill='#666666')
        self.alarm_toggle = self.alarm_switch.create_rectangle(15, 25, 65, 65, 
                                                               fill='#8b7355', outline='#2d1f13')
        self.alarm_switch.bind('<Button-1>', lambda e: self.toggle_alarm())
        
        tk.Label(alarm_frame, text="ALARM", font=('Arial', 10, 'bold'),
                bg='#2d2d2d', fg='#9ca3af').pack(pady=(5, 0))
        
        # Timer settings
        timer_frame = tk.Frame(settings_frame, bg='#1a1a1a', padx=15, pady=15)
        timer_frame.pack(side='left', padx=20)
        
        for i, (label, key) in enumerate([('HOURS', 'hours'), ('MINUTES', 'minutes'), ('SECONDS', 'seconds')]):
            row = tk.Frame(timer_frame, bg='#1a1a1a')
            row.pack(pady=5)
            
            tk.Label(row, text=f"{label}:", font=('Arial', 10, 'bold'),
                    bg='#1a1a1a', fg='#9ca3af').pack(side='left', padx=5)
            
            value_label = tk.Label(row, text='05' if key == 'minutes' else '00',
                                  font=('Arial', 16, 'bold'),
                                  bg='#1a1a1a', fg='#00ff41', width=3)
            value_label.pack(side='left', padx=5)
            setattr(self, f'timer_{key}_label', value_label)
            
            knob = tk.Canvas(row, width=50, height=50, bg='#4a5563', 
                           highlightthickness=2, highlightbackground='#374151')
            knob.pack(side='left', padx=5)
            knob.create_oval(15, 15, 35, 35, fill='#1f2937', outline='#374151')
            knob.create_line(25, 10, 25, 20, fill='#9ca3af', width=3)
            
            knob.bind('<Button-1>', lambda e, k=key: self.start_rotate(k, e))
            knob.bind('<B1-Motion>', lambda e, k=key: self.handle_rotate(k, e))
        
        # Clock display
        clock_frame = tk.Frame(main_frame, bg='#0a0a0a', padx=30, pady=30)
        clock_frame.pack()
        
        display_frame = tk.Frame(clock_frame, bg='#0a0a0a')
        display_frame.pack()
        
        self.digits = []
        positions = [0, 1, 3, 4, 6, 7, 9, 10]
        
        for i, pos in enumerate(positions):
            digit_frame = tk.Frame(display_frame, bg='#1a1a1a', 
                                  width=80, height=120,
                                  highlightbackground='#333333',
                                  highlightthickness=2)
            digit_frame.grid(row=0, column=pos, padx=3, pady=5)
            digit_frame.grid_propagate(False)
            
            digit_label = tk.Label(digit_frame, text="0", 
                                  font=('Courier', 60, 'bold'),
                                  bg='#1a1a1a', fg='#ffffff')
            digit_label.place(relx=0.5, rely=0.5, anchor='center')
            
            line = tk.Frame(digit_frame, bg='#000000', height=2)
            line.place(relx=0, rely=0.5, relwidth=1)
            
            self.digits.append(digit_label)
            
            # Add separators
            if pos in [1, 4, 7]:
                sep_frame = tk.Frame(display_frame, bg='#0a0a0a')
                sep_frame.grid(row=0, column=pos+1, padx=5)
                
                tk.Label(sep_frame, text="●", font=('Arial', 20),
                        bg='#0a0a0a', fg='#ffa500').pack(pady=(30, 10))
                tk.Label(sep_frame, text="●", font=('Arial', 20),
                        bg='#0a0a0a', fg='#ffa500').pack(pady=(10, 30))
        
        # Labels
        tk.Label(clock_frame, text="HOURS  :  MINUTES  :  SECONDS  :  CENTISECONDS",
                font=('Courier', 10), bg='#0a0a0a', fg='#666666').pack(pady=(10, 0))
        
        # Date display
        self.date_label = tk.Label(main_frame, text="", 
                                   font=('Arial', 18, 'bold'),
                                   bg='#2d2d2d', fg='#00ff41')
        self.date_label.pack(pady=(20, 0))
        
        # Control buttons
        controls_frame = tk.Frame(main_frame, bg='#2d2d2d')
        controls_frame.pack(pady=(30, 0))
        
        self.buttons = {}
        button_configs = [
            ('clock', 'CLOCK'),
            ('timer', 'TIMER'),
            ('stopwatch', 'STOPWATCH'),
            ('startstop', 'START/STOP'),
            ('reset', 'RESET')
        ]
        
        for i, (key, label) in enumerate(button_configs):
            btn_frame = tk.Frame(controls_frame, bg='#2d2d2d')
            btn_frame.grid(row=0, column=i, padx=10)
            
            canvas = tk.Canvas(btn_frame, width=90, height=90, 
                             bg='#2d2d2d', highlightthickness=0)
            canvas.pack()
            
            # Draw knob
            canvas.create_oval(5, 5, 85, 85, fill='#4a5563', outline='#374151', width=4)
            canvas.create_oval(30, 30, 60, 60, fill='#1f2937', outline='#374151', width=2)
            canvas.create_rectangle(42, 10, 48, 25, fill='#9ca3af', outline='')
            
            canvas.bind('<Button-1>', lambda e, k=key: self.button_click(k))
            self.buttons[key] = canvas
            
            tk.Label(btn_frame, text=label, font=('Arial', 9, 'bold'),
                    bg='#2d2d2d', fg='#9ca3af').pack(pady=(5, 0))
        
        # Mode indicator
        self.mode_label = tk.Label(main_frame, text="MODE: CLOCK",
                                   font=('Arial', 12, 'bold'),
                                   bg='#2d2d2d', fg='#00ff41')
        self.mode_label.pack(pady=(20, 0))
        
        # Start clock
        self.set_mode('clock')
        self.update_clock()
    
    def toggle_alarm(self):
        self.alarm_enabled = not self.alarm_enabled
        if self.alarm_enabled:
            self.alarm_switch.itemconfig(self.alarm_toggle, fill='#ff4444')
            self.alarm_switch.coords(self.alarm_toggle, 15, 65, 65, 105)
            self.alarm_switch.itemconfig(self.alarm_indicator, fill='#ff0000')
        else:
            self.alarm_switch.itemconfig(self.alarm_toggle, fill='#8b7355')
            self.alarm_switch.coords(self.alarm_toggle, 15, 25, 65, 65)
            self.alarm_switch.itemconfig(self.alarm_indicator, fill='#666666')
    
    def start_rotate(self, key, event):
        self.rotate_start = event.y
        self.rotate_key = key
        self.rotate_start_value = self.timer_settings[key]
    
    def handle_rotate(self, key, event):
        if hasattr(self, 'rotate_start'):
            delta = self.rotate_start - event.y
            change = delta // 10
            max_val = 23 if key == 'hours' else 59
            new_value = max(0, min(max_val, self.rotate_start_value + change))
            
            self.timer_settings[key] = new_value
            label = getattr(self, f'timer_{key}_label')
            label.config(text=f"{new_value:02d}")
            
            self.timer_time = (self.timer_settings['hours'] * 3600000 + 
                             self.timer_settings['minutes'] * 60000 + 
                             self.timer_settings['seconds'] * 1000)
            
            if not self.running and self.mode == 'timer':
                self.update_timer_display()
    
    def button_click(self, key):
        if key == 'clock':
            self.set_mode('clock')
        elif key == 'timer':
            self.set_mode('timer')
        elif key == 'stopwatch':
            self.set_mode('stopwatch')
        elif key == 'startstop':
            self.start_stop()
        elif key == 'reset':
            self.reset_display()
    
    def set_mode(self, new_mode):
        self.mode = new_mode
        self.running = False
        
        self.mode_label.config(text=f"MODE: {new_mode.upper()}")
        
        if new_mode == 'clock':
            pass
        elif new_mode == 'timer':
            self.timer_time = (self.timer_settings['hours'] * 3600000 + 
                             self.timer_settings['minutes'] * 60000 + 
                             self.timer_settings['seconds'] * 1000)
            self.update_timer_display()
        elif new_mode == 'stopwatch':
            self.stopwatch_time = 0
            self.update_stopwatch_display()
    
    def start_stop(self):
        if self.mode == 'clock':
            return
        self.running = not self.running
    
    def reset_display(self):
        self.running = False
        if self.mode == 'stopwatch':
            self.stopwatch_time = 0
            self.update_stopwatch_display()
        elif self.mode == 'timer':
            self.timer_time = (self.timer_settings['hours'] * 3600000 + 
                             self.timer_settings['minutes'] * 60000 + 
                             self.timer_settings['seconds'] * 1000)
            self.update_timer_display()
    
    def play_sonar(self):
        if not self.alarm_enabled:
            return
        
        def beep_thread():
            for i in range(10):
                try:
                    winsound.Beep(800, 500)
                except:
                    print("BEEP!")
                if i < 9:
                    threading.Event().wait(0.6)
        
        thread = threading.Thread(target=beep_thread, daemon=True)
        thread.start()
    
    def update_digit(self, index, value):
        if self.prev_values[index] != value:
            self.digits[index].config(text=value)
            self.prev_values[index] = value
    
    def pad(self, num):
        return f"{num:02d}"
    
    def update_stopwatch_display(self):
        total_cs = self.stopwatch_time // 10
        hours = total_cs // 360000
        minutes = (total_cs % 360000) // 6000
        seconds = (total_cs % 6000) // 100
        centiseconds = total_cs % 100
        
        h = self.pad(hours)
        m = self.pad(minutes)
        s = self.pad(seconds)
        c = self.pad(centiseconds)
        
        time_str = h + m + s + c
        for i, digit in enumerate(time_str):
            self.update_digit(i, digit)
    
    def update_timer_display(self):
        total_cs = self.timer_time // 10
        hours = total_cs // 360000
        minutes = (total_cs % 360000) // 6000
        seconds = (total_cs % 6000) // 100
        centiseconds = total_cs % 100
        
        h = self.pad(hours)
        m = self.pad(minutes)
        s = self.pad(seconds)
        c = self.pad(centiseconds)
        
        time_str = h + m + s + c
        for i, digit in enumerate(time_str):
            self.update_digit(i, digit)
    
    def update_clock(self):
        if self.mode == 'clock':
            now = datetime.now()
            hours = self.pad(now.hour)
            minutes = self.pad(now.minute)
            seconds = self.pad(now.second)
            centiseconds = self.pad(now.microsecond // 10000)
            
            time_str = hours + minutes + seconds + centiseconds
            for i, digit in enumerate(time_str):
                self.update_digit(i, digit)
            
            days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
            months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
            
            day_name = days[now.weekday()]
            date = self.pad(now.day)
            month = months[now.month - 1]
            year = now.year
            
            self.date_label.config(text=f"{day_name} {date}-{month}-{year}")
        
        elif self.mode == 'stopwatch' and self.running:
            self.stopwatch_time += 10
            self.update_stopwatch_display()
        
        elif self.mode == 'timer' and self.running:
            self.timer_time -= 10
            if self.timer_time <= 0:
                self.timer_time = 0
                self.running = False
                self.update_timer_display()
                self.play_sonar()
            else:
                self.update_timer_display()
        
        self.root.after(10, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = BambangSplitFlapClock(root)
    root.mainloop()