from the_flying_chair_adventures.game_settings.status import Health


class Blob:
    def __init__(self, screen, sprite, position_x, position_y, velocity_x, velocity_y):
        self.screen = screen
        self.sprite = sprite
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    # moving the blob sprite
    def update_blob(self):
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y

    # Drawing the blob sprite on the screen
    def draw_blob(self):
        self.screen.blit(self.sprite, (self.position_x, self.position_y))

    # Getting the size and the position of the blob sprite
    def hitbox_blob(self):
        hitbox_blob = self.sprite.get_rect()
        hitbox_blob.x = self.position_x
        hitbox_blob.y = self.position_y
        return hitbox_blob


class BlobManager:
    position_x_list = list()
    position_y_list = list()

    def __init__(self, screen, sprite):
        self.screen = screen
        self.sprite = sprite

        for i in range(20, 800, 20):
            self.position_y_list.append(i)

        self.position_y = random.choice(self.position_y_list)
