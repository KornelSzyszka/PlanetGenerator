import planet_type as pt


class BodyGen:
    @staticmethod
    def generate_water():
        water_map = {
            (-1.0, 0.0): (0, 0, 0, 0),          # Backgroud
            (0., 0.6): (0, 0, 70),              # Deep ocean
            (0.6, 0.8): (0, 0, 80),             # Ocean
            (0.8, 0.97): (0, 0, 90),               # Coastal
            (0.97, 1): (190, 180, 70)
        }
        return water_map

    @staticmethod
    def generate_colors(avg_temperature):
        # Temperature - biomes relations
        if avg_temperature < -30:
            biomes = pt.PlanetType.noise_world
        elif avg_temperature < 0:
            biomes = pt.PlanetType.noise_world
        elif avg_temperature < 10:
            biomes = pt.PlanetType.g_cold_temperate_world
        elif avg_temperature < 22:
            biomes = pt.PlanetType.g_temperate_world
        elif avg_temperature < 36:
            biomes = pt.PlanetType.noise_world
        else:
            biomes = pt.PlanetType.noise_world

        # Painting biomes
        land_map = {
            (-1.0, 0.0): (0, 0, 0, 0),  # Transparent layer
            (0.0, 0.6): biomes[0],  # Ocean layer I
            (0.6, 0.7): biomes[1],  # Ocean layer II
            (0.7, 0.8): biomes[2],  # Ocean layer III
            (0.8, 0.85): biomes[3],  # Plants layer I
            (0.85, 0.88): biomes[4],  # Plants layer II
            (0.88, 0.9): biomes[5],  # Plants layer III
            (0.9, 0.92): biomes[6],  # Land layer I
            (0.92, 0.98): biomes[7],  # Land layer II
            (0.98, 1): biomes[8],  # Land layer III
        }
        return land_map

    @staticmethod
    def generate_clouds():
        clouds = pt.PlanetType.clouds
        cloud_map = {
            (-1.0, 0.0): (0, 0, 0, 0),  # Transparent layer
            (0.6, 0.8): clouds[0],
            (0.8, 0.85): clouds[1],
        }
        return cloud_map
