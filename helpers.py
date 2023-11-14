import pygame

def build_background(screen):
    # Returns a pygame surface that will be the game background

    # define each of the tiles i want
    strt = pygame.image.load('assets/road_textures/roadTexture_01.png')
    strt_h = pygame.image.load('assets/road_textures/roadTexture_13.png')
    tl = pygame.image.load('assets/road_textures/roadTexture_02.png')
    tr = pygame.image.load('assets/road_textures/roadTexture_03.png')
    bl = pygame.image.load('assets/road_textures/roadTexture_14.png')
    br = pygame.image.load('assets/road_textures/roadTexture_15.png')
    grass = pygame.image.load('assets/road_textures/roadTexture_25.png')


    # get the screen size and width
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # get the tile size
    tile_size = strt.get_width()

    # make a surface that will be the background
    bg = pygame.Surface((screen_width, screen_height))
    # make the screen all grass
    for i in range(0, screen_width, tile_size):
        for j in range(0, screen_height, tile_size):
            bg.blit(grass, (i,j))

    # build a grid defining where all of my tiles go
    grid = [
        [tl,   strt_h, strt_h, strt_h, strt_h,    tr],
        [strt, grass, grass, grass, grass, strt],
        [strt, grass, grass, grass, grass, strt],
        [strt, grass, grass, grass, grass, strt],
        [strt, grass, grass, grass, grass, strt],
        [strt, grass, grass, grass, grass, strt],
        [bl, strt_h, strt_h, strt_h, strt_h, br],
    ]

    # loop over each piece of the grid and blit it to the surface (i,j) pixels

    # make the track surface
    track_width = len(grid[0]) * tile_size
    track_height = len(grid) * tile_size
    track = pygame.Surface((track_width, track_height))

    # loop over the y pixels of the screen
    for n, j in enumerate(range(0, track_height, tile_size)):

        # loop over the x pixels of screen
        for m, i in enumerate(range(0, track_width, tile_size)):
            # blit the tile to the surface
            try: track.blit(grid[n][m], (i,j))
            except: track.blit(grass, (i,j))

    # blit the track to background
    bg.blit(track, (screen_width//2 - track_width//2,
                    screen_height//2 - track_height//2))

    # return my surface that I made
    return bg
