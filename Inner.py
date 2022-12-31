import pygame
from Warrior import Warrior

pygame.init()

clock = pygame.time.Clock()

red_warrior_group = pygame.sprite.GroupSingle()
red_warrior_group.add(Warrior('bottom'))

blue_warrior_group = pygame.sprite.GroupSingle()
blue_warrior_group.add(Warrior('top'))

red_bullets_group = pygame.sprite.Group()
blue_bullets_group = pygame.sprite.Group()
explosions = []

red_hit_bullets = None
blue_hit_bullets = None
