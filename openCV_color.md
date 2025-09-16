# Why No Tuple?

A tuple (255, 255, 255) would be used for a BGR (Blue, Green, Red) image, which has three channels. Your code is likely operating on a single-channel, grayscale image, where the color is defined by a single integer from 0 to 255.

OpenCV automatically detects the number of channels in the input image and interprets the color argument accordingly:

    If your img is a 3-channel BGR image, you must use a tuple for the color, such as (255, 255, 255) for white.

    If your img is a single-channel grayscale image, you must use a single integer for the color, where 255 is white.

If you try to use a tuple (255, 255, 255) with a single-channel image, you will get an error because the number of color values doesn't match the number of channels in the image.