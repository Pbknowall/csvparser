import csv

#file = input('Enter the name of the playlist file:')
file = 'D:/Music/iTunes/Playlists/house.csv'
fileFormat = 'mp3'
if file.endswith('.csv'):
    with open(file, 'r', encoding="utf8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        jsonData = rows
else: jsonData = open(file()).read()

def proofCheckTrackInfo(data):
    keyVariations = {
            "trackName": ["trackname", "name"],
            "artistName": ["artistname", "artist", "artistname(s)"],
            "duration": ["duration", "length", "time", "duration(ms)"]
        }
    normalisedData = []
    for element in data:
        normalisedData.append({key.lower().replace(" ", ""): value for key, value in element.items()})
    missingKeys = []
    for canKey, variations in keyVariations.items():
        if not any(var in normalisedData[0] for var in variations):
            missingKeys.append(canKey)

    for canKey, variations in keyVariations.items():
        for variation in variations:
            for element in normalisedData:
                if variation in element:
                    element[canKey] = element.pop(variation)
    
    if missingKeys:
        return False, normalisedData, missingKeys
    return (True, normalisedData, [])



res = proofCheckTrackInfo(jsonData)
print(res)

if len(res[2]) > 1 or (len(res[2]) > 0 and 'duration' not in res[2]):
    print('The following keys are missing from the file provided:', ', '.join(res[2]))
else:
    if 'duration' in res[2]:
        print('***Duration is not a key in the file provided, meaning some media players may not support the m3u8 to be created***\n***Proper synchronisation and seemless playback may not be possible and the playlist\'s total duration may not be displayed***')
    #name = file.split('/')[-1].split('.')[0] if file.count('/')>file.count('\\') else file.split('\\')[-1].split('.')[0]
    with open(file.replace('.csv', '.m3u8').replace('.json', '.m3u8'), 'w') as f:
        f.write('#EXTM3U\n')
        for track in res[1]:
            #print(track)
            duration = track.get("duration", -1)
            #print(duration)
            f.write(f'#EXTINF:{duration if int(duration)<1000 else int(int(duration)/1000)},{track["artistName"]} - {track["trackName"]}\n') # Implement different formats
            f.write(f'{track["trackName"]}.{fileFormat}\n')