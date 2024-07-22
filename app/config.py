import scholarly

def configure_proxy():
    proxies = {
        "http": "http://your_luminati_proxy",
        "https": "http://your_luminati_proxy",
    }
    scholarly.use_proxy(proxies)
