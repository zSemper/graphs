# Imports
import numpy as np
import plotly.graph_objects as go
from scipy.ndimage import gaussian_filter

########################
# Control
x_size = 50
y_size = 50
seed = 42
smoothness = 7.0
# Used in LLM1.png = 1.0
# Used in LLM2.png = 4.0
# Used in LLM3.png = 7.0
########################

# Generates noise based on smoothness value
def generate_smooth_noise():
    # Set seed = 42
    np.random.seed(seed)

    # Generate random noise
    raw_noise = np.random.rand(y_size, x_size)

    # Apply Gaussian smoothing (higher smoothness = smoother)
    smoothed_noise = gaussian_filter(raw_noise, sigma=smoothness)

    # Normalize to range between 0 and 1
    z_min, z_max = smoothed_noise.min(), smoothed_noise.max()
    normalized_noise = (smoothed_noise - z_min) / (z_max - z_min)

    return normalized_noise

# Generates 3D Plot
def plot_3d_surface(z):
    x = np.arange(0, x_size)
    y = np.arange(0, y_size)
    x_grid, y_grid = np.meshgrid(x, y)

    # Create graph figure
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis', colorbar=dict(title="Parameter Werte"))])
    fig.update_layout(
        title='Simple Darstellung für ein LLM',
        scene=dict(
            xaxis_title='X Achse',
            yaxis_title='Y Achse',
            zaxis_title='Z Achse',
            zaxis=dict(range=[0, 1])
        )
    )
    fig.show()

# Generate graph
z = generate_smooth_noise()
plot_3d_surface(z)
