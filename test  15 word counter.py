import operator

full_text = """""
Is this the real life
Is this just fantasy
Caught in a landslide
No escape from reality

Open your eyes
Look up to the skies and see
I'm just a poor boy, I need no sympathy
Because I'm easy come easy go
Little high, little low
Any way the wind blows
Doesn't really matter to me to me

Mama just killed a man
Put a gun against his head
Pulled my trigger now he's dead
Mama life had just begun
But now I've gone and thrown it all away

Mama ooh
Didn't mean to make you cry
If I'm not back again this time tomorrow
Carry on carry on as if nothing really matters

Too late my time has come
Sends shivers down my spine
Body's aching all the time
Goodbye everybody I've got to go
Gotta leave you all behind and face the truth

Mama ooh Any way the wind blows
I don't wanna die
I sometimes wish I'd never been born at all

I see a little silhouetto of a man
Scaramouche Scaramouche will you do the Fandango
Thunderbolt and lightning very very frightening me
Galileo Galileo
Galileo Galileo
Galileo Figaro
Magnifico-o-o-o-o

I'm just a poor boy, nobody loves me
He's just a poor boy from a poor family
Spare him his life from this monstrosity

Easy come easy go will you let me go
Bismillah No, we will not let you go Let him go
Bismillah We will not let you go Let him go
Bismillah We will not let you go Let me go
Will not let you go Let me go
Never let you go Never never never never let me go
Oh oh oh oh
No no no no no no no
Oh mamma mia mamma mia Mamma mia let me go
Beelzebub has a devil put aside for me for me for me

So you think you can stone me and spit in my eye
So you think you can love me and leave me to die
Oh baby can't do this to me baby
Just gotta get out just gotta get right outta here

Ooh ooh yeah ooh yeah

Nothing really matters
Anyone can see
Nothing really matters
Nothing really matters to me

Any way the wind blows
"""

word_list = full_text.split()

word_count = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)

for word_tuple in sorted_count:
    print(f'{word_tuple[0].capitalize()} - {word_tuple[1]}')

print(f'\nThere are {len(sorted_count)} unique words ')

print (sorted_count)




