import http.client

def get(your_sign):
    conn = http.client.HTTPConnection("horoscope4.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "38687d25a0mshe69cebd42ff34fcp1cbaf4jsnb6447ddd4038",
        'x-rapidapi-host': "horoscope4.p.rapidapi.com"
    }

    conn.request("GET", "/api/v1/horoscope/"+your_sign+"/day/", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))