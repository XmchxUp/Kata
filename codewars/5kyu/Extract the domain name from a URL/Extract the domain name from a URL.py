def domain_name(url):
    replaces = [
        "http://",
        "https://",
        "www.",
    ]
    for r in replaces:
        url = url.replace(r, "")
    return url.split(".")[0]
