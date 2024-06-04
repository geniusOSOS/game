import pygame
import random
import sys
import os
import json
from gtts import gTTS

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Typing Game')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Set fonts, ensuring support for Chinese and phonetics
font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"  # macOS Arial Unicode font path
font = pygame.font.Font(font_path, 36)
small_font = pygame.font.Font(font_path, 24)

# Load sentence library from file
with open("sentence_list.json", "r", encoding="utf-8") as file:
    sentence_list = json.load(file)

# Initialize proficiency set
proficient_sentences = set()


def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("current_sentence.mp3")
    pygame.mixer.music.load("current_sentence.mp3")
    pygame.mixer.music.play()


def speak_word(word, lang='en'):
    tts = gTTS(text=word, lang=lang)
    tts.save("current_word.mp3")
    pygame.mixer.music.load("current_word.mp3")
    pygame.mixer.music.play()


# Choose a random sentence and its translation and phonetics
def choose_sentence():
    while True:
        current_sentence_data = random.choice(sentence_list)
        current_sentence = current_sentence_data["sentence"]
        if current_sentence not in proficient_sentences:
            return current_sentence_data


current_sentence_data = choose_sentence()
current_sentence = current_sentence_data["sentence"]
current_translation = current_sentence_data["translation"]
current_phonetics = current_sentence_data["phonetics"]
typed_sentence = ""

# Play audio
speak(current_sentence)

# Timer
start_ticks = pygame.time.get_ticks()

# Continuous delete interval (milliseconds)
delete_interval = 100
last_delete_time = 0

# Word position lists
word_positions = []

# Button
button_rect = pygame.Rect((screen_width // 2 - 50, screen_height - 100, 100, 50))

# Cooldown settings
cooldown_time = 1000  # milliseconds
last_click_time = 0

def draw_text_with_phonetics(text, phonetics, font, small_font, color, surface, x, y, max_width):
    words = text.split(' ')
    current_width = 0

    word_positions.clear()

    for i, word in enumerate(words):
        word_surface = font.render(word, True, color)
        word_width, word_height = word_surface.get_size()
        phonetic = phonetics[i] if i < len(phonetics) else ""
        phonetic_surface = small_font.render(phonetic, True, color)
        phonetic_width, phonetic_height = phonetic_surface.get_size()

        if current_width + word_width >= max_width:
            y += word_height + phonetic_height
            current_width = 0

        surface.blit(word_surface, (x + current_width, y))
        surface.blit(phonetic_surface, (x + current_width, y + word_height))

        word_positions.append((word, x + current_width, y, word_width, word_height))

        current_width += word_width + font.size(' ')[0]


def draw_text_multiline(text, font, color, surface, x, y, max_width):
    words = text.split(' ')
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_surface = font.render(word, True, color)
        word_width, word_height = word_surface.get_size()
        if current_width + word_width >= max_width:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width
        else:
            current_line.append(word)
            current_width += word_width + font.size(' ')[0]

    if current_line:
        lines.append(' '.join(current_line))

    for i, line in enumerate(lines):
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (x, y + i * word_height))

    return lines  # Return each line of text for later use


def get_text_lines(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_surface = font.render(word, True, (0, 0, 0))  # color doesn't matter here
        word_width, word_height = word_surface.get_size()
        if current_width + word_width >= max_width:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width
        else:
            current_line.append(word)
            current_width += word_width + font.size(' ')[0]

    if current_line:
        lines.append(' '.join(current_line))

    return lines


# Main game loop
running = True
delete_key_held = False

while running:
    screen.fill(black)

    current_time = pygame.time.get_ticks()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_RETURN:
                if typed_sentence == current_sentence:
                    current_sentence_data = choose_sentence()
                    current_sentence = current_sentence_data["sentence"]
                    current_translation = current_sentence_data["translation"]
                    current_phonetics = current_sentence_data["phonetics"]
                    typed_sentence = ""
                    start_ticks = pygame.time.get_ticks()  # Reset timer
                    speak(current_sentence)
            elif event.key == pygame.K_BACKSPACE:
                delete_key_held = True
                if typed_sentence:
                    typed_sentence = typed_sentence[:-1]
                    last_delete_time = current_time
            else:
                typed_sentence += event.unicode
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                delete_key_held = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if button_rect.collidepoint(mouse_x, mouse_y):
                if current_time - last_click_time > cooldown_time:
                    proficient_sentences.add(current_sentence)
                    # Save the proficient sentences to file
                    with open("proficient_sentences.json", "a", encoding="utf-8") as file:
                        file.write(current_sentence + "\n")

                    # Remove the current sentence from the sentence list
                    sentence_list = [sentence for sentence in sentence_list if sentence["sentence"] != current_sentence]
                    # Save the updated sentence list to file
                    with open("sentence_list.json", "w", encoding="utf-8") as file:
                        json.dump(sentence_list, file, ensure_ascii=False, indent=4)

                    current_sentence_data = choose_sentence()
                    current_sentence = current_sentence_data["sentence"]
                    current_translation = current_sentence_data["translation"]
                    current_phonetics = current_sentence_data["phonetics"]
                    typed_sentence = ""
                    start_ticks = pygame.time.get_ticks()  # Reset timer
                    speak(current_sentence)
                    last_click_time = current_time
            else:
                for word, word_x, word_y, word_width, word_height in word_positions:
                    if word_x <= mouse_x <= word_x + word_width and word_y <= mouse_y <= word_y + word_height:
                        speak_word(word)
                        break

    # Continuous delete handling
    if delete_key_held and current_time - last_delete_time >= delete_interval:
        if typed_sentence:
            typed_sentence = typed_sentence[:-1]
            last_delete_time = current_time

    # Draw current sentence, phonetics, and translation
    draw_text_with_phonetics(current_sentence, current_phonetics, font, small_font, white, screen, 20, 20, screen_width - 40)
    draw_text_multiline(current_translation, small_font, white, screen, 20, 220, screen_width - 40)  # Move translation down

    # Get text lines of the current sentence
    sentence_lines = get_text_lines(current_sentence, font, screen_width - 40)
    # Draw typed sentence in the same way
    draw_text_multiline(typed_sentence, font, white, screen, 20, 300, screen_width - 40)  # Move player input down

    # Draw button
    pygame.draw.rect(screen, green, button_rect)
    button_text = small_font.render('Proficiently', True, black)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

    # Draw timer
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    draw_text_multiline(f"Time: {seconds:.2f}", small_font, white, screen, 20, 480, screen_width - 40)  # Move timer down

    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Save proficient sentences to a file
with open("proficient_sentences.json", "w", encoding="utf-8") as file:
    for sentence in proficient_sentences:
        file.write(sentence + "\n")

# Delete generated audio files
if os.path.exists("current_sentence.mp3"):
    os.remove("current_sentence.mp3")
if os.path.exists("current_word.mp3"):
    os.remove("current_word.mp3")
import pygame
import random
import sys
import os
import json
from gtts import gTTS

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Typing Game')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Set fonts, ensuring support for Chinese and phonetics
font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"  # macOS Arial Unicode font path
font = pygame.font.Font(font_path, 36)
small_font = pygame.font.Font(font_path, 24)

# Load sentence library from file
with open("sentence_list.json", "r", encoding="utf-8") as file:
    sentence_list = json.load(file)

# Initialize proficiency set
proficient_sentences = set()


def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("current_sentence.mp3")
    pygame.mixer.music.load("current_sentence.mp3")
    pygame.mixer.music.play()


def speak_word(word, lang='en'):
    tts = gTTS(text=word, lang=lang)
    tts.save("current_word.mp3")
    pygame.mixer.music.load("current_word.mp3")
    pygame.mixer.music.play()


# Choose a random sentence and its translation and phonetics
def choose_sentence():
    while True:
        current_sentence_data = random.choice(sentence_list)
        current_sentence = current_sentence_data["sentence"]
        if current_sentence not in proficient_sentences:
            return current_sentence_data


current_sentence_data = choose_sentence()
current_sentence = current_sentence_data["sentence"]
current_translation = current_sentence_data["translation"]
current_phonetics = current_sentence_data["phonetics"]
typed_sentence = ""

# Play audio
speak(current_sentence)

# Timer
start_ticks = pygame.time.get_ticks()

# Continuous delete interval (milliseconds)
delete_interval = 100
last_delete_time = 0

# Word position lists
word_positions = []

# Button
button_rect = pygame.Rect((screen_width // 2 - 50, screen_height - 100, 100, 50))

# Cooldown settings
cooldown_time = 1000  # milliseconds
last_click_time = 0

def draw_text_with_phonetics(text, phonetics, font, small_font, color, surface, x, y, max_width):
    words = text.split(' ')
    current_width = 0

    word_positions.clear()

    for i, word in enumerate(words):
        word_surface = font.render(word, True, color)
        word_width, word_height = word_surface.get_size()
        phonetic = phonetics[i] if i < len(phonetics) else ""
        phonetic_surface = small_font.render(phonetic, True, color)
        phonetic_width, phonetic_height = phonetic_surface.get_size()

        if current_width + word_width >= max_width:
            y += word_height + phonetic_height
            current_width = 0

        surface.blit(word_surface, (x + current_width, y))
        surface.blit(phonetic_surface, (x + current_width, y + word_height))

        word_positions.append((word, x + current_width, y, word_width, word_height))

        current_width += word_width + font.size(' ')[0]


def draw_text_multiline(text, font, color, surface, x, y, max_width):
    words = text.split(' ')
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_surface = font.render(word, True, color)
        word_width, word_height = word_surface.get_size()
        if current_width + word_width >= max_width:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width
        else:
            current_line.append(word)
            current_width += word_width + font.size(' ')[0]

    if current_line:
        lines.append(' '.join(current_line))

    for i, line in enumerate(lines):
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (x, y + i * word_height))

    return lines  # Return each line of text for later use


def get_text_lines(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_surface = font.render(word, True, (0, 0, 0))  # color doesn't matter here
        word_width, word_height = word_surface.get_size()
        if current_width + word_width >= max_width:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width
        else:
            current_line.append(word)
            current_width += word_width + font.size(' ')[0]

    if current_line:
        lines.append(' '.join(current_line))

    return lines


# Main game loop
running = True
delete_key_held = False

while running:
    screen.fill(black)

    current_time = pygame.time.get_ticks()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_RETURN:
                if typed_sentence == current_sentence:
                    current_sentence_data = choose_sentence()
                    current_sentence = current_sentence_data["sentence"]
                    current_translation = current_sentence_data["translation"]
                    current_phonetics = current_sentence_data["phonetics"]
                    typed_sentence = ""
                    start_ticks = pygame.time.get_ticks()  # Reset timer
                    speak(current_sentence)
            elif event.key == pygame.K_BACKSPACE:
                delete_key_held = True
                if typed_sentence:
                    typed_sentence = typed_sentence[:-1]
                    last_delete_time = current_time
            else:
                typed_sentence += event.unicode
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                delete_key_held = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if button_rect.collidepoint(mouse_x, mouse_y):
                if current_time - last_click_time > cooldown_time:
                    proficient_sentences.add(current_sentence)
                    # Save the proficient sentences to file
                    with open("proficient_sentences.json", "a", encoding="utf-8") as file:
                        file.write(current_sentence + "\n")

                    # Remove the current sentence from the sentence list
                    sentence_list = [sentence for sentence in sentence_list if sentence["sentence"] != current_sentence]
                    # Save the updated sentence list to file
                    with open("sentence_list.json", "w", encoding="utf-8") as file:
                        json.dump(sentence_list, file, ensure_ascii=False, indent=4)

                    current_sentence_data = choose_sentence()
                    current_sentence = current_sentence_data["sentence"]
                    current_translation = current_sentence_data["translation"]
                    current_phonetics = current_sentence_data["phonetics"]
                    typed_sentence = ""
                    start_ticks = pygame.time.get_ticks()  # Reset timer
                    speak(current_sentence)
                    last_click_time = current_time
            else:
                for word, word_x, word_y, word_width, word_height in word_positions:
                    if word_x <= mouse_x <= word_x + word_width and word_y <= mouse_y <= word_y + word_height:
                        speak_word(word)
                        break

    # Continuous delete handling
    if delete_key_held and current_time - last_delete_time >= delete_interval:
        if typed_sentence:
            typed_sentence = typed_sentence[:-1]
            last_delete_time = current_time

    # Draw current sentence, phonetics, and translation
    draw_text_with_phonetics(current_sentence, current_phonetics, font, small_font, white, screen, 20, 20, screen_width - 40)
    draw_text_multiline(current_translation, small_font, white, screen, 20, 220, screen_width - 40)  # Move translation down

    # Get text lines of the current sentence
    sentence_lines = get_text_lines(current_sentence, font, screen_width - 40)
    # Draw typed sentence in the same way
    draw_text_multiline(typed_sentence, font, white, screen, 20, 300, screen_width - 40)  # Move player input down

    # Draw button
    pygame.draw.rect(screen, green, button_rect)
    button_text = small_font.render('Proficiently', True, black)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

    # Draw timer
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    draw_text_multiline(f"Time: {seconds:.2f}", small_font, white, screen, 20, 480, screen_width - 40)  # Move timer down

    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Save proficient sentences to a file
with open("proficient_sentences.json", "w", encoding="utf-8") as file:
    for sentence in proficient_sentences:
        file.write(sentence + "\n")

# Delete generated audio files
if os.path.exists("current_sentence.mp3"):
    os.remove("current_sentence.mp3")
if os.path.exists("current_word.mp3"):
    os.remove("current_word.mp3")
