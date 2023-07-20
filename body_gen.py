import planet_type as pt


class BodyGen:
    @staticmethod
    def generate_water():
        water_map = {
            (-1.0, 0.0): (0, 0, 0, 0),          # Backgroud
            (0., 0.6): (0, 0, 70),              # Deep ocean
            (0.6, 0.8): (0, 0, 80),             # Ocean
            (0.8, 0.98): (0, 0, 90),            # Coastal
            (0.98, 1): (190, 180, 70)
        }
        return water_map

    @staticmethod
    def generate_colors(avg_temperature):
        # Temperature - biomes relations
        if avg_temperature < -30:
            biomes = pt.PlanetType.frozen_world
        elif avg_temperature < 0:
            biomes = pt.PlanetType.g_boreal_world
        elif avg_temperature < 10:
            biomes = pt.PlanetType.g_cold_temperate_world
        elif avg_temperature < 22:
            biomes = pt.PlanetType.g_temperate_world
        elif avg_temperature < 36:
            biomes = pt.PlanetType.g_tropical_world
        else:
            biomes = pt.PlanetType.g_dune_world

        # Painting biomes
        land_map = {
            (-1.0, 0.0): (0, 0, 0, 0),
            (0.0, 0.16): biomes[0],
            (0.16, 0.2): biomes[1],
            (0.2, 0.24): biomes[2],
            (0.24, 0.32): biomes[3],
            (0.32, 0.4): biomes[4],
            (0.4, 0.48): biomes[5],
            (0.48, 0.64): biomes[6],
            (0.64, 0.8): biomes[7],
            (0.8, 0.86): biomes[8],
            (0.86, 0.92): biomes[9],
            (0.92, 0.95): biomes[10],
            (0.95, 1): biomes[11],
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
