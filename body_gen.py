import planet_type as pt


class BodyGen:
    @staticmethod
    def generate_colors(avg_temperature, star_type):
        # Temperature - biomes relations
        if avg_temperature < -30:
            biomes = pt.PlanetType.frozen_world
            water_map = pt.PlanetType.frozen_ocean
        elif avg_temperature < 0:
            biomes_attr = f"{star_type}_boreal_world"
            biomes = getattr(pt.PlanetType, biomes_attr)
            water_map = pt.PlanetType.frozen_ocean
        elif avg_temperature < 10:
            biomes_attr = f"{star_type}_cold_temperate_world"
            biomes = getattr(pt.PlanetType, biomes_attr)
            water_map = pt.PlanetType.standard_ocean
        elif avg_temperature < 22:
            biomes_attr = f"{star_type}_temperate_world"
            biomes = getattr(pt.PlanetType, biomes_attr)
            water_map = pt.PlanetType.standard_ocean
        elif avg_temperature < 36:
            biomes_attr = f"{star_type}_tropical_world"
            biomes = getattr(pt.PlanetType, biomes_attr)
            water_map = pt.PlanetType.warm_ocean
        else:
            biomes_attr = f"{star_type}_dune_world"
            biomes = getattr(pt.PlanetType, biomes_attr)
            water_map = pt.PlanetType.warm_ocean

        water_map = {
            (-1.0, 0.0): (0, 0, 0, 0),  # Backgroud
            (0., 0.6): water_map[0],  # Deep ocean
            (0.6, 0.8): water_map[1],  # Ocean
            (0.8, 0.97): water_map[2],  # Coastal
            (0.97, 1): water_map[3],
        }

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
        return water_map, land_map

    @staticmethod
    def generate_clouds():
        clouds = pt.PlanetType.clouds
        cloud_map = {
            (-1.0, 0.0): (0, 0, 0, 0),  # Transparent layer
            (0.6, 0.8): clouds[0],
            (0.8, 0.85): clouds[1],
        }
        return cloud_map
