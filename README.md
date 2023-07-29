# Planet Generator
The program is written in Python and is designed to generate procedural 2D planets in the form of images. It utilizes the Tkinter library to create a simple user interface and the PIL (Pillow) library for image manipulation and generation.

Main features of the program:
- User Interface: The program has a simple user interface built with Tkinter. Users can choose various parameters for the generated planet, such as resolution, average temperature, and star type.
- Procedural Planet Generation: The program uses noise generation algorithms from the "noise_gen" library. Noise is used to generate the planet's terrain height and shape, giving it a natural and random appearance.
- Biome Creation: Based on the generated noise and the average temperature and star type parameters, the program creates different biomes such as land, water, and clouds. Each biome is assigned appropriate colors, which are used to color the planet.
- Image Display and Saving: After generating the planet, the program displays the planet's image in the main application window. Users have the option to save the generated image in PNG format.

How the program works:
Upon launching the program, the user sees the application interface with various controls. They can change the planet's parameters, such as resolution, average temperature, and star type, using sliders and radio buttons.
After clicking the "Generate Planet" button, the program procedurally generates a planet with the selected parameters. It then displays the generated planet's image in the main application window. The planet is divided into different biomes with corresponding colors.
Users can save the generated image by clicking the "Save Planet" button. After choosing a location and file name, the image will be saved in PNG format.

-------------------------------------------------------------------------------------------------------------
G-type 22°C
![G22](https://github.com/KornelSzyszka/PlanetGenerator/assets/66333958/6406b884-d64f-4a0d-92e9-034e7c30b0bc)
-------------------------------------------------------------------------------------------------------------
M-Type 16°C
![M16](https://github.com/KornelSzyszka/PlanetGenerator/assets/66333958/b1ed5a09-4683-4f52-9b95-eeb6fa04f9f7)
-------------------------------------------------------------------------------------------------------------
G-Type 10°C
![G10](https://github.com/KornelSzyszka/PlanetGenerator/assets/66333958/8df7e81f-7475-4ddb-abee-b3da01a911a1)
-------------------------------------------------------------------------------------------------------------
M-Type 15°C
![M-15](https://github.com/KornelSzyszka/PlanetGenerator/assets/66333958/3c6fe327-ff4e-43d3-a85c-bebdbab1e945)
-------------------------------------------------------------------------------------------------------------
K-Type 22°C
![K22](https://github.com/KornelSzyszka/PlanetGenerator/assets/66333958/dc71e6e9-0d4a-4436-a7f9-c0fa55963401)
-------------------------------------------------------------------------------------------------------------
M-Type 12°C
![M12](https://github.com/KornelSzyszka/PlanetGenerator/assets/66333958/93ea991d-3455-4eaf-b5ed-cc58c4f45e43)
-------------------------------------------------------------------------------------------------------------
G-Type 10°C
![G-10](https://github.com/KornelSzyszka/PlanetGenerator/assets/66333958/8f7f30ba-98c0-42d9-b1ef-1e532180e81e)
-------------------------------------------------------------------------------------------------------------
K-Type 3°C
![K3](https://github.com/KornelSzyszka/PlanetGenerator/assets/66333958/c3172f40-847f-4e32-bb85-b9230d021c30)
-------------------------------------------------------------------------------------------------------------
