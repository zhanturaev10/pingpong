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
SETTINGS_MENU = "settings_menu"

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
                    current_menu = SETTINGS_MENU
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
        button_positions = update_button_positions(len(main_menu_button_texts))
        for i, (x, y) in enumerate(button_positions):
            draw_button_with_delay(x, y, 400, 50, main_menu_button_texts[i], main_menu_button_actions[i])

        # Handle events
        handle_main_menu_events()

        pygame.display.update()


# Function to handle the Player vs Bot menu
def player_vs_bot_menu():
    global current_menu
    while current_menu == PLAYER_VS_BOT_MENU:
        screen.fill(WHITE)

        # Draw buttons
        button_positions = update_button_positions(len(player_vs_bot_menu_button_texts))
        for i, (x, y) in enumerate(button_positions):
            draw_button_with_delay(x, y, 400, 50, player_vs_bot_menu_button_texts[i],
                                   player_vs_bot_menu_button_actions[i])

        # Handle events
        handle_player_vs_bot_menu_events()

        pygame.display.update()


# Function to handle the Settings menu
def settings_menu():
    global current_menu, current_resolution_index
    while current_menu == SETTINGS_MENU:
        screen.fill(WHITE)

        # Draw buttons
        button_positions = update_button_positions(len(settings_menu_button_texts))
        for i, (x, y) in enumerate(button_positions):
            if i == 0:  # Draw left arrow
                draw_button_with_delay(x, y + 60, 50, 70, "<", decrease_resolution)
            elif i == 1:  # Draw resolution text in the middle
                draw_text(x + 200, y + 40,
                          f"{res_options[current_resolution_index][0]}x{res_options[current_resolution_index][1]}")
            elif i == 2:  # Draw right arrow
                draw_button_with_delay(x + 350, y - 40, 50, 70, ">", increase_resolution)
            elif i == 3:  # Draw Back to Main Menu button
                draw_button_with_delay(x, y, 400, 50, settings_menu_button_texts[i], settings_menu_button_actions[i])

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


def handle_player_vs_bot():
    global current_menu
    current_menu = PLAYER_VS_BOT_MENU


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


def change_resolution():
    global SCREEN_WIDTH, SCREEN_HEIGHT, screen
    SCREEN_WIDTH, SCREEN_HEIGHT = res_options[current_resolution_index]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    update_button_positions()


main_menu_button_texts = ["Player vs Player", "Player vs Bot", "Settings", "Map Editor", "Quit"]
main_menu_button_actions = [handle_player_vs_player, handle_player_vs_bot, handle_settings, handle_map_editor,
                            handle_quit]

player_vs_bot_menu_button_texts = ["Easy", "Normal", "Hard", "Back to Main Menu"]
player_vs_bot_menu_button_actions = [handle_player_vs_bot_easy, handle_player_vs_bot_normal, handle_player_vs_bot_hard,
                                     return_to_main_menu]

settings_menu_button_texts = ["<", ">", "Resolution", "Back to Main Menu"]
settings_menu_button_actions = [decrease_resolution, increase_resolution, None, return_to_main_menu]


def update_button_positions(num_buttons=None):
    if num_buttons is None:
        num_buttons = len(main_menu_button_texts)  # Default to main menu buttons
    button_width = 400
    button_height = 50
    # Calculate horizontal and vertical center positions
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2
    # Calculate total height of all buttons
    total_buttons_height = num_buttons * button_height
    # Calculate the starting y position for the first button
    start_y = center_y - (total_buttons_height // 2)
    # Calculate button y positions based on start_y
    button_y_positions = [start_y + i * button_height for i in range(num_buttons)]
    # Calculate button x position based on center
    button_x_position = center_x - (button_width // 2)
    buttons = [(button_x_position, y) for y in button_y_positions]
    return buttons


if __name__ == "__main__":
    while current_menu is not None:
        if current_menu == MAIN_MENU:
            main_menu()
        elif current_menu == PLAYER_VS_BOT_MENU:
            player_vs_bot_menu()
        elif current_menu == SETTINGS_MENU:
            settings_menu()
