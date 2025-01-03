import csv

#file = input('Enter the name of the playlist file:')
file = 'C:/Users/Pbknowall/Desktop/Liked Songs - Skiley Export.csv'
if file.endswith('.csv'):
    with open(file, 'r', encoding="utf8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        jsonData = rows
else: jsonData = open(file()).read()

def proofCheckTrackInfo(data):
    keyVariations = {
            "trackName": ["trackname", "track name", "name"],
            "artistName": ["artistname", "artist name", "artist"],
            "duration": ["duration", "length", "time"]
        }
    normalisedKeys = {key.lower().replace(" ", ""): value for key, value in data.items()}
    missingKeys = []

    for canKey, variations in keyVariations.items():
        if not any(var in normalisedKeys for var in variations):
            missingKeys.append(canKey)
    
    if missingKeys:
        return False, missingKeys
    return True

res = proofCheckTrackInfo(jsonData[0])
if len(res[1]) > 0 and 'duration' not in res[1]:
    print('The following keys are missing from the file provided:', ', '.join(res[1]))
else:
    if len(res[1]) > 0:
        print('***Duration is not a key in the file provided, meaning some media players may not support the m3u8 to be created***\n***Proper synchronisation and seemless playback may not be possible and the playlist\'s total duration may not be displayed***')

    #name = file.split('/')[-1].split('.')[0] if file.count('/')>file.count('\\') else file.split('\\')[-1].split('.')[0]
    with open(file.replace('.csv', '.m3u8').replace('.json', '.m3u8'), 'w') as f:
        f.write('#EXTM3U\n')
        for track in jsonData:
            duration = track.get("duration", -1)
            print(duration)
            f.write(f'#EXTINF:{duration},{track["artistName"]} - {track["trackName"]}\n') # Implement different formats
            #f.write(f'{track["trackUrl"]}\n')