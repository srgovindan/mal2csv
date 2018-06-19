# MAL XML to CSV Converter v0.2
# Created by srgovindan, 19 June 2018
import xml.etree.ElementTree as ET 
import csv
print('\nProgram started.')

# Anime List 
print('Converting MAL Anime List.')
# get xml file to convert
filename = 'animelist.xml'
tree = ET.parse(filename)
root = tree.getroot()
print('Got XML file.')
# open a file for writing on the desktop
path = raw_input('Please enter the file path of the export file in the format, .../animelist.csv :')
animeList = open(path, 'w')
print('Opened file for writing.')
# create the csv writer object
csvwriter = csv.writer(animeList,'excel')
list_head = []
print('Created CSV writer.\n')
# find and convert XML data to CSV
for member in root.findall('anime'):
	# create a temp variable to store data for each row
	anime = []
	# scrub MAL series ID and use as list head value
	malID = member.find('series_animedb_id').text
	list_head.append(malID)

	# scrub other data from xml
	title = member.find('series_title').text
	title = title.encode('ascii','ignore')
	anime.append(title)

	mediaType = member.find('series_type').text
	anime.append(mediaType)

	status = member.find('my_status').text
	anime.append(status)

	score = member.find('my_score').text
	anime.append(score)

	episodes_watched = member.find('my_watched_episodes').text
	anime.append(episodes_watched)

	episodes = member.find('series_episodes').text
	anime.append(episodes)

	date_start = member.find('my_start_date').text
	anime.append(date_start)

	date_finish = member.find('my_finish_date').text
	anime.append(date_finish)

	print(anime)
	csvwriter.writerow(anime)
# close and save CSV file
animeList.close()
print('Closed CSV file.')


# Manga List
print('Converting MAL Manga List.')
# get xml file to convert
filename = 'mangalist.xml'
tree = ET.parse(filename)
root = tree.getroot()
print('Got XML file.')
# open a file for writing on the desktop
path = raw_input('Please enter the file path of the export file in the format, .../mangalist.csv :')
mangaList = open(path, 'w')
print('Opened file for writing.')
# create the csv writer object
csvwriter = csv.writer(mangaList,'excel')
list_head = []
print('Created CSV writer.\n')
# find and convert XML data to CSV
for member in root.findall('manga'):
	# create a temp variable to store data for each row
	manga = []
	# scrub MAL series ID and use as list head value
	malID = member.find('manga_mangadb_id').text
	list_head.append(malID)

	# scrub other data from xml
	title = member.find('manga_title').text
	title = title.encode('ascii','ignore')
	manga.append(title)

	status = member.find('my_status').text
	manga.append(status)

	score = member.find('my_score').text
	manga.append(score)

	ch_read = member.find('my_read_chapters').text
	manga.append(ch_read)

	ch = member.find('manga_chapters').text
	manga.append(ch)

	vol_read = member.find('my_read_volumes').text
	manga.append(vol_read)

	vol = member.find('manga_volumes').text
	manga.append(vol)

	date_start = member.find('my_start_date').text
	manga.append(date_start)

	date_finish = member.find('my_finish_date').text
	manga.append(date_finish)

	print(manga)
	csvwriter.writerow(manga)
# close and save CSV file
mangaList.close()
print('Closed CSV file.')
