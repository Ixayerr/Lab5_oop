import tkinter as tk
from tkinter import messagebox


class MeanCalculatorApp(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=1)
        self.create_widgets()

    def create_widgets(self):
        """Створення віджетів."""
        # Labels and Entry for input values
        tk.Label(self, text="Enter A:").grid(row=0, column=0)
        self.a_entry = tk.Entry(self)
        self.a_entry.grid(row=0, column=1)

        tk.Label(self, text="Enter B:").grid(row=1, column=0)
        self.b_entry = tk.Entry(self)
        self.b_entry.grid(row=1, column=1)

        tk.Label(self, text="Enter C:").grid(row=2, column=0)
        self.c_entry = tk.Entry(self)
        self.c_entry.grid(row=2, column=1)

        tk.Label(self, text="Enter D:").grid(row=3, column=0)
        self.d_entry = tk.Entry(self)
        self.d_entry.grid(row=3, column=1)

        # Calculate button
        self.calc_button = tk.Button(self, text="Calculate", command=self.calculate_means)
        self.calc_button.grid(row=4, column=0, columnspan=2)

        # Output Labels
        self.output_label = tk.Label(self, text="")
        self.output_label.grid(row=5, column=0, columnspan=2)

    def mean(self, x, y):
        """Обчислення середнього арифметичного та геометричного."""
        arithmetic_mean = (x + y) / 2
        geometric_mean = (x * y) ** 0.5
        return arithmetic_mean, geometric_mean

    def calculate_means(self):
        """Зчитування даних"""
        try:
            A = float(self.a_entry.get())
            B = float(self.b_entry.get())
            C = float(self.c_entry.get())
            D = float(self.d_entry.get())

            # Calculate for pairs: (A, B), (A, C), (A, D)
            results = [
                self.mean(A, B),
                self.mean(A, C),
                self.mean(A, D)
            ]

            # Display results
            output_text = (
                f"(A, B): Arithmetic = {results[0][0]:.2f}, Geometric = {results[0][1]:.2f}\n"
                f"(A, C): Arithmetic = {results[1][0]:.2f}, Geometric = {results[1][1]:.2f}\n"
                f"(A, D): Arithmetic = {results[2][0]:.2f}, Geometric = {results[2][1]:.2f}"
            )
            self.output_label.config(text=output_text)
        except ValueError:
            messagebox.showerror("Помилка", "Введіть дійсні числа!")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mean Calculator")
    app = MeanCalculatorApp(root)
    root.mainloop()
