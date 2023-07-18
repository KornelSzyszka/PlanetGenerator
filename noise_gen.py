import random
import noise
import numpy as np


class NoiseGen:
    @staticmethod
    def generate_noise(resolution, avg_temperature):
        center = resolution // 2
        scale = 0.2 * resolution
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0
        seed = random.randint(0, 100)
        noise_array = np.zeros((resolution, resolution))

        for y in range(resolution):
            for x in range(resolution):
                squared_distance_to_center = (x - center) ** 2 + (y - center) ** 2
                if squared_distance_to_center <= center ** 2:
                    noise_value = noise.pnoise2(x / scale,
                                                y / scale,
                                                octaves=octaves,
                                                persistence=persistence,
                                                lacunarity=lacunarity,
                                                repeatx=resolution,
                                                repeaty=resolution,
                                                base=seed)
                    noise_array[y, x] = noise_value

        normalized_noise = (noise_array - np.min(noise_array)) / \
                           (np.max(noise_array) - np.min(noise_array))

        background = normalized_noise[0, 0]
        for y in range(resolution):
            for x in range(resolution):
                if normalized_noise[y, x] == background:
                    normalized_noise[y, x] = -0.1

        for y in range(resolution):
            for x in range(resolution):
                if normalized_noise[y, x] > 0:
                    z = distance_from_center = abs(y - center)
                    normalized_noise[y, x] += z/(avg_temperature**3 + 1/4*avg_temperature)
                    if normalized_noise[y, x] > 1:
                        normalized_noise[y, x] = 1

        return normalized_noise
