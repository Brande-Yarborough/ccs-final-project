import discogs_client
d = discogs_client.Client('ExampleApplication/0.1',
                          user_token="AhPySnZsfOSbHSygKTMUmTGyWvQwGJvyfhYgDRoC")


def fetchDiscOgsData():
    type = 'release'
    title = ''
    artist = 'Beyonce'
    genre = ''
    year = ''
    results = d.search(artist=artist, type=type)
    print(results[0])
    return results


fetchDiscOgsData()


# determining what information coming back based on parameters
