import tkinter as tk
from tkinter import messagebox, filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class RecurrenceApp(tk.Frame):
    """GUI додаток для побудови графіка рекурентного виразу."""

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=1)
        self.create_widgets()

    def create_widgets(self):
        """Створення віджетів."""
        # Buttons
        self.save_button = tk.Button(self, text="Save Data to File", command=self.save_data)
        self.save_button.pack()

        self.plot_button = tk.Button(self, text="Show Plot", command=self.show_plot)
        self.plot_button.pack()

        # Canvas for graph
        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(fill=tk.BOTH, expand=1)

    def calculate_recurrence(self, n=100, T0=0.3, K=2.5, U=2):
        """Обчислення значень y за рекурентним виразом."""
        y = [0]
        for k in range(n):
            y_next = (1 - T0 / 0.3) * y[k] + (T0 / 0.3) * K * U
            y.append(y_next)
        return [k * T0 for k in range(n + 1)], y

    def save_data(self):
        """Збереження даних у файл."""
        t, y = self.calculate_recurrence()
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file:
            for i in range(len(t)):
                file.write(f"{t[i]:.5f};{y[i]:.5f}\n")
            file.close()
            messagebox.showinfo("успіх", "Дані збережено!")

    def show_plot(self):
        """Побудова графіка."""
        t, y = self.calculate_recurrence()

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(t, y, label="y(t)")
        ax.set_title("Рекурентний графік")
        ax.set_xlabel("Time (t)")
        ax.set_ylabel("y(t)")
        ax.grid(True)
        ax.legend()

        # Embed plot into Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        canvas.draw()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Recurrence Plotter")
    app = RecurrenceApp(root)
    root.mainloop()
