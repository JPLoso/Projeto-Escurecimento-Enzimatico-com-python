import numpy as np

def calc_percentuais(region_mask, region_gray):
    pixels_validos = region_gray[region_mask > 0]

    if len(pixels_validos) == 0:
        return (0, 0, 0)

    escuros = np.sum(pixels_validos <= 85)
    medios = np.sum((pixels_validos > 85) & (pixels_validos <= 170))
    claros = np.sum(pixels_validos > 170)

    total = len(pixels_validos)

    return (
        escuros / total * 100,
        medios / total * 100,
        claros / total * 100
    )