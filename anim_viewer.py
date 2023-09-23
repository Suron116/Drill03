from pico2d import *

open_canvas()

character = load_image('chr.png')
x = 0
frame = 0
while (x < 750):
    clear_canvas()                  
    character.clip_draw(frame * 5, 0, 25, 80, x, 90)
    update_canvas()
    frame = (frame + 1) % 7 
    x += 5
    delay(0.01)
    get_events()

close_canvas()