class PlanetType:
    # Biome list
    # Water layers
    __deep_ocean = (0, 0, 70)
    __warm_deep_ocean = (0, 160, 190)
    __ocean = (0, 0, 80)
    __warm_ocean = (0, 170, 210)
    __coastal = (0, 10, 90)
    __warm_coastal = (0, 190, 230)
    __coast = (190, 180, 70)
    __cold_coast = (80, 75, 50)
    __frozen_coast = (190, 255, 250)
    __frozen = (225, 255, 245)
    __frozen2 = (225, 220, 245)
    __frozen3 = (210, 230, 230)
    # Vegetation layers
    __g_tundra = (0, 100, 90)
    __g_taiga = (0, 80, 60)
    __g_continental_forest = (0, 105, 60)
    __g_continental_steppe = (90, 180, 80)
    __g_mediterranean = (135, 200, 20)
    __g_subtropical = (50, 110, 20)
    __g_tropical = (20, 80, 20)
    __g_savanna = (115, 130, 40)
    # Land layers
    __semi_arid = (190, 140, 36)
    __arid_desert = (174, 155, 36)
    __snow_biome = (255, 255, 255)
    __mountains = (20, 30, 45)
    # Clouds
    __cloud_body = (255, 255, 255, 160)
    __cloud_shape = (220, 255, 255, 150)

    clouds = (
        (255, 255, 255, 190),
        (255, 255, 235, 200),
    )

    # Water maps
    standard_ocean = (
        __deep_ocean,
        __ocean,
        __coastal,
        __coast,
    )

    frozen_ocean = (
        __frozen,
        __frozen2,
        __frozen3,
        __frozen_coast,
    )

    warm_ocean = (
        __warm_deep_ocean,
        __warm_ocean,
        __warm_coastal,
        __coast,
    )

    # Land Maps
    noise_world = (
        (0, 0, 0),
        (21, 21, 21),
        (42, 42, 42),
        (63, 63, 63),
        (84, 84, 84),
        (105, 105, 105),
        (126, 126, 126),
        (147, 147, 147),
        (168, 168, 168),
        (189, 189, 189),
        (210, 210, 210),
        (231, 231, 231),
    )

    frozen_world = (
        __snow_biome,
        __snow_biome,
        __snow_biome,
        __snow_biome,
        __snow_biome,
        __snow_biome,
        __snow_biome,
        __snow_biome,
        __snow_biome,
        __snow_biome,
        __snow_biome,
        __snow_biome,
    )

    g_boreal_world = (
        __g_savanna,
        __g_taiga,
        __g_tundra,
        __g_taiga,
        __g_tundra,
        __g_taiga,
        __g_tundra,
        __mountains,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
    )

    g_cold_temperate_world = (
        __g_mediterranean,
        __g_savanna,
        __g_continental_steppe,
        __g_continental_forest,
        __g_continental_forest,
        __g_taiga,
        __g_taiga,
        __g_taiga,
        __g_tundra,
        __g_tundra,
        __mountains,
        __frozen,
    )

    g_temperate_world = (
        __g_tropical,
        __arid_desert,
        __semi_arid,
        __g_subtropical,
        __g_savanna,
        __g_mediterranean,
        __g_continental_steppe,
        __g_continental_forest,
        __g_taiga,
        __g_tundra,
        __mountains,
        __frozen,
    )

    g_tropical_world = (
        __semi_arid,
        __arid_desert,
        __g_tropical,
        __g_subtropical,
        __g_savanna,
        __g_mediterranean,
        __g_continental_steppe,
        __g_subtropical,
        __g_tropical,
        __g_continental_forest,
        __g_continental_steppe,
        __g_tropical,
    )

    g_dune_world = (
        __arid_desert,
        __semi_arid,
        __arid_desert,
        __semi_arid,
        __g_savanna,
        __g_savanna,
        __semi_arid,
        __g_subtropical,
        __g_tropical,
        __semi_arid,
        __g_mediterranean,
        __mountains,
    )

