import discord, json, random, os
from discord.ext import commands
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv('klucz.env')
print('działa klucz')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

#id kanałów

kanal_terrariaczat = 591240468998914052
kanal_terrariamody =591240488145649694
kanal_terrariabudowle = 591319147405901834
kanal_luzne = 591229124950097955
kanal_gry = 629000030698733568
kanal_szukam = 591232396033261568
kanal_memy = 591231724831244309
kanal_bot = 591666865848320032
kanal_ankietyrebirth = 1528694290761519216
kanal_bazgroly = 736244684866846762

#jakiś syf

krysti_variable = 1
ilepast = 0
wujekkujek = 'A jakoćci wspominałem już niegdyś, świętej pamięci mój wujaszek był mąż zacny, lecz surowy wielce. Jam zaś ledwie pacholę był, może lat pięć, może i sześć miałem - któż by to dziś zliczył! Młodziuchny tedy byłem, a wuj u babki naszej w gościnie siedział. I rzekłem żartem, podkreślam — dla żartu jeno!, rym taki mi się w głowie uroił: „Wujek - Kujek!” - rzecze ma niewinna dusza, przez „k”, przez „k”, bom sobie rym taki upodobał. Lecz ledwie słowo z ust mych wypadło, wujaszek srogo na mię spojrzał, a wnet, nie mówiąc ni słowa, liścia takiego mi zdzielił w pysk, że aż echo po izbie się rozniosło! I od onych czasów, powiadam wam, żadnego już żartu z wujem nie śmiałem czynić. '
brus = 'Miaem problemy z pornografią. Byem mocno uzależniony i szukaem mocniejszych wrażeń. Stąd wszedłem na tą na taką stronę. Przeklikaem do ósmej strony, bo nic mi nie odpowiadało... Szukaem po prostu mocniejszych wrażeń. 😈😈😈'
cobyszrobil = 'Czysto teoretycznie, załóżmy, załóżmy czysto teoretycznie, że jesteś prezydentem Chujolandii. Chujolandia zajmuje powiedzmy 30% naszego globu. Twoja Chujolandia jest mocarstwem, nuklearnym, atomowym, jakimkolwiek. Jest bardzo potężna militarnie i w ogóle, prawda? I w pewnym momencie przylatuje Ci jakiś przedstawiciel kurwa, Cipkolandii drugiej planety Cipkolandii i mówi ci tak! Słuchaj... ziomie z Chujolandii, albo się dogadujemy i przylatuje do ciebie co tydzień i przygotowywujesz mi tutaj 10 mężczyzn, 10 kobiet, to, tam, tam, toto, albo wracam na mój statek i odpalam kurwa moje międzygalaktyczne działo w twoją pierdoloną planetę. Co byś zrobił, co byś zrobił... w takim przypadku? '
ostatnie = {}


ankiety_czlon1 = [
    "Najlepszy",
    "Najgorszy",
    "Ulubiony",
    "Najbardziej underrated",
    "Najbardziej overrated"
]
                                                # unused rzeczy do ankiet, może kiedyś użyję
ankiety_czlon2 = [
    "miecz",
    "łuk",
    "yoyo",
    "boss",
    "NPC",
    "akces",
    "armor",
    "biom",
    "event"
]

przekleństwa = [
    'kurw', 'pierd', 'huj', 'jeb', 'kurew'
]

odp_szukam = {
    'gra kto': f'<#{kanal_szukam}> tu masz kanał do tego',
    'chętny do grania': f'<#{kanal_szukam}> tu masz kanał do tego',
    'szukam os': f'<#{kanal_szukam}> tu masz kanał do tego',
    'hce kto': f'<#{kanal_szukam}> tu masz kanał do tego',
    'szukam kog': f'<#{kanal_szukam}> tu masz kanał do tego',
    'ktos gra': f'<#{kanal_szukam}> tu masz kanał do tego',
    'ktoś gra': f'<#{kanal_szukam}> tu masz kanał do tego',
    'kto gra': f'<#{kanal_szukam}> tu masz kanał do tego',
    'ktos chce zag': f'<#{kanal_szukam}> tu masz kanał do tego',
    'ktoś chce zag': f'<#{kanal_szukam}> tu masz kanał do tego'
}

odp_mody = {
    'mod': f'<#{kanal_terrariamody}> tu gadamy o modach',
    'calamity': f'<#{kanal_terrariamody}> tu gadamy o modach',
    'thorium': f'<#{kanal_terrariamody}> tu gadamy o modach',
    'fargo': f'<#{kanal_terrariamody}> tu gadamy o modach',
    'overhaul': f'<#{kanal_terrariamody}> tu gadamy o modach'
}

gamba = [
        ('nic', 36, 0),
        ('+0,1 punkta karnego', 22, 0.1,),
        ('-0,1 punkta karnego', 22, -0.1),
        ('+1 punkt karny ez', 8, 1),
        ('-1 punkt karny, masz farta', 8, -1),
        ('mute', 0.5, 'mute'),                        #  <-  mute 1h                                      #outputy gamby (2. kolumna to szansa w %)
        ('+1 strajk es', 0.1, 5),
        #syf
        (brus, 0.75, 0),
        ('gówno', 1, 0),
        (wujekkujek, 0.9, 0),
        (cobyszrobil, 0.75)
    ]

#------------------------------------------------------------------------

try:
    with open("patusy.json", "r", encoding="utf-8") as plik:
        patusy = json.load(plik)

    patusy = {int(k): v for k, v in patusy.items()}

except FileNotFoundError:
    patusy = {}

#------------------------------------------------------------------------

try:
    with open("strajki.json", "r", encoding="utf-8") as plik:
        strajki = json.load(plik)

    strajki = {int(k): v for k, v in strajki.items()}

except FileNotFoundError:
    strajki = {}

#------------------------------------------------------------------------

odpowiedzi = {
    'barry': 'spoczywaj w pokoju',
    "obalić": "pełna zgoda",
    "fandom": "jebać fandom",
    "belka": "belka ten temat",
    'doa': 'neem',                                  # bot wychwytuje te słowa w zdaniu, po czym ma 1/3 szans na odpowiedź
    'mute': 'permanentny najlepiej',
    "kurw": "nie przeklinajcie",
    "pierd": "nie przeklinajcie",
    "huj": "nie przeklinajcie",
    'jeb': "nie przeklinajcie",
    'kurew': 'nie przeklinajcie'
}

odpowiedzi_kanal = {
    kanal_terrariaczat: {
        **odp_mody,
        **odp_szukam,
    },
    kanal_terrariamody: odp_szukam,
    kanal_terrariabudowle: odp_szukam,              # keywordy zależne od kanału, variablesy wyżej
    kanal_luzne: {
        'offtop': 'luźno',
        'luźno': 'ustalone że luźno',
        **odp_szukam
        },
    kanal_gry: odp_szukam,
    kanal_memy: odp_szukam,
    kanal_bot: odp_szukam,
    kanal_bazgroly: odp_szukam
}

xodpowiedzi = {
    'cześć': 'cześ',
    'czesc': 'cześ',
    'hej': 'kup se klej',
    'siema': 'siema',
    'witam': 'żegnam',
    "co": "gówno",
    "co ?": 'gówno !',
    "działa?": "działa",
    "czar": "nuch",
    'dupa': 'i kamieni kupa',
    'tata jest cola': 'to se weź',                                                    # bot odpowie tylko wtedy, gdy wysłana wiadomość będzie dokładnie taka (nie ma znaczenia czy wielkie czy małe litery tho)
    'rozmowa chuja z butem': 'rel',
    'sad': 'jabłkowy',
    "!pomoc": "https://terraria-pl-lore.fandom.com/pl/wiki/TPLbot",
    "!wiki": "https://terraria.wiki.gg/ oto wiki",
    "!npc": "https://i.redd.it/1pq3d8ie6e051.png",
    '!setupy': 'https://terraria.wiki.gg/wiki/Guide:Class_setups',
    "!ankieta": f"zapraszam na <#{kanal_ankietyrebirth}>",
    "!porno": "niestety nie ma tu takiej komendy",
    "!tplwiki": "https://terraria-pl-lore.fandom.com/pl/wiki/Terraria_PL_Lore_Wiki",
    'https://cdn.discordapp.com/attachments/591229124950097955/1541513360061898792/ezgif.com-gif-maker.gif': 'rel',
}

reakcje = {
    "szczur": "🪤",
    'porno': '🔥',
    'stopy mixa': '👣',
    'mammon': '♿',
    'jajco': '🥚',
    'upvampin': '🧛',
    'brus': '🐖',
    'fdziarz': '👴',
    'umazing': '🍐',
    'nuklearnie fizycznie': '🫃',
    'daily przekle': '❌'
}

zdjęcia = {
    '!potion': 'python rzeczy/qrsyf/potiony.png',
    '!shimmer': 'python rzeczy/qrsyf/shimmer.jpg',
}


async def dodaj_punkty(member, punkty):
    user_id = member.id

    if user_id not in strajki:
        strajki[user_id] = {
            "punkty": 0,
            "strajki": 0
        }

    if strajki[user_id]["punkty"] < 0:
             strajki[user_id]["punkty"] = 0


    strajki[user_id]["punkty"] += punkty


    if strajki[user_id]["punkty"] >= 5:                                                                 #funkcja dodająca punkty karne & strajki

        strajki[user_id]["punkty"] = 0
        strajki[user_id]["strajki"] += 1

        numer_strajka = strajki[user_id]["strajki"]

        czas = 2 ** (numer_strajka - 1)

        await member.timeout(
            timedelta(hours=min(672, czas)),
            reason=f"Strike #{numer_strajka}: spam, niepoprawny język, i inne pierdoły"
        )


    with open("strajki.json", "w", encoding="utf-8") as plik:
        json.dump(strajki, plik, ensure_ascii=False, indent=4)


@bot.event
async def on_ready():
    print(f"Bot {bot.user} działa")

    print("Serwery, na których jestem:")
    for serwer in bot.guilds:
        print(f"- {serwer.name} | ID: {serwer.id}")



@bot.event
async def on_message(message):
    global krysti_variable, ilepast

    if message.author.bot:
        return

    if message.channel.id == 1538268811537678426:                                                         #pułapka na boty (24h muta)
        user = message.author
        await user.timeout(
                    timedelta(hours=24),
                    reason=f"pułapka na boty"
                )
        print('dostał muta')
        return

    text = message.content.lower().strip()



    channel_id = message.channel.id
    user_id = message.author.id



    if channel_id != kanal_bot:

        if channel_id not in ostatnie:
            ostatnie[channel_id] = []

        ostatnie[channel_id].append(user_id)

        ostatnie[channel_id] = ostatnie[channel_id][-6:]                                          #flood (6 wiadomości pod rząd -> ostrzeżenie i znowu liczy)

        if len(ostatnie[channel_id]) == 6:

            if len(set(ostatnie[channel_id])) == 1:

                await message.channel.send("ok ale nie flooduj")

                await dodaj_punkty(
                    message.author,
                    0.6
                )

                ostatnie[channel_id] = []



    liczba = 0

    for przekleństwo in przekleństwa:
        liczba += text.count(przekleństwo)

    if liczba > 0:
        user_id = message.author.id
        #print(user_id)                                                    liczenie przekleństw

        if user_id not in patusy:
            patusy[user_id] = 0

        patusy[user_id] += liczba
        with open("patusy.json", "w", encoding="utf-8") as plik:
            json.dump(patusy, plik, ensure_ascii=False, indent=4)

        await dodaj_punkty(
            message.author,
            liczba * 0.1
        )




    if text.startswith('!czypatus'):
            if message.mentions:
                osoba = message.mentions[0]
                liczba = patusy.get(osoba.id, 0)
                await message.channel.send(f"{osoba.display_name} przeklnął {liczba} razy, co za patus")             #komenda !czypatus
    
            else:
                liczba = patusy.get(message.author.id, 0)
                await message.channel.send(f"Przeklnąłeś {liczba} razy patusie")
    
            return

    if text.startswith('!strajki'):
                if message.mentions:
                    osoba = message.mentions[0]
                    dane = strajki.get(osoba.id, {
                        "punkty": 0,
                        "strajki": 0
                    })
                    liczbapunktów = dane['punkty']
                    liczbastrajków = dane['strajki']
                    await message.channel.send(f"{osoba.display_name} ma {round(liczbapunktów, 1)} punktów karnych i {liczbastrajków} strajków")             #komenda !strajki
        
                else:
                    dane = strajki.get(message.author.id, {
                        "punkty": 0,
                        "strajki": 0
                    })
                    liczbapunktów = dane['punkty']
                    liczbastrajków = dane['strajki']
                    await message.channel.send(f"masz {round(liczbapunktów, 1)} punktów karnych i {liczbastrajków} strajków")
        
                return

    
    if text == '!patusy':

        ranking = sorted(
            patusy.items(),
            key=lambda x: x[1],
            reverse=True
        )

        top5 = ranking[:10]

        wynik = "TOP 10 PATUSÓW:\n\n"                                                                 #komenda !patusy (ranking)

        for miejsce, (user_id, liczba) in enumerate(top5, start=1):

            user = await bot.fetch_user(user_id)

            wynik += f"{miejsce}. {user.display_name} — {liczba} przekleństw\n"

        await message.channel.send(wynik)
        return


    if text == '!krysti':
        krysti_variable = random.randint(1, 23)
        await message.channel.send(                                                                 #komenda !krysti
            file=discord.File(f'python rzeczy/krysti/{krysti_variable}.png')
        )
        return

    if text == '!ile':
        if ilepast == 0 or ilepast == message.guild.member_count:
            await message.channel.send(f'na tpl jest {message.guild.member_count} osób')
        elif ilepast > message.guild.member_count:
            await message.channel.send(f'jest {message.guild.member_count}, ostatnio było {ilepast}, przykra sprawa')           #!ile osób (może usunę)
        else:
            await message.channel.send(f'jest {message.guild.member_count}, ostatnio było {ilepast}, fifka')
        ilepast = message.guild.member_count
        return

    if text == '!gamba':
        wynik = random.choices(
            gamba,
            weights=[x[1] for x in gamba],
            k=1
        )[0]
                                                                                                                #!gamba
        nazwa, waga, punkty = wynik

        await message.channel.send(nazwa)

        if isinstance(punkty, (int, float)):
            if punkty != 0:
                await dodaj_punkty(message.author, punkty)
        else:
            if punkty == 'mute':
                await message.author.timeout(timedelta(hours=1), reason=f"spoczywaj w sikach")

        return

    if text == '!gamba5':
        for i in range(5):
            wynik = random.choices(
                gamba,
                weights=[x[1] for x in gamba],
                k=1
            )[0]
                                                                                                                    #!gamba5
            nazwa, waga, punkty = wynik

            await message.channel.send(nazwa)

            if isinstance(punkty, (int, float)):
                if punkty != 0:
                    await dodaj_punkty(message.author, punkty)
            else:
                if punkty == 'mute':
                    await message.author.timeout(timedelta(hours=1), reason=f"spoczywaj w sikach")

        return

    if text == '!moneta':
        monetawynik = random.choice([1,-1])
        await message.channel.send(f'wypada {monetawynik} punkt!')                                                   #moneta
        await dodaj_punkty(message.author, monetawynik)


    if message.author.id == 960975516779806730 or message.author.id == 1100884416877834383:
        if text.startswith('!detimeout'):
            if message.mentions:                                                                    #usuwanie timeouta
                osoba = message.mentions[0]
                await osoba.timeout(None, reason=f"ez")
                return


    if text == '!testankieta':
        czlon1 = random.choice(ankiety_czlon1)
        czlon2 = random.choice(ankiety_czlon2)
        tytuł = czlon1 + ' ' + czlon2

        ankieta = discord.Poll(question=tytuł, duration=timedelta(hours=1), multiple=False)
        ankieta.add_answer(text='a')
        ankieta.add_answer(text='b')
                                                                                                        # unused ankeity
        await message.channel.send(poll=ankieta)
        return

    
    if text in zdjęcia:
        await message.channel.send(file=discord.File(zdjęcia[text]))                           #wysyłanie zdjęć
        return



    if text in xodpowiedzi:                                                #wiadomości z pojedynczych słów
        await message.channel.send(xodpowiedzi[text])
        return



    for slowo, odp in odpowiedzi.items():                                  #wychwytywanie słów w zdaniach
        if slowo in text:
            if random.randint(1,3) == 1:
                await message.channel.send(odp)
            return



    if message.channel.id in odpowiedzi_kanal:                             #wiadomości zależne od kanału

        odpowiedzi_dla_kanalu = odpowiedzi_kanal[message.channel.id]

        for slowo, odp in odpowiedzi_dla_kanalu.items():
            if slowo in text:
                if slowo in odp_szukam:
                    if random.randint(1,20) == 1:
                        await message.reply(file=discord.File('python rzeczy/qrsyf/szukamgif.gif'))
                    else:
                        await message.reply(odp)
                else:
                    await message.channel.send(odp)
                return



    



    for slowo, odp in reakcje.items():                                     #reakcje
        if slowo in text:
            await message.add_reaction(odp)






            

    #await bot.process_commands(message)

    


bot.run(os.getenv("token"))