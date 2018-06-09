import cv2
import numpy as np


class ClusterToTxt():
    def __init__(self):
        pass

    def show_image_and_wait(self, img):
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_points_and_targets(self, img_path):
        img = cv2.imread(img_path)
        rows, cols, _ = img.shape
    
        pixels = {}
        unique_targets = set()
        data_raw = {}

        for r in range(rows):
            for pixel in range(cols):
                tup = tuple(img[r][pixel])
                if tup != tuple([255,255,255]): # do not count white (background color) as target
                     unique_targets.add(tup)
                     data_raw["{},{}".format(r, pixel)] = tup

    
        num_clusters = len(unique_targets)
        #print("{}\nNumber of points: {}".format(data_raw, len(data_raw)))
        return data_raw, unique_targets


    def convert_color_to_int(self, target, targets):
        return targets.index(target)


    def create_data_file(self, filename, points, targets):
        with open(filename, "w") as f:
            for point, target in points.items():
                target = self.convert_color_to_int(target, targets)
                f.write("{},{}\n".format(point, target))


def main():
    converter = ClusterToTxt()
    path = 'images/test_3_colors.png'
    p, t = converter.get_points_and_targets(path)
    
    converter.create_data_file("datasets/test_3_colors.txt", p, list(t))
    print("done")

if __name__ == "__main__":
    main()