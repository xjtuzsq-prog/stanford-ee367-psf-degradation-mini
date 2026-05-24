import numpy as np
import matplotlib.pyplot as plt

#生成defocus PSF
def defocus_psf(size, radius):
    """生成defocus PSF"""
    x = np.arange(-size//2 + 1, size//2 + 1)
    y = np.arange(-size//2 + 1, size//2 + 1)
    x, y = np.meshgrid(x, y)
    r = np.sqrt(x**2 + y**2)
    psf = (r <= radius).astype(float)
    psf /= psf.sum()  # 归一化
    return psf


#生成高斯PSF
def gaussian_psf(size, sigma):
    """生成高斯PSF"""
    x = np.arange(-size//2 + 1, size//2 + 1)
    y = np.arange(-size//2 + 1, size//2 + 1)
    x, y = np.meshgrid(x, y)
    psf = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    psf /= psf.sum()  # 归一化
    return psf