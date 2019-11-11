import csv

f = open('data.csv')
reader = csv.reader(f)
    
albums = []
for row in reader:
    albums.append(row)
    
# albums = [row for row in reader]

header = albums[0]
albums = albums[1:]



list_of_album_dicts = [dict(zip(header,album)) for album in albums]

def find_by_name(name, elements):
    for element in elements:
        if element['album'] == name:
            return element
    return None
    
def find_by_rank(number, elements):
    for element in elements:
        if int(element['number']) == number:
            return element
    return None 
    
def find_by_year(year, elements):
    albums_by_year = []
    for element in elements:
        if int(element['year']) == year:
            albums_by_year.append(element)        
    return albums_by_year

def find_by_years(year1 , year2, elements):
    albums_by_year = []
    for element in elements:
        if year1 <= int(element['year']) <= year2:
            albums_by_year.append(element)        
    return albums_by_year

def find_by_rank(rank, elements):
    for element in elements:
        if int(element['number']) == rank:
            return element

def find_by_ranks(rank1, rank2, elements):
    albums_by_rank = []
    for element in elements:
        if int(rank1) <= int(element['number']) <= int(rank2):
            albums_by_rank.append(element)        
    return albums_by_rank

# def find_by_year(year):
#     return list(filter(lambda album_dict: album_dict['year'] == year, list_of_album_dicts))
    
# def find_by_years(year1, year2):
#     return list(filter(lambda album_dict: year1 <= album_dict['year'] <= year2, list_of_album_dicts))

# def find_by_ranks(rank1, rank2):
#     return list(filter(lambda album_dict: rank1 <= album_dict['number'] <= rank2, list_of_album_dicts))

def all_titles(elements):
    titles = []
    for element in elements:
        title = element['album']
        titles.append(title)
    return titles


def all_artists(elements):
    artists = []
    for element in elements:
        artist = element['artist']
        artists.append(artist)
    return artists
        

def _get_max_freq(elements):
    freq = {}
    for element in elements:
        if element not in freq:
            freq[element] = 1
        else:
            freq[element] += 1
    
    highest = max(freq.items(),key=lambda t:t[1])[1]
    highest_freq=[]
    for element in freq:
        if freq[element] == highest:
            highest_freq.append(element)
    return highest_freq



def most_albums(elements):
    artists = all_artists(elements)
    return _get_max_freq(artists) 


import string

def most_words(elements):
    titles = all_artists(elements)
    def filter_out_special_chars(string_):
        good_char = string.ascii_letters + ' '
        good_list = filter(lambda c : c in good_char, string_)
        good_str = ''.join(good_list)
        return good_str
    def get_words(string_):
        good_str = filter_out_special_chars(string_)
        list_of_words = good_str.split(' ')
        return list_of_words
    words_in_titles = [get_words(title) for title in titles]
   
    words = sum(words_in_titles,[])
    
    return _get_max_freq(words)
        

def list_of_years(elements):
    list_yrs = []
    for element in elements:
        list_yr = element['year']
        list_yr_int = int(list_yr)
        list_yrs.append(list_yr_int)
    return list_yrs


import matplotlib.pyplot as plt


def make_hist_albums_by_decade(elements):
    plt.clf
    return plt.hist(list_of_years(elements), bins=[1950,1960,1970,1980,1990,2000,2010,2020])



def list_of_genres(elements):
    list_genres = []
    for element in elements:
        genre = element['genre'].split(',')
        genre = [s.strip() for s in genre]
        list_genres.append(genre)
    return sum(list_genres, [])

def make_hist_albums_by_genre(elements):
    plt.clf()
    plt.hist(list_of_genres(elements))
    plt.show()


    
# open the text file in read
text_file = open('top-500-songs.txt', 'r')
# read each line of the text file
# here is where you can print out the lines to your terminal and get an idea 
# for how you might think about re-formatting the data
lines = text_file.readlines()

def to_list_of_lists(lines):
    list_of_lists = []
    for line in lines:
        cleaned_string = line.strip()
        list_ = cleaned_string.split('\t')
        list_of_lists.append(list_)
    return list_of_lists

list_of_lists = to_list_of_lists(lines)

def into_list_of_dicts(elements):
    top_500_dicts = []
    for element in elements:
        dict_1 = {'number': int(element[0]),
               'name': element[1] ,
               'artist': element[2],
               'year': int(element[3])}
        top_500_dicts.append(dict_1)
    return top_500_dicts
        
top_500_dicts = into_list_of_dicts(list_of_lists)   

import json

file = open('track_data.json', 'r')
json_data = json.load(file)

def all_tracks(elements):
    tracks = []
    for element in elements:
        track = element['tracks']
        tracks.append(track)
    return tracks

def all_song_names(elements):
    tracks = []
    for element in elements:
        track = element['name']
        tracks.append(track)
    return tracks

json_tracks_lists = all_tracks(json_data)

def multi_to_single_list (list_of_lists):
    single_list = []
    for _list in list_of_lists:
        single_list.extend(_list)
    return single_list

single_list_json = multi_to_single_list (json_tracks_lists)

def intersection(list_1, list_2):
    list_3 = [x for x in list_1 if x in list_2] 
    return list_3 

def all_song_names(elements):
    tracks = []
    for element in elements:
        track = element['name']
        tracks.append(track)
    return tracks

top_songs_in_json = intersection(single_list_json, all_song_names(top_500_dicts))

def top_album_in_charts(list_of_dicts, elements):
    freq = json_data
    for freq_1 in freq:
        freq_1['count'] = 0
    freq

    for freq_1 in freq:
        songs = freq_1['tracks']
        for song in songs:
            for element in elements:
                if song == element:
                    freq_1['count'] += 1
    
    counts = []
    for freq_1 in freq:
        counts.append(freq_1['count'])
    counts
    highest = max(counts)
        
    highest_freq=[]
    for freq_1 in freq:
        if freq_1['count'] == highest:
            highest_freq.append(freq_1['album'])
            highest_freq.append(freq_1['artist'])
    return highest_freq


                
        