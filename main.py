import pygame
import sys

pygame.init()

# Constants for screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080  # Starting resolution (1920x1080)
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong Menu")

# Define menu states
MAIN_MENU = "main_menu"
PLAYER_VS_BOT_MENU = "player_vs_bot_menu"
SETTINGS_MENU = "settings_menu"  # Added settings menu state

# Variable to hold the current menu state
current_menu = MAIN_MENU

# Add a delay to handle button clicks
BUTTON_CLICK_DELAY = 200  # 200 milliseconds (adjust this value as needed)

# Variable to track the last time a button was clicked
last_click_time = 0

# Fixed resolution options
res_options = [(1920, 1080), (1600, 900), (1280, 1024), (800, 600)]
current_resolution_index = 0

# Function to handle the main menu events
def handle_main_menu_events():
    global current_menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_menu = None
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if 200 <= mouse_pos[0] <= 600:
                if 150 <= mouse_pos[1] <= 200:
                    handle_player_vs_player()
                elif 250 <= mouse_pos[1] <= 300:
                    current_menu = PLAYER_VS_BOT_MENU
                elif 350 <= mouse_pos[1] <= 400:
                    current_menu = SETTINGS_MENU  # Change to settings menu
                elif 450 <= mouse_pos[1] <= 500:
                    handle_map_editor()
                elif 550 <= mouse_pos[1] <= 600:
                    handle_quit()

# Function to handle the Player vs Bot menu events
def handle_player_vs_bot_menu_events():
    global current_menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_menu = None
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if 200 <= mouse_pos[0] <= 600:
                if 150 <= mouse_pos[1] <= 200:
                    handle_player_vs_bot_easy()
                elif 250 <= mouse_pos[1] <= 300:
                    handle_player_vs_bot_normal()
                elif 350 <= mouse_pos[1] <= 400:
                    handle_player_vs_bot_hard()
                elif 450 <= mouse_pos[1] <= 500:
                    return_to_main_menu()

# Function to handle the main menu
def main_menu():
    global current_menu
    while current_menu == MAIN_MENU:
        screen.fill(WHITE)

        # Draw buttons
        draw_button_with_delay(200, 150, 400, 50, "Player vs Player", handle_player_vs_player)
        draw_button_with_delay(200, 250, 400, 50, "Player vs Bot", player_vs_bot_menu)
        draw_button_with_delay(200, 350, 400, 50, "Settings", handle_settings)
        draw_button_with_delay(200, 450, 400, 50, "Map Editor", handle_map_editor)
        draw_button_with_delay(200, 550, 400, 50, "Quit", handle_quit)

        # Handle events
        handle_main_menu_events()

        pygame.display.update()

# Function to handle the Player vs Bot menu
def player_vs_bot_menu():
    global current_menu
    while current_menu == PLAYER_VS_BOT_MENU:
        screen.fill(WHITE)

        # Draw buttons
        draw_button_with_delay(200, 150, 400, 50, "Easy", handle_player_vs_bot_easy)
        draw_button_with_delay(200, 250, 400, 50, "Normal", handle_player_vs_bot_normal)
        draw_button_with_delay(200, 350, 400, 50, "Hard", handle_player_vs_bot_hard)
        draw_button_with_delay(200, 450, 400, 50, "Back to Main Menu", return_to_main_menu)

        # Handle events
        handle_player_vs_bot_menu_events()

        pygame.display.update()

# Function to handle the Settings menu
def settings_menu():
    global current_menu, current_resolution_index
    while current_menu == SETTINGS_MENU:
        screen.fill(WHITE)

        # Draw buttons
        draw_button_with_delay(200, 100, 50, 50, "<", decrease_resolution)
        draw_button_with_delay(650, 100, 50, 50, ">", increase_resolution)

        # Draw current resolution text
        draw_text(400, 100, f"Resolution: {res_options[current_resolution_index][0]}x{res_options[current_resolution_index][1]}")

        draw_button_with_delay(200, 200, 400, 50, "Back to Main Menu", return_to_main_menu)

        # Handle events
        handle_settings_menu_events()

        pygame.display.update()

# Function to handle the settings menu events
def handle_settings_menu_events():
    global current_menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_menu = None
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if 200 <= mouse_pos[0] <= 600:
                if 100 <= mouse_pos[1] <= 150:
                    decrease_resolution()
                elif 650 <= mouse_pos[1] <= 200:
                    increase_resolution()
                elif 200 <= mouse_pos[1] <= 250:
                    return_to_main_menu()

# Function to draw buttons with a delay (updated for dynamic resizing and repositioning)
def draw_button_with_delay(x, y, width, height, text, action=None):
    global last_click_time
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, (200, 200, 200), (x, y, width, height))
        if click[0] == 1 and action is not None:
            current_time = pygame.time.get_ticks()
            if current_time - last_click_time > BUTTON_CLICK_DELAY:
                action()
                last_click_time = current_time
    else:
        pygame.draw.rect(screen, (150, 150, 150), (x, y, width, height))

    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

# Function to draw text
def draw_text(x, y, text):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def handle_player_vs_player():
    print("Player vs Player selected")

# Functions to handle the Player vs Bot difficulty options
def handle_player_vs_bot_easy():
    print("Player vs Bot (Easy) selected")

def handle_player_vs_bot_normal():
    print("Player vs Bot (Normal) selected")

def handle_player_vs_bot_hard():
    print("Player vs Bot (Hard) selected")

# Function to handle the Settings option
def handle_settings():
    print("Settings selected")

# Function to handle the Map Editor option
def handle_map_editor():
    print("Map Editor selected")

# Function to handle the Quit option
def handle_quit():
    global current_menu
    current_menu = None
    pygame.quit()
    sys.exit()

# Function to return to the main menu
def return_to_main_menu():
    global current_menu
    current_menu = MAIN_MENU
# Function to handle the Settings option
def handle_settings():
    global current_menu
    current_menu = SETTINGS_MENU
def increase_resolution():
    global current_resolution_index
    current_resolution_index = (current_resolution_index + 1) % len(res_options)
    change_resolution()

# Function to decrease the resolution
def decrease_resolution():
    global current_resolution_index
    current_resolution_index = (current_resolution_index - 1) % len(res_options)
    change_resolution()

# Function to change the resolution immediately after switching
def change_resolution():
    global SCREEN_WIDTH, SCREEN_HEIGHT
    SCREEN_WIDTH, SCREEN_HEIGHT = res_options[current_resolution_index]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Update button positions and sizes based on the new resolution
    update_button_positions()

# Function to update button positions and sizes based on the current resolution
def update_button_positions():
    # Main menu button positions
    main_menu_buttons_y = [150, 250, 350, 450, 550]
    player_vs_bot_menu_buttons_y = [150, 250, 350, 450]
    settings_menu_buttons_y = [100, 200]

    # Update button positions
    buttons = [
        (200, main_menu_buttons_y[0], 400, 50),  # Player vs Player
        (200, main_menu_buttons_y[1], 400, 50),  # Player vs Bot
        (200, main_menu_buttons_y[2], 400, 50),  # Settings
        (200, main_menu_buttons_y[3], 400, 50),  # Map Editor
        (200, main_menu_buttons_y[4], 400, 50),  # Quit

        (200, player_vs_bot_menu_buttons_y[0], 400, 50),  # Easy
        (200, player_vs_bot_menu_buttons_y[1], 400, 50),  # Normal
        (200, player_vs_bot_menu_buttons_y[2], 400, 50),  # Hard
        (200, player_vs_bot_menu_buttons_y[3], 400, 50),  # Back to Main Menu

        (200, settings_menu_buttons_y[0], 50, 50),  # "<" arrow
        (650, settings_menu_buttons_y[0], 50, 50),  # ">" arrow
        (400, settings_menu_buttons_y[0], 400, 50),  # Resolution text
        (200, settings_menu_buttons_y[1], 400, 50)  # Back to Main Menu
    ]

    for i, button in enumerate(buttons):
        buttons[i] = (
            round(button[0] * SCREEN_WIDTH / 1920),
            round(button[1] * SCREEN_HEIGHT / 1080),
            round(button[2] * SCREEN_WIDTH / 1920),
            round(button[3] * SCREEN_HEIGHT / 1080)
        )

    return buttons

if __name__ == "__main__":
    while current_menu is not None:
        if current_menu == MAIN_MENU:
            main_menu()
        elif current_menu == PLAYER_VS_BOT_MENU:
            player_vs_bot_menu()
        elif current_menu == SETTINGS_MENU:
            settings_menu()
