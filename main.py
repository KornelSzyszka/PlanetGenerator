from PIL import Image
import noise_gen as ng
import body_gen as bg

resolution = 1024

avg_temperature = 12

noise_map = ng.NoiseGen.generate_noise(resolution, avg_temperature)
clouds_noise_map = ng.NoiseGen.generate_clouds_noise(resolution)
water_normalized_noise, planet_normalized_noise, = noise_map
water_map = bg.BodyGen.generate_water()
land_map = bg.BodyGen.generate_colors(avg_temperature)
cloud_map = bg.BodyGen.generate_clouds()

land_image = Image.new("RGBA", (resolution, resolution))
planet_array = land_image.load()
clouds_image = Image.new("RGBA", (resolution, resolution))
clouds_array = clouds_image.load()
water_image = Image.new("RGBA", (resolution, resolution))
water_array = water_image.load()

for y in range(resolution):
    for x in range(resolution):
        planet_noise_value = planet_normalized_noise[y, x]
        for (lower, upper), color in land_map.items():
            if lower <= planet_noise_value <= upper:
                planet_array[x, y] = color
                break
        cloud_noise_value = clouds_noise_map[y, x]
        for (lower, upper), color in cloud_map.items():
            if lower <= cloud_noise_value <= upper:
                clouds_array[x, y] = color
                break
        water_noise_value = water_normalized_noise[y, x]
        for (lower, upper), color in water_map.items():
            if lower <= water_noise_value <= upper:
                water_array[x, y] = color
                break
shadow_image = Image.open("shadow.png")
shadow_image.resize((resolution, resolution), Image.LANCZOS)
planet_image = Image.alpha_composite(water_image, land_image)
output_image = Image.alpha_composite(planet_image, clouds_image)
output_image = Image.alpha_composite(output_image, shadow_image)
output_image.save("Planet.png")
output_image.show()
