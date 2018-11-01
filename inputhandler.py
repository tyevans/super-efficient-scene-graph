import cv2


class InputHandler(object):

    def step(self):
        inkey = cv2.waitKey(1) & 0xFF
        print(inkey)

        if inkey == ord('q'):
            pass
            # cv2.destroyAllWindows()
            # break

        # elif inkey == ord('a'):
        #     viewport.transform.x -= 1
        # elif inkey == ord('d'):
        #     viewport.transform.x += 1
        # elif inkey == ord('w'):
        #     viewport.transform.y -= 1
        # elif inkey == ord('s'):
        #     viewport.transform.y += 1