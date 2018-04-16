import csv


def remove_feature(artist):
	index = artist.find("feat")
	artist_trim = artist
	if index > -1:
		artist_trim = artist[:index-1]
	return artist_trim

def det_decade(year):
	year = int(year)
	if year < 1970:
		return str(1960)
	if year <1980:
		return str(1970)
	if year < 1990:
		return str(1980)
	if year < 2000:
		return str(1990)
	if year < 2010:
		return str(2000)
	else:
		return str(2010)

def write_to_csv(final_array, file):
# output to csv
	with open(file, "w") as g:
	    writer = csv.writer(g)
	    writer.writerows(final_array)



data = []
with open("billboardlyrics.csv") as f:
	reader = csv.reader(f)
	for row in reader:
		data.append(row)


array_locations = {"1960": 0, "1970": 1, "1980": 2, "1990": 3, "2000": 4, "2010": 5, "songs": 6, "start": 7, "end": 8}


artists_data = {}
data = data[1:]
for row in data:
	artist = row[2]
	year = row[3]
	# trim off the feature from the artist.
	artist = remove_feature(artist)

	if artist not in artists_data:
		# create data array of the appropriate length
		dp = [0] *9
		dp[array_locations[det_decade(row[3])]] =1
		dp[array_locations["songs"]] = row[1]
		artists_data[artist] = dp
		artists_data[artist][array_locations["start"]] = str(year)
		artists_data[artist][array_locations["end"]] = str(year)
		
	else:
		#increment the song count, add the new song 	
		if int(year) < int(artists_data[artist][array_locations["start"]]):
			artists_data[artist][array_locations["start"]] = str(year)
		elif int(year) > int(artists_data[artist][array_locations["end"]]):
			artists_data[artist][array_locations["end"]] = str(year)

		scaled_yr = det_decade(row[3])
		artists_data[artist][array_locations[scaled_yr]] += 1
		# add neww song to songs string.
		artists_data[artist][array_locations["songs"]] = artists_data[artist][array_locations["songs"]] + ", " + row[1]


#Grab Gender
gender_data = []
with open("singers_gender.csv", 'r', encoding='latin1') as f:
		reader = csv.reader(f)
		for row in reader:
				gender_data.append(row)


for solo_artist in gender_data:
	singer = solo_artist[0].lower()
	if singer in artists_data:
		artists_data[singer].append(solo_artist[1])
		artists_data[singer].append(solo_artist[2])


#format data for csv
final_array = []
for artist in artists_data:
	artist_array = [artist]
	for element in artists_data[artist]:
		artist_array.append(element)
	final_array.append(artist_array)



write_to_csv(final_array, "artist_song_counts_range1.csv")







