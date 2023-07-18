from PIL import Image
import noise_gen as ng
import body_gen as bg

# 80 <= res <= 1024
"""
7400 - 80
"""
resolution = 1000

avg_temperature = 15
planet_normalized_noise = ng.NoiseGen.generate_noise(resolution, avg_temperature)
cloud_normalized_noise = ng.NoiseGen.generate_noise(resolution, avg_temperature)
color_map = bg.BodyGen.generate_colors(avg_temperature)
cloud_map = bg.BodyGen.generate_clouds()

planet_image = Image.new("RGBA", (resolution, resolution))
planet_array = planet_image.load()
clouds_image = Image.new("RGBA", (resolution, resolution))
clouds_array = clouds_image.load()

for y in range(resolution):
    for x in range(resolution):
        planet_noise_value = planet_normalized_noise[y, x]
        for (lower, upper), color in color_map.items():
            if lower <= planet_noise_value <= upper:
                planet_array[x, y] = color
                break
        cloud_noise_value = cloud_normalized_noise[y, x]
        for (lower, upper), color in cloud_map.items():
            if lower <= cloud_noise_value <= upper:
                clouds_array[x, y] = color
                break
Image.alpha_composite(planet_image, clouds_image).show()
#Image.alpha_composite(planet_image, clouds_image).save("planet.png", 'PNG')
