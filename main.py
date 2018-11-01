import time

import cv2

from actor import SquareActor
from charts import Bar
from inputhandler import InputHandler
from stage import Stage
from viewport import ViewPort
from webcam import WebcamActor

if __name__ == "__main__":
    stage = Stage()

    # actor = SquareActor()
    # stage.add_actor(actor)

    # input_handler = InputHandler()
    # webcam_actor = WebcamActor()
    # stage.add_actor(webcam_actor)

    bar = Bar(20, 100, 100, 50)
    stage.add_actor(bar)
    bar.height.set_value(300)

    viewport = ViewPort(stage, 1024, 768)
    # viewport.center_on(bar)

    last_tick = time.time()
    draw_rate = 1 / 15
    draw_timer = 0
    while True:
        tick = time.time()
        delta = tick - last_tick
        last_tick = tick

        stage.step(delta)
        draw_timer -= delta
        if draw_timer <= 0:
            draw_timer += draw_rate

            viewport.clear()
            stage.draw(viewport)

            cv2.imshow("Frame", viewport.canvas)

        try:
            raw_key = cv2.waitKey(1)
            in_key = raw_key & 0xFF
            if raw_key == -1:
                continue

            # print(in_key, raw_key, chr(in_key))
            if in_key == ord('q'):
                cv2.destroyAllWindows()
                break

            elif in_key == ord('a'):
                viewport.transform.x -= 1
            elif in_key == ord('d'):
                viewport.transform.x += 1
            elif in_key == ord('w'):
                viewport.transform.y -= 1
            elif in_key == ord('s'):
                viewport.transform.y += 1

        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            raise
