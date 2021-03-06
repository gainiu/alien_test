import sys
import pygame
from rect_bullet import RectBullet
from rect import RectBox


def check_event(rect_settings, screen, rectplayer, rectbullets, stats, button, rectboxes, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(rect_settings, screen,
                                event, rectplayer, rectbullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, rectplayer)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(rect_settings, screen, rectboxes,
                              rectplayer, rectbullets, stats, button, mouse_x, mouse_y)


def check_play_button(rect_settings, screen, rectboxes, rectplayer, rectbullets, stats, button, mouse_x, mouse_y):
    if button.rect.collidepoint(mouse_x, mouse_y) and not stats.rect_active:
        rect_settings.initial_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.rect_active = True

        rectbullets.empty()
        rectboxes.empty()

        create_boxes(rect_settings, screen, rectboxes)
        rectplayer.player_center()


def check_keydown_event(rect_settings, screen, event, rectplayer, rectbullets, stats):
    if event.key == pygame.K_UP:
        rectplayer.moving_up = True
    elif event.key == pygame.K_DOWN:
        rectplayer.moving_down = True
    elif event.key == pygame.K_SPACE:
        if len(rectbullets) == 0 and stats.rect_active:
            create_rectbullets(rect_settings, screen, rectplayer, rectbullets)


def check_keyup_event(event, rectplayer):
    if event.key == pygame.K_UP:
        rectplayer.moving_up = False
    elif event.key == pygame.K_DOWN:
        rectplayer.moving_down = False


def create_rectbullets(rect_settings, screen, rectplayer, rectbullets):
    new_bullet = RectBullet(rect_settings, screen, rectplayer)
    rectbullets.add(new_bullet)


def check_bullet_box_collide(rect_settings, screen, rectbullets, rectboxes):
    collisions = pygame.sprite.groupcollide(rectboxes, rectbullets, True, True)
    if len(rectboxes) == 0:
        rectboxes.empty()
        rect_settings.increase_speed()
        create_boxes(rect_settings, screen, rectboxes)


def create_boxes(rect_settings, screen, rectboxes):
    rectbox = RectBox(rect_settings, screen)
    rectboxes.add(rectbox)


def update_rectbox(rect_settings, screen, rectboxes, rectbullets):
    screen_rect = screen.get_rect()
    for rectbox in rectboxes.sprites():
        if rectbox.rect.bottom >= screen_rect.bottom:
            rectbox.moving_up = True
            rectbox.moving_down = False
        if rectbox.rect.top <= 0:
            rectbox.moving_down = True
            rectbox.moving_up = False
    rectboxes.update()
    check_bullet_box_collide(rect_settings, screen, rectbullets, rectboxes)


def update_bullet(rectbullets, screen, stats):
    screen_rect = screen.get_rect()
    rectbullets.update()
    if stats.rect_left > 0:
        for bullet in rectbullets.copy():
            if bullet.rect.right >= screen_rect.right:
                stats.rect_left -= 1
                rectbullets.remove(bullet)
    else:
        stats.rect_active = False
        rectbullets.empty()
        pygame.mouse.set_visible(True)


def update_screen(rect_settings, screen, rectboxes, rectplayer, rectbullets, stats, button):
    screen.fill(rect_settings.screen_bg)
    for bullet in rectbullets.sprites():
        bullet.draw_bullet()
    for rectbox in rectboxes.sprites():
        rectbox.draw_rect()
    rectplayer.blitme()
    if not stats.rect_active:
        button.draw_button()
    pygame.display.flip()
