def heading(text, h=1):
    if h < 1:
        h = 1
    if h > 6:
        h = 6
    return f"{'#' * h} {text}"
