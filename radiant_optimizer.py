"""
Radiant Optimizer - Gaming Performance Booster
Simple GUI for Windows Gaming Optimizations
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time
from optimizer_backend import RadiantOptimizer

class RadiantOptimizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Radiant Optimizer - Gaming Performance Booster")
        self.root.geometry("900x700")
        self.root.configure(bg='#0a0e1f')

        # Initialize backend
        self.optimizer = RadiantOptimizer()

        # Setup UI
        self.setup_ui()

        # Start monitoring
        self.monitoring = True
        self.update_system_info()

    def setup_ui(self):
        """Setup the user interface"""

        # Title
        title_frame = tk.Frame(self.root, bg='#0a0e1f')
        title_frame.pack(fill=tk.X, padx=20, pady=20)

        title_label = tk.Label(
            title_frame,
            text="RADIANT OPTIMIZER",
            font=("Segoe UI", 24, "bold"),
            bg='#0a0e1f',
            fg='#4F7CFF'
        )
        title_label.pack()

        subtitle = tk.Label(
            title_frame,
            text="Windows Gaming Performance Booster",
            font=("Segoe UI", 10),
            bg='#0a0e1f',
            fg='#a0a8c5'
        )
        subtitle.pack()

        # System Info Frame
        info_frame = tk.LabelFrame(
            self.root,
            text="System Information",
            font=("Segoe UI", 12, "bold"),
            bg='#1a1f3a',
            fg='#ffffff',
            relief=tk.FLAT,
            padx=15,
            pady=15
        )
        info_frame.pack(fill=tk.BOTH, padx=20, pady=10)

        self.cpu_label = tk.Label(
            info_frame,
            text="CPU: Loading...",
            font=("Segoe UI", 10),
            bg='#1a1f3a',
            fg='#ffffff',
            anchor='w'
        )
        self.cpu_label.pack(fill=tk.X, pady=2)

        self.ram_label = tk.Label(
            info_frame,
            text="RAM: Loading...",
            font=("Segoe UI", 10),
            bg='#1a1f3a',
            fg='#ffffff',
            anchor='w'
        )
        self.ram_label.pack(fill=tk.X, pady=2)

        self.disk_label = tk.Label(
            info_frame,
            text="Disk: Loading...",
            font=("Segoe UI", 10),
            bg='#1a1f3a',
            fg='#ffffff',
            anchor='w'
        )
        self.disk_label.pack(fill=tk.X, pady=2)

        self.gpu_label = tk.Label(
            info_frame,
            text="GPU: Loading...",
            font=("Segoe UI", 10),
            bg='#1a1f3a',
            fg='#ffffff',
            anchor='w'
        )
        self.gpu_label.pack(fill=tk.X, pady=2)

        # Quick Actions Frame
        quick_frame = tk.LabelFrame(
            self.root,
            text="Quick Optimizations",
            font=("Segoe UI", 12, "bold"),
            bg='#1a1f3a',
            fg='#ffffff',
            relief=tk.FLAT,
            padx=15,
            pady=15
        )
        quick_frame.pack(fill=tk.BOTH, padx=20, pady=10)

        # Quick buttons in 2 columns
        buttons_frame = tk.Frame(quick_frame, bg='#1a1f3a')
        buttons_frame.pack(fill=tk.BOTH)

        # Left column
        left_col = tk.Frame(buttons_frame, bg='#1a1f3a')
        left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.create_button(
            left_col,
            "🎮 Apply Gaming Preset",
            self.apply_gaming_preset,
            "#4F7CFF"
        )

        self.create_button(
            left_col,
            "⚡ FPS Boost Preset",
            self.apply_fps_boost,
            "#10b981"
        )

        self.create_button(
            left_col,
            "🎯 Enable Game Mode",
            self.enable_game_mode,
            "#1a1f3a"
        )

        self.create_button(
            left_col,
            "⚙️ High Performance Power",
            self.set_high_performance,
            "#1a1f3a"
        )

        # Right column
        right_col = tk.Frame(buttons_frame, bg='#1a1f3a')
        right_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.create_button(
            right_col,
            "🚫 Disable Game DVR",
            self.disable_game_dvr,
            "#1a1f3a"
        )

        self.create_button(
            right_col,
            "🎨 Disable Visual Effects",
            self.disable_visual_effects,
            "#1a1f3a"
        )

        self.create_button(
            right_col,
            "🗑️ Clean Temp Files",
            self.clean_temp_files,
            "#1a1f3a"
        )

        self.create_button(
            right_col,
            "↩️ Restore All Tweaks",
            self.restore_tweaks,
            "#f59e0b"
        )

        # Output Log Frame
        log_frame = tk.LabelFrame(
            self.root,
            text="Output Log",
            font=("Segoe UI", 12, "bold"),
            bg='#1a1f3a',
            fg='#ffffff',
            relief=tk.FLAT,
            padx=15,
            pady=15
        )
        log_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=10,
            font=("Consolas", 9),
            bg='#0a0e1f',
            fg='#00ff00',
            insertbackground='#00ff00',
            relief=tk.FLAT
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)

        # Footer
        footer = tk.Label(
            self.root,
            text="⚠️ Run as Administrator for full functionality | Some tweaks require system restart",
            font=("Segoe UI", 8),
            bg='#0a0e1f',
            fg='#6b7280'
        )
        footer.pack(pady=10)

        self.log("Radiant Optimizer initialized successfully!")
        self.log("Ready to boost your gaming performance!")

    def create_button(self, parent, text, command, bg_color):
        """Create a styled button"""
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 10),
            bg=bg_color,
            fg='#ffffff',
            activebackground='#6B8FFF',
            activeforeground='#ffffff',
            relief=tk.FLAT,
            cursor='hand2',
            padx=20,
            pady=10
        )
        btn.pack(fill=tk.X, pady=5)
        return btn

    def log(self, message):
        """Add message to log"""
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)

    def update_system_info(self):
        """Update system information display"""
        if not self.monitoring:
            return

        try:
            info = self.optimizer.get_system_info()

            self.cpu_label.config(
                text=f"CPU: {info['cpu']['cores']} Cores / {info['cpu']['threads']} Threads | Usage: {info['cpu']['usage']:.1f}%"
            )

            self.ram_label.config(
                text=f"RAM: {info['memory']['used_gb']:.1f} / {info['memory']['total_gb']:.1f} GB ({info['memory']['percent']:.1f}%)"
            )

            self.disk_label.config(
                text=f"Disk C: {info['disk']['used_gb']:.0f} / {info['disk']['total_gb']:.0f} GB ({info['disk']['percent']:.1f}%)"
            )

            # Update GPU info once
            if "Loading" in self.gpu_label.cget("text"):
                gpu = self.optimizer.get_gpu_info()
                self.gpu_label.config(text=f"GPU: {gpu['name']}")

        except Exception as e:
            self.log(f"Error updating system info: {str(e)}")

        # Schedule next update
        self.root.after(2000, self.update_system_info)

    def run_tweak(self, func, name):
        """Run a tweak in background thread"""
        def worker():
            self.log(f"Applying {name}...")
            try:
                success, msg = func()
                if success:
                    self.log(f"✓ {name}: {msg}")
                    messagebox.showinfo("Success", f"{name} applied successfully!\n\n{msg}")
                else:
                    self.log(f"✗ {name}: {msg}")
                    messagebox.showwarning("Warning", f"{name} failed:\n\n{msg}")
            except Exception as e:
                self.log(f"✗ {name}: Error - {str(e)}")
                messagebox.showerror("Error", f"Failed to apply {name}:\n\n{str(e)}")

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()

    # Tweak Functions
    def apply_gaming_preset(self):
        """Apply all gaming optimizations"""
        self.log("=" * 50)
        self.log("Applying Gaming Preset...")

        def worker():
            results = self.optimizer.apply_gaming_preset()
            for result in results:
                self.log(result)
            self.log("Gaming Preset applied!")
            messagebox.showinfo(
                "Gaming Preset Applied",
                "All gaming optimizations have been applied!\n\n" + "\n".join(results)
            )

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()

    def apply_fps_boost(self):
        """Apply FPS boost preset"""
        self.log("=" * 50)
        self.log("Applying FPS Boost Preset...")

        def worker():
            results = self.optimizer.apply_fps_boost_preset()
            for result in results:
                self.log(result)
            self.log("FPS Boost Preset applied!")
            messagebox.showinfo(
                "FPS Boost Applied",
                "FPS boost optimizations have been applied!\n\n" + "\n".join(results)
            )

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()

    def enable_game_mode(self):
        self.run_tweak(self.optimizer.enable_game_mode, "Game Mode")

    def set_high_performance(self):
        self.run_tweak(self.optimizer.set_high_performance_power_plan, "High Performance Power Plan")

    def disable_game_dvr(self):
        self.run_tweak(self.optimizer.disable_game_dvr, "Disable Game DVR")

    def disable_visual_effects(self):
        self.run_tweak(self.optimizer.disable_visual_effects, "Disable Visual Effects")

    def clean_temp_files(self):
        self.run_tweak(self.optimizer.clean_temp_files, "Clean Temp Files")

    def restore_tweaks(self):
        if messagebox.askyesno("Restore Tweaks", "Are you sure you want to restore all original settings?"):
            self.run_tweak(self.optimizer.restore_all_tweaks, "Restore All Tweaks")

def main():
    root = tk.Tk()
    app = RadiantOptimizerGUI(root)

    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    root.mainloop()

if __name__ == "__main__":
    main()
