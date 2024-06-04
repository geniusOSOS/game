import pygame
import random
import sys
import os
import json
from gtts import gTTS

# 初始化 Pygame
pygame.init()
pygame.mixer.init()

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Typing Game')

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)

# 设置字体，确保使用支持中文和音标的字体
font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"  # macOS中的Arial Unicode字体路径
font = pygame.font.Font(font_path, 36)
small_font = pygame.font.Font(font_path, 24)

# 从文件中读取句子库
with open("sentence_list.json", "r", encoding="utf-8") as file:
    sentence_list = json.load(file)


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


# 选择一个随机句子及其翻译和音标
current_sentence_data = random.choice(sentence_list)
current_sentence = current_sentence_data["sentence"]
current_translation = current_sentence_data["translation"]
current_phonetics = current_sentence_data["phonetics"]
typed_sentence = ""

# 播放音频
speak(current_sentence)

# 计时器
start_ticks = pygame.time.get_ticks()

# 连续删除间隔时间（毫秒）
delete_interval = 100
last_delete_time = 0

# 单词位置列表
word_positions = []


def draw_text_with_phonetics(text, phonetics, font, small_font, color, surface, x, y, max_width):
    words = text.split(' ')
    lines = []
    phonetic_lines = []
    current_line = []
    current_phonetic_line = []
    current_width = 0

    word_positions.clear()

    for i, word in enumerate(words):
        word_surface = font.render(word, True, color)
        word_width, word_height = word_surface.get_size()
        phonetic = phonetics[i] if i < len(phonetics) else ""
        phonetic_surface = small_font.render(phonetic, True, color)
        phonetic_width, phonetic_height = phonetic_surface.get_size()

        if current_width + word_width >= max_width:
            lines.append(current_line)
            phonetic_lines.append(current_phonetic_line)
            current_line = [word_surface]
            current_phonetic_line = [phonetic_surface]
            current_width = word_width
        else:
            current_line.append(word_surface)
            current_phonetic_line.append(phonetic_surface)
            current_width += word_width + font.size(' ')[0]

        word_positions.append((word, x + current_width - word_width, y, word_width, word_height))

    if current_line:
        lines.append(current_line)
        phonetic_lines.append(current_phonetic_line)

    y_offset = y
    for line, phonetic_line in zip(lines, phonetic_lines):
        max_line_height = max([surf.get_height() for surf in line])
        max_phonetic_height = max([surf.get_height() for surf in phonetic_line])
        for word_surface, phonetic_surface in zip(line, phonetic_line):
            surface.blit(word_surface, (x, y_offset))
            surface.blit(phonetic_surface, (x, y_offset + max_line_height))
            x += word_surface.get_width() + font.size(' ')[0]
        y_offset += max_line_height + max_phonetic_height
        x = 20


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

    return lines  # 返回每行文本以便后续使用


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


# 游戏主循环
running = True
delete_key_held = False

while running:
    screen.fill(black)

    current_time = pygame.time.get_ticks()

    # 事件处理
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
                    current_sentence_data = random.choice(sentence_list)
                    current_sentence = current_sentence_data["sentence"]
                    current_translation = current_sentence_data["translation"]
                    current_phonetics = current_sentence_data["phonetics"]
                    typed_sentence = ""
                    start_ticks = pygame.time.get_ticks()  # 重置计时器
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
            for word, word_x, word_y, word_width, word_height in word_positions:
                if word_x <= mouse_x <= word_x + word_width and word_y <= mouse_y <= word_y + word_height:
                    speak_word(word)
                    break

    # 连续删除处理
    if delete_key_held and current_time - last_delete_time >= delete_interval:
        if typed_sentence:
            typed_sentence = typed_sentence[:-1]
            last_delete_time = current_time

    # 绘制当前句子及其音标和翻译
    draw_text_with_phonetics(current_sentence, current_phonetics, font, small_font, white, screen, 20, 20,
                             screen_width - 40)
    draw_text_multiline(current_translation, small_font, white, screen, 20, 220, screen_width - 40)  # 将中文翻译的位置往下移动

    # 获取当前句子的分行
    sentence_lines = get_text_lines(current_sentence, font, screen_width - 40)
    # 按相同方式绘制已输入的句子
    draw_text_multiline(typed_sentence, font, white, screen, 20, 300, screen_width - 40)  # 将玩家输入的位置往下移动

    # 绘制计时器
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    draw_text_multiline(f"Time: {seconds:.2f}", small_font, white, screen, 20, 480, screen_width - 40)  # 将时间位置往下移动

    pygame.display.flip()
    pygame.time.Clock().tick(60)

# 删除生成的音频文件
if os.path.exists("current_sentence.mp3"):
    os.remove("current_sentence.mp3")
if os.path.exists("current_word.mp3"):
    os.remove("current_word.mp3")
