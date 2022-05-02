import matplotlib.pyplot as plt

def floodfill(img, x, y):
    if x < 0 or y < 0 or x > (img.shape[0] -1) or y > (img.shape[1] -1):
        return img
    if img[x, y] != 1:
        return img
    plt.imshow(img, "gray")
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()
    img[x ,y] = 2
    img = floodfill(img, x - 1, y)
    img = floodfill(img, x + 1, y)
    img = floodfill(img, x, y + 1)
    img = floodfill(img, x, y - 1)
    return img


def main():
    # img = plt.imread("files/img0.png")[:, :, 0]
    img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    img = floodfill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show()




if __name__ == "__main__":
    main()
