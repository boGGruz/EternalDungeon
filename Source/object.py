import pygame as pg
from textures import Texture_Items


class Items:
    def __init__(self):
        self.texture = Texture_Items()
        self.potion = self.texture.items["heal_potion"]
        self.potion_rect = self.potion.get_rect()
        self.attack = self.texture.items["attack_1"]
        self.hole = self.texture.items["hole_lock"]
        self.hole_rect = self.hole.get_rect()
        self.attack = pg.transform.scale(self.attack,(64, 64))
        self.attack_rect = self.attack.get_rect()
        self.get_pressed = False
        self.key_texture = self.texture.items["key"]
        self.key_rect = self.key_texture.get_rect()

    def healing_potion(self, window, character):
        if character.colliderect(self.potion_rect):
            self.potion = self.texture.items["heal_potion_pickup"]
        else:
            self.potion = self.texture.items["heal_potion"]
        self.potion_rect.x = 800 - 21
        self.potion_rect.y = 450 - 25
        window.blit(self.potion, self.potion_rect)

    def attack_up(self, window, character, rand_up):
        if character.colliderect(self.attack_rect):
            self.attack = self.texture.items[f"attack_pickup_{rand_up}"]
            self.attack = pg.transform.scale(self.attack, (96, 96))
        else:
            self.attack = self.texture.items[f"attack_{rand_up}"]
            self.attack = pg.transform.scale(self.attack, (96, 96))
        self.attack_rect.x = 800 - 48
        self.attack_rect.y = 450 - 48
        window.blit(self.attack, self.attack_rect)

    def hole_triger(self, window, character):
        if character.colliderect(self.hole_rect):
            self.hole = self.texture.items["hole_lock_pickup"]
            self.hole = pg.transform.scale(self.hole, (128, 128))
        else:
            self.hole = self.texture.items["hole_lock"]
            self.hole = pg.transform.scale(self.hole, (128, 128))
        self.hole_rect = self.hole.get_rect()
        self.hole_rect.x = 800 - 64
        self.hole_rect.y = 400 - 64
        window.blit(self.hole, self.hole_rect)

    def key(self, window, character):
        if character.colliderect(self.key_rect):
            self.key_texture = self.texture.items["key_pickup"]
            self.key_texture = pg.transform.scale(self.key_texture, (96, 96))
        else:
            self.key_texture = self.texture.items["key"]
            self.key_texture = pg.transform.scale(self.key_texture, (96, 96))
        self.key_rect = self.key_texture.get_rect()
        self.key_rect.x = 800 - 48
        self.key_rect.y = 400 - 48
        window.blit(self.key_texture, self.key_rect)










