def histogram(song_lyrics):
    count = dict()
    lines = str(song_lyrics).split(' ')  # Splitting lyrics into words
    for words in lines:
        if words not in count:
            count[words] = 1
        else:
            count[words] += 1
    return count

def main():
    fav_song_lyrics = 'Baby really hurt me crying in the taxi He don\'t wanna know me Says he made the big mistake of dancing in my storm Says it was poison So I guess I\'ll go home Into the arms of the girl that I love The only love I haven\'t screwed up She\'s so hard to please but she\'s a forest fire I do my best to meet her demands play at romance we slow dance In the living room but all that a stranger would see Is one girl swaying alone stroking her cheek They say You\'re a little much for me You\'re a liability You\'re a little much for me So they pull back make other plans I understand I\'m a liability Get you wild make you leave I\'m a little much for e-a-na-na-na everyone The truth is I am a toy that people enjoy Til all of the tricks don\'t work anymore And then they are bored of me I know that it\'s exciting running through the night but Every perfect summer\'s eating me alive until you\'re gone Better on my own They say You\'re a little much for me You\'re a liability You\'re a little much for me So they pull back make other plans I understand I\'m a liability Get you wild make you leave I\'m a little much for e-a-na-na-na everyone They\'re gonna watch me disappear into the sun You\'re all gonna watch me disappear into the sun'
    print(histogram(fav_song_lyrics))

if __name__ == '__main__':
    main()
