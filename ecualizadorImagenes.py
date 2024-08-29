import cv2

# Leer la imagen
im = cv2.imread("C:/Users/Asus/Desktop/proyecto/imagen4.jpg")

# Verificar si la imagen se cargó correctamente
if im is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta del archivo.")
else:
    # Convertir la imagen de BGR a HSV
    imhsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

    # Ecualizar el histograma del canal V (Valor)
    imhsv[:, :, 2] = cv2.equalizeHist(imhsv[:, :, 2])

    # Convertir la imagen de HSV de vuelta a BGR
    imEq = cv2.cvtColor(imhsv, cv2.COLOR_HSV2BGR)

    beta = 10
    imBright = cv2.convertScaleAbs(imEq, beta=beta)

    # Guardar la imagen ecualizada
    #cv2.imwrite('C:/Users/Asus/Desktop/proyecto/ImgsEcualizada/imagenEcualizada4.jpg', imEq)
    cv2.imwrite('C:/Users/Asus/Desktop/proyecto/ImgsBrillo/imagenBrillo4.jpg', imBright)

    print("Imagen ecualizada guardada como 'imagen_ecualizada4.jpg'.")


