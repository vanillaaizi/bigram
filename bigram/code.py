import random
import pygame
#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Bigram Table")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
font = pygame.font.SysFont('Arial', 20)
def draw_cell(surface, x, y, width, height, text):
    pygame.draw.rect(surface, BLACK, (x, y, width, height), 1)
    text_surface = font.render(text, True, BLACK)
    surface.blit(text_surface, (x + 5, y + 5))
draw_cell(screen, 50, 50, 100, 50, "First letter")
draw_cell(screen, 150, 50, 100, 50, "Second letter")
draw_cell(screen, 250, 50, 100, 50, "Probability")
#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
def read_names(filename):
    with open(filename, 'r') as f:
        names = f.read().splitlines()
    return names
def build_bigram_model(names):
    bigrams = {}
    for name in names:
        for i in range(len(name)-1):
            bigram = name[i:i+2]
            if bigram in bigrams:
                bigrams[bigram] += 1
            else:
                bigrams[bigram] = 1
    total_bigrams = sum(bigrams.values())
    for bigram, count in bigrams.items():
        bigrams[bigram] = count / total_bigrams
    return bigrams
def generate_name(bigrams):
    first_letter_options = [bigram[0] for bigram in bigrams.keys()]
    first_letter = random.choice(first_letter_options)
    name = first_letter
    while True:
        last_letter = name[-1]
        possible_bigrams = [bigram for bigram in bigrams.keys() if bigram[0] == last_letter]
        if not possible_bigrams:
            break
        probabilities = [bigrams[bigram] for bigram in possible_bigrams]
        chosen_bigram = random.choices(possible_bigrams, probabilities)[0]
        name += chosen_bigram[1]
    return name
if __name__ == '__main__':
    names = read_names('names.txt')
    bigrams = build_bigram_model(names)
    print(bigrams)
    for i in range(10):
        print(generate_name(bigrams))
#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
first_letters = [bigram[0] for bigram in bigrams.keys()]
second_letters = [bigram[1] for bigram in bigrams.keys()]
probabilities = list(bigrams.values())
for i in range(len(first_letters)):
    draw_cell(screen, 50, 100 + i * 25, 100, 25, first_letters[i])
    draw_cell(screen, 150, 100 + i * 25, 100, 25, second_letters[i])
    draw_cell(screen, 250, 100 + i * 25, 100, 25, str(round(probabilities[i], 4)))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

