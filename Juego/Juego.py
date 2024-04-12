import pygame

# Inicializar Pygame
pygame.init()

# Tamaño de la pantalla
screen_size = [500, 500]

# Coordenadas del círculo
center_x = 250
center_y = 250
radius = 75

# Crear la ventana
screen = pygame.display.set_mode(screen_size)

running = True
is_dragging = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            dist_x = mouse_pos[0] - center_x
            dist_y = mouse_pos[1] - center_y
            is_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            is_dragging = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                center_y -= 10
            elif event.key == pygame.K_s:
                center_y += 10
            elif event.key == pygame.K_a:
                center_x -= 10
            elif event.key == pygame.K_d:
                center_x += 10

    screen.fill(("black")) # Se pinta el fondo de la ventana
    # Se dibuja un círculo verde en el centro (usando las variables)
    pygame.draw.circle(screen, ("green"), (center_x, center_y), radius)
    
    if is_dragging:
        mouse_pos = pygame.mouse.get_pos()
        center_x = mouse_pos[0] - dist_x
        center_y = mouse_pos[1] - dist_y

    pygame.display.flip() # Muestra los cambios en la pantalla
        
pygame.quit()
