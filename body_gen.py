import planet_type as pt


class BodyGen:
    @staticmethod
    def generate_colors(avg_temperature):
        # Temperature - biomes relations
        if avg_temperature < 8:
            ocean_level = 0.042 * avg_temperature
            biomes = pt.PlanetType.g_type_boreal
        elif avg_temperature < 12:
            ocean_level = 1 / 30 * avg_temperature + 0.1
            biomes = pt.PlanetType.g_type_boreal
        elif avg_temperature < 15:
            ocean_level = 1 / 30 * avg_temperature + 0.1
            biomes = pt.PlanetType.g_type_moderate
        elif avg_temperature <= 30:
            ocean_level = 0.011 * avg_temperature + 0.433
            biomes = pt.PlanetType.g_type_moderate
        else:
            ocean_level = 0.011 * avg_temperature + 0.433
            biomes = pt.PlanetType.g_type_dune

        # Biome dependencies
        ocean_layer_I = 2 / 3 * ocean_level
        ocean_layer_II = ocean_layer_I + 1 / 6 * ocean_level
        ocean_layer_III = ocean_layer_II + 1 / 6 * ocean_level
        plant_layer_I = ocean_level + 0.05
        plant_layer_II = plant_layer_I + 0.05
        plant_layer_III = plant_layer_II + 0.2
        land_layer_I = plant_layer_III + 1 / 2 * (1 - plant_layer_III)
        land_layer_II = land_layer_I + 4 / 10 * (1 - plant_layer_III)
        land_layer_III = land_layer_II + 1 / 10 * (1 - plant_layer_III)

        # Painting biomes
        """
        color_map = {
            (-1.0, 0.0): (0, 0, 0, 0),                             # Transparent layer
            (0.0, ocean_layer_I): biomes[0],                       # Ocean layer I
            (ocean_layer_I, ocean_layer_II): biomes[1],            # Ocean layer II
            (ocean_layer_II, ocean_layer_III): biomes[2],          # Ocean layer III
            (ocean_layer_III, plant_layer_I): biomes[3],           # Plants layer I
            (plant_layer_I, plant_layer_II): biomes[4],            # Plants layer II
            (plant_layer_II, plant_layer_III): biomes[5],          # Plants layer III
            (plant_layer_III, land_layer_I): biomes[6],            # Land layer I
            (land_layer_I, land_layer_II): biomes[7],              # Land layer II
            (land_layer_II, land_layer_III): biomes[8],            # Land layer III
        }
        """
        color_map = {
            (-1.0, 0.0): (0, 0, 0, 0),  # Transparent layer
            (0.0, 0.4): biomes[0],  # Ocean layer I
            (0.4, 0.5): biomes[1],  # Ocean layer II
            (0.5, 0.55): biomes[2],  # Ocean layer III
            (0.55, 0.6): biomes[4],  # Plants layer I
            (0.6, 0.66): biomes[5],  # Plants layer II
            (0.66, 0.77): biomes[6],  # Plants layer III
            (0.75, 0.88): biomes[5],  # Land layer I
            (0.88, 0.98): biomes[2],  # Land layer II
            (0.98, 1): biomes[8],  # Land layer III
        }

        print(color_map)
        return color_map

    @staticmethod
    def generate_clouds():
        clouds = pt.PlanetType.clouds
        cloud_map = {
            (-1.0, 0.0): (0, 0, 0, 0),  # Transparent layer
            (0.6, 0.8): clouds[0],
            (0.8, 0.85): clouds[1],
        }
        return cloud_map
