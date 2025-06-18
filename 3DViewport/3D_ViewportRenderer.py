'''
created - 19/06/2025
# author - Cal Lucas
# description - This module contains the 3D viewport renderer class that handles rendering of 3D objects in a viewport.
'''
import pygame
from pygame import *

#ViewportRenderer class
class ViewportRenderer3D:
    def __init__(self, width, height):

        self.width = width
        self.height = height
        #Camera position and orientation
        self.camera_position = [0, 0, -5]  # Camera positioned at (0, 0, -5)
        self.camera_orientation = [0, 0, 0]  # No rotation initially
        '''
        Initializes the ViewportRenderer class.
        This class is responsible for rendering 3D objects in a viewport.
        '''
    
    def camera_move(self, dx, dy, dz):
        '''
        Moves the camera by the specified deltas.
        :param dx: Change in x position
        :param dy: Change in y position
        :param dz: Change in z position
        '''
        self.camera_position[0] += dx
        self.camera_position[1] += dy
        self.camera_position[2] += dz
    
    def camera_rotate(self, pitch, yaw, roll):
        '''
        Rotates the camera by the specified angles.
        :param pitch: Rotation around the x-axis
        :param yaw: Rotation around the y-axis
        :param roll: Rotation around the z-axis
        '''
        self.camera_orientation[0] += pitch
        self.camera_orientation[1] += yaw
        self.camera_orientation[2] += roll


#Window 
    def create_window(self):
        '''
        Creates a window for the 3D viewport.
        This method initializes the Pygame window with the specified width and height.
        '''
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("3D Viewport Renderer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the display to show the black screen
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        
        # Here you would call your rendering methods
        # self.render_objects()
        # CPU / FPS 
            fps = self.clock.get_fps()
            self.screen.fill((0, 0, 0))
         
            # Render the CPU USAGE and FPS
            font = pygame.font.Font(None, 12)
            cpu_usage = pygame.font.Font(None, 12).render(f"CPU Usage: {pygame.time.get_ticks() // 1000}%", True, (255, 255, 255))
            fps_text = font.render(f"FPS: {self.clock.get_fps():.2f}", True, (255, 255, 255))
            self.screen.blit(cpu_usage, (10, 10))
            self.screen.blit(fps_text, (10, 20))
            # Update the display
            pygame.display.flip()  # Update the display
            self.clock.tick(120)  # Limit to 60 FPS


# Example usage
if __name__ == "__main__":
    renderer = ViewportRenderer3D(800, 600)
    renderer.create_window()
    # You can add more methods to render objects here
    # e.g., renderer.render_objects()   

# Note: The actual rendering of 3D objects would require more complex logic, including projection and transformation matrices.
# This code sets up a basic structure for a 3D viewport renderer using Pygame.