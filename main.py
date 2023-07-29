import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from itertools import product
import noise_gen as ng
import body_gen as bg


class PlanetGeneratorApp:
    def __init__(self, input_root):
        self.output_image = None
        self.tk_image = None
        self.save_button = None
        self.generate_button = None
        self.temperature_scale = None
        self.resolution_scale = None
        self.right_frame = None
        self.canvas = None

        self.root = input_root
        self.root.title("Planet Generator")
        self.root.iconbitmap("resources/icon.ico")
        self.root.configure(bg="#333333")
        self.root.option_add("*Font", "Arial 10")

        custom_button_style = {
            "background": "#666666",
            "foreground": "#FFFFFF",
            "activebackground": "#888888",
            "activeforeground": "#FFFFFF",
            "bd": 0,
        }
        self.root.option_add("*TButton", custom_button_style)

        self.background_image = Image.open("resources/space_background.png")
        self.background_image = self.background_image.resize((1024, 1024), Image.LANCZOS)
        self.background_tk_image = ImageTk.PhotoImage(self.background_image)

        self.resolution = 1024
        self.avg_temperature = 15
        self.star_type = tk.StringVar()
        self.star_type.set("g")

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.resolution, height=self.resolution)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_tk_image)
        self.canvas.pack(side=tk.LEFT)

        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, padx=10)

        tk.Label(self.right_frame, text="Resolution:").pack()
        self.resolution_scale = tk.Scale(self.right_frame, from_=128, to=1024, orient=tk.HORIZONTAL)
        self.resolution_scale.set(self.resolution)
        self.resolution_scale.pack()

        tk.Label(self.right_frame, text="Average Temperature:").pack()
        self.temperature_scale = tk.Scale(self.right_frame, from_=-50, to=50, orient=tk.HORIZONTAL)
        self.temperature_scale.set(self.avg_temperature)
        self.temperature_scale.pack()

        tk.Label(self.right_frame, text="Star Type:").pack()
        star_types = [("M", "m"), ("K", "k"), ("G", "g")]
        for star_type, value in star_types:
            tk.Radiobutton(self.right_frame, text=star_type, variable=self.star_type, value=value).pack(anchor=tk.W)

        self.generate_button = tk.Button(self.right_frame, text="Generate Planet", command=self.generate_planet)
        self.generate_button.pack(pady=10)

        self.save_button = tk.Button(self.right_frame, text="Save Planet", command=self.save_planet)
        self.save_button.pack()

    def generate_planet(self):
        self.resolution = self.resolution_scale.get()
        self.avg_temperature = self.temperature_scale.get()

        water_normalized_noise, land_normalized_noise = ng.NoiseGen.generate_noise(self.resolution,
                                                                                   self.avg_temperature)
        clouds_noise_map = ng.NoiseGen.generate_clouds_noise(self.resolution)
        water_map, land_map = bg.BodyGen.generate_colors(self.avg_temperature, self.star_type.get())
        cloud_map = bg.BodyGen.generate_clouds()

        land_image = Image.new("RGBA", (self.resolution, self.resolution))
        clouds_image = Image.new("RGBA", (self.resolution, self.resolution))
        water_image = Image.new("RGBA", (self.resolution, self.resolution))

        land_array = land_image.load()
        clouds_array = clouds_image.load()
        water_array = water_image.load()

        for y, x in product(range(self.resolution), repeat=2):
            planet_noise_value = land_normalized_noise[y, x]
            land_array[x, y] = self.find_color(planet_noise_value, land_map)

            cloud_noise_value = clouds_noise_map[y, x]
            clouds_array[x, y] = self.find_color(cloud_noise_value, cloud_map)

            water_noise_value = water_normalized_noise[y, x]
            water_array[x, y] = self.find_color(water_noise_value, water_map)

        shadow_image = Image.open("./resources/shadow.png").resize((self.resolution, self.resolution), Image.LANCZOS)
        self.output_image = Image.alpha_composite(water_image, land_image)
        self.output_image = Image.alpha_composite(self.output_image, clouds_image)
        self.output_image = Image.alpha_composite(self.output_image, shadow_image)

        self.display_image(self.output_image)

    @staticmethod
    def find_color(noise_value, color_map):
        for (lower, upper), color in color_map.items():
            if lower <= noise_value <= upper:
                return color
        return 0, 0, 0, 0

    def display_image(self, image):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        x_center = (canvas_width - self.resolution) / 2
        y_center = (canvas_height - self.resolution) / 2

        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(x_center, y_center, anchor=tk.NW, image=self.tk_image)

    def save_planet(self):
        if self.tk_image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if file_path:
                self.output_image.save(file_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = PlanetGeneratorApp(root)
    root.mainloop()
