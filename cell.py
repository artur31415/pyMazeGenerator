import pygame


class Cell:


    walls = {
        "Left": True,
        "Right": True,
        "Top": True,
        "Bottom": True
    }

    grid_pos = (0, 0)
    is_visited = False

    def __init__(self, position) -> None:
        self.grid_pos = position

    def draw(self, SURFACE, cell_size):
        cartesian_pos = self.grid_to_cartesian(cell_size)

        col = (255, 0, 0)
        if self.is_visited:
            col = (255, 255, 0)

        pygame.draw.rect(SURFACE, col, (cartesian_pos[0], cartesian_pos[1], cell_size, cell_size))
            
        for k, v in self.walls.items():
            if v:
                s_pos, e_pos = self.get_line_positions(k, cell_size)
                pygame.draw.line(SURFACE, (0, 0, 0), s_pos, e_pos)

    def grid_to_cartesian(self, cell_size):
        return (self.grid_pos[0] * cell_size, self.grid_pos[1] * cell_size)

    def get_line_positions(self, line_key, cell_size):
        cartesian_pos = self.grid_to_cartesian(cell_size)
        start_pos = cartesian_pos
        end_pos = (0, 0)

        if line_key == "Left":
            end_pos = (cartesian_pos[0], cartesian_pos[1] + cell_size)
        elif line_key == "Bottom":
            start_pos = (cartesian_pos[0], cartesian_pos[1] + cell_size)
            end_pos = (cartesian_pos[0] + cell_size, cartesian_pos[1] + cell_size)
        elif line_key == "Right":
            start_pos = (cartesian_pos[0] + cell_size, cartesian_pos[1] + cell_size)
            end_pos = (cartesian_pos[0] + cell_size, cartesian_pos[1])
        elif line_key == "Top":
            start_pos = (cartesian_pos[0] + cell_size, cartesian_pos[1])
            end_pos = (cartesian_pos[0], cartesian_pos[1])
        else:
            print("what key? ", str(line_key))

        return start_pos, end_pos