import pygame
from checkAI import dineout, get_ai_response

pygame.init()
screen = pygame.display.set_mode((1000, 700))
font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 36)

questions = ["Nights Budget", "City/Town", "Neighborhood", "Type of food", "Time of day"]
answers = [""] * len(questions)
current_q = 0
input_box = pygame.Rect(100, 100, 600, 32)
output_box = pygame.Rect(100, 200, 800, 400)  # Output area for AI response
color = pygame.Color('lightskyblue3')
output_color = pygame.Color('darkgreen')
active = True
text = ''
ai_response = ''
show_response = False

def wrap_text(text, font, max_width):
    """Wrap text to fit within the specified width"""
    words = text.split(' ')
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        if font.size(test_line)[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                lines.append(word)  # Single word longer than max_width
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

running = True
while running:
    screen.fill((30, 30, 30))
    
    if not show_response:
        # Show question and input
        question_surface = title_font.render(f"Question {current_q + 1}: {questions[current_q]}", True, (255, 255, 255))
        screen.blit(question_surface, (100, 50))
        
        txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        
        # Show progress
        progress_text = f"Progress: {current_q + 1}/{len(questions)}"
        progress_surface = font.render(progress_text, True, (200, 200, 200))
        screen.blit(progress_surface, (100, 150))
    else:
        # Show AI response
        title_surface = title_font.render("AI Travel Recommendations:", True, (255, 255, 255))
        screen.blit(title_surface, (100, 50))
        
        # Draw output box
        pygame.draw.rect(screen, (50, 50, 50), output_box)
        pygame.draw.rect(screen, output_color, output_box, 2)
        
        # Wrap and display the AI response
        wrapped_lines = wrap_text(ai_response, font, output_box.width - 20)
        
        y_offset = 20
        for line in wrapped_lines[:15]:  # Limit to 15 lines to fit in box
            line_surface = font.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (output_box.x + 10, output_box.y + y_offset))
            y_offset += 25
        
        # Show instruction to close
        instruction_surface = font.render("Press ESC to close or SPACE to ask another question", True, (200, 200, 200))
        screen.blit(instruction_surface, (100, 620))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not show_response:
                if event.key == pygame.K_RETURN:
                    answers[current_q] = text
                    text = ''
                    current_q += 1
                    if current_q >= len(questions):
                        prompt = dineout(answers)
                        ai_response = get_ai_response(prompt)
                        show_response = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            else:
                # When showing response
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    # Reset for new questions
                    current_q = 0
                    answers = [""] * len(questions)
                    text = ''
                    ai_response = ''
                    show_response = False

    pygame.display.flip()

pygame.quit()