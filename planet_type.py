class PlanetType:
    # Biome list
    # Ocean layer
    __deep_ocean_biome = (0, 0, 70)
    __ocean_biome = (0, 0, 80)
    __coastal_biome = (0, 10, 90)
    __frozen_ocean = (225, 255, 245)
    # Plant layer
    __g_rainforest_biome = (0, 130, 60)
    __g_continental_biome = (0, 105, 60)
    __g_boreal_biome = (0, 80, 60)
    __g_tundra_biome = (0, 100, 90)
    __g_oasis_biome = (0, 120, 60)
    # Land layer
    __coast_biome = (190, 180, 70)
    __cold_coast_biome = (110, 100, 90)
    __desert_biome = (210, 175, 105)
    __snow_biome = (255, 255, 255)
    __mountains = (20, 30, 45)
    # Clouds
    __cloud_body = (255, 255, 255, 160)
    __cloud_shape = (220, 255, 255, 150)

    g_type_moderate = (
        __deep_ocean_biome,
        __ocean_biome,
        __coastal_biome,
        __coast_biome,
        __g_rainforest_biome,
        __g_continental_biome,
        __g_boreal_biome,
        __mountains,
        __snow_biome)

    g_type_boreal = (
        __deep_ocean_biome,
        __ocean_biome,
        __coastal_biome,
        __frozen_ocean,
        __g_tundra_biome,
        __g_boreal_biome,
        __mountains,
        __snow_biome,
        __snow_biome
    )

    g_type_dune = (
        __desert_biome,
        __coast_biome,
        __desert_biome,
        __desert_biome,
        __coast_biome,
        __coast_biome,
        __g_oasis_biome,
        __coastal_biome,
        __ocean_biome,
    )

    g_type_cold = (
        __mountains,
        __g_boreal_biome,
        __frozen_ocean,
        __snow_biome,
        __snow_biome,
        __snow_biome,
        __snow_biome,
        __frozen_ocean,
        __deep_ocean_biome
    )

    clouds = (
        __cloud_body,
        __cloud_shape,
    )
