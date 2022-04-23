def create_gaussian_pyramid(image, levels):
    '''
    Creates a Gaussian pyramid for each image.
    :param image: An image, i.e video frame
    :param levels: The Gaussian pyramid level
    :return: Returns a pyramid of nr. levels images
    '''
    gauss = image.copy()
    gauss_pyr = [gauss]

    for level in range(1, levels):
        gauss = cv2.pyrDown(gauss)
        gauss_pyr.append(gauss)

    return gauss_pyr
