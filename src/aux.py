import numpy as np

def zero_pad(matrix):
    m = matrix.reshape((matrix.shape[0], -1))
    padded = 0 * np.ones(2 * [max(m.shape)], dtype=m.dtype)
    padded[0:m.shape[0], 0:m.shape[1]] = m
    return padded

def haversine_scalar(coord1: tuple, coord2: tuple) -> float:
    """
    Calculate the Haversine distance between two points on the Earth.

    Parameters:
    - coord1: tuple (lat1, lon1) in degrees
    - coord2: tuple (lat2, lon2) in degrees

    Returns:
    - Distance in kilometers
    """
    # Convert degrees to radians
    lat1, lon1 =coord1.as_tuple()
    lat2, lon2 = coord2.as_tuple()

    lat1, lon1 = np.radians((lat1, lon1))
    lat2, lon2 = np.radians((lat2, lon2))

    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    # Earth's radius in kilometers
    R = 6371.0
    return R * c  # [km]


def haversine_vector(coords1: np.ndarray, coords2: np.ndarray) -> np.ndarray:
    lat1, lon1 = np.radians(coords1[:, 0]), np.radians(coords1[:, 1])
    lat2, lon2 = np.radians(coords2[:, 0]), np.radians(coords2[:, 1])

    dlat = lat2[:, np.newaxis] - lat1
    dlon = lon2[:, np.newaxis] - lon1

    a = (
        np.sin(dlat / 2)**2
        + np.cos(lat1) * np.cos(lat2)[:, np.newaxis] * np.sin(dlon / 2)**2
    )
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    R = 6371.0
    return R * c  # [km]

def get_distance_matrix(v1, v2):
    v1_array = np.array([coord.as_tuple() for coord in v1])
    v2_array = np.array([coord.as_tuple() for coord in v2])
    
    distance_matrix = cdist(v1_array, v2_array, metric=lambda u, v: haversine_vector(np.array([u]), np.array([v]))[0])
    return distance_matrix