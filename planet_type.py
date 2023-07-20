class PlanetType:
    # Biome list
    # Water layers
    __deep_ocean = (0, 0, 70)
    __ocean = (0, 0, 80)
    __coastal = (0, 10, 90)
    __frozen = (225, 255, 245)
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
    __coast = (190, 180, 70)
    __frozen_coast = (190, 255, 250)
    __semi_arid = (190, 140, 36)
    __arid_desert = (174, 155, 36)
    __snow_biome = (255, 255, 255)
    __mountains = (20, 30, 45)
    # Clouds
    __cloud_body = (255, 255, 255, 160)
    __cloud_shape = (220, 255, 255, 150)

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

    )

    ocean_layer = (
        __deep_ocean,
        __ocean,
        __coastal,
    )

    g_boreal_world = (

    )

    g_cold_temperate_world = (
        __g_savanna,
        __g_continental_steppe,
        __g_continental_forest,
        __g_continental_forest,
        __g_taiga,
        __g_taiga,
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

    g_atoll_world = (

    )

    g_dune_world = (

    )

    clouds = (
        (255, 255, 255, 190),
        (255, 255, 235, 200),
    )
