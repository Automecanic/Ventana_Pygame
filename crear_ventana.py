# coding=utf-8

# importa la librería Pygame
import pygame


def main():
    # inicializa Pygame
    pygame.init()

    # establece el título de la ventana
    pygame.display.set_caption(u'Crear ventana')

    # establece el tamaño de la ventana
    pygame.display.set_mode((400, 400))

    # bucle infinito
    while True:
        # retorna un solo evento de la cola de eventos
        event = pygame.event.wait()

        # si se presiona el botón 'cerrar' de la ventana
        if event.type == pygame.QUIT:
            # detiene el bucle
            break

    # finaliza Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
