from flask import Flask, render_template, request

app = Flask('app')

classes = [
    'Sentimentale', 'Anticipation', 'Science-fiction', 'Aventure', 'Philosophie', 'Policier', 'Apprentissage', 'Fable', 'Horreur', 'Espionnage', 'Biographie'
]

personnages = []

@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html', classes=classes)


# histoire
@app.route('/liste')
def liste():
    global personnages
    return render_template('liste.html', liste=personnages)


@app.route('/ficheDepuisListe', methods=['POST'])
def ficheDepuisListe():
    perso = {'nom': 'Legere', 'titre': 'Napoléon ', 'classe': 'Biographie', 'histoire': "Napoléon Bonaparte, né le 15 août 1769 à Ajaccio et mort le 5 mai 1821 sur l'île de Sainte-Hélène, est un militaire et homme d'État français, premier empereur des Français du 18 mai 1804 au 6 avril 1814 et du 20 mars au 22 juin 1815, sous le nom de Napoléon Ier.\r\n\r\nSecond enfant de Charles Bonaparte et Letizia Ramolino, Napoléon Bonaparte devient en 1793 général dans les armées de la Première République française, née de la Révolution, où il est notamment commandant en chef de l'armée d'Italie puis de l'armée d'Orient. Arrivé au pouvoir en 1799 par le coup d'État du 18 Brumaire, il est Premier consul — consul à vie à partir du 2 août 1802 — jusqu'au 18 mai 1804, date à laquelle l'Empire est proclamé par un sénatus-consulte suivi d'un plébiscite. Il est sacré empereur, en la cathédrale Notre-Dame de Paris, le 2 décembre 1804, par le pape Pie VII, en même temps que son épouse Joséphine de Beauharnais.\r\n\r\nEn tant que général en chef et chef d'État, Napoléon tente de briser les coalitions montées et financées par le royaume de Grande-Bretagne et qui rassemblent, à partir de 1792, les monarchies européennes contre la France et son régime né de la Révolution. Il conduit les armées françaises d'Italie au Nil et d'Autriche à la Prusse et à la Pologne : les nombreuses et brillantes victoires de Bonaparte (Arcole, Rivoli, Pyramides, Marengo, Austerlitz, Iéna, Friedland), dans des campagnes militaires rapides, disloquent les quatre premières coalitions. Les paix successives, qui mettent un terme à chacune de ces coalitions, renforcent la France et donnent à Napoléon un degré de puissance jusqu'alors rarement égalé en Europe, lors de la paix de Tilsit (1807).\r\n\r\nNapoléon réforme durablement l'État, en restaurant son autorité et sa primauté. La France connaît d'importantes réformes, qui font de Napoléon l'un des pères fondateurs des institutions contemporaines françaises. En ce sens, les codifications napoléoniennes, dont le Code civil de 1804, permettent de renforcer les libertés individuelles ou l'égalité des citoyens devant la loi, en opérant une synthèse par la garantie de certains acquis révolutionnaires et la reprise de principes traditionnels issus de l'Ancien Régime. L'administration française est réorganisée, avec la création des préfets dans les départements. De même, une nouvelle monnaie émerge, le franc, tandis qu'est instaurée la Banque de France. Le Conseil d'État est également créé, tout comme les lycées.\r\n\r\nNapoléon tente également de renforcer l'empire colonial français de l'Ancien Régime en outre-mer. Alors que la révolution haïtienne tourne à la sécession dans cette colonie, Napoléon rétablit l'esclavage en 1802, rétablissement qu’il souhaite provisoire, notamment pour empêcher l’indépendance proclamée de l'île par le général Toussaint Louverture. Toujours pour des raisons politiques, Napoléon revend paradoxalement la Louisiane aux États-Unis, en 1803. Il perd cependant la plupart des colonies qui l’intéressaient face aux Britanniques, et perd Saint-Domingue à la suite de l'échec de l'expédition militaire préalable (1802-1803), visant à combattre les indépendantistes.\r\n\r\nNapoléon porte le territoire français à son extension maximale en Europe, avec 134 départements en 1812, transformant Rome, Hambourg, Barcelone ou Amsterdam en chefs-lieux de départements français. Il est aussi président de la République italienne de 1802 à 1805, roi d'Italie de 1805 à 1814, médiateur de la Confédération suisse de 1803 à 1813 et protecteur de la confédération du Rhin de 1806 à 1813. Ses victoires lui permettent d'annexer à la France de vastes territoires et de gouverner la majeure partie de l'Europe continentale en plaçant les membres de sa famille sur les trônes de plusieurs royaumes : Joseph à Naples puis en Espagne, Louis en Hollande, Jérôme en Westphalie et son beau-frère Joachim Murat à Naples. Il crée également un duché de Varsovie, sans restaurer formellement l'indépendance polonaise, et soumet temporairement à son influence des puissances vaincues telles que le royaume de Prusse et l'empire d'Autriche.\r\n\r\nAlors qu'ils financent des coalitions de plus en plus générales, les alliés contre la France finissent par remporter des succès décisifs en Espagne (bataille de Vitoria) et en Allemagne (bataille de Leipzig) en 1813. L'intransigeance de Napoléon devant ces revers lui fait perdre le soutien de pans entiers de la nation française, tandis que ses anciens alliés ou vassaux se retournent contre lui. Amené à abdiquer en 1814 après la prise de Paris, capitale de l'Empire français, et à se retirer à l'île d'Elbe, il tente de reprendre le pouvoir en France, lors de l'épisode des Cent-Jours en 1815. Capable de reconquérir la France et d'y rétablir le régime impérial sans coup férir, il amène pourtant, à la suite de diverses trahisons et dissensions de ses maréchaux, le pays dans une impasse avec la lourde défaite de Waterloo, qui met fin à l'Empire napoléonien et assure la restauration de la dynastie des Bourbons. Sa mort en exil, à Sainte-Hélène, sous la garde des Britanniques, fait l'objet de nombreuses controverses.\r\n\r\nObjet dès son vivant d'une légende dorée comme d'une légende noire, il doit sa très grande notoriété à son habileté militaire, récompensée par de nombreuses victoires, et à sa trajectoire politique étonnante, mais aussi à son régime despotique et très centralisé ainsi qu'à son ambition, qui se traduit par des guerres meurtrières (au Portugal, en Espagne et en Russie) avec des millions de morts et blessés, militaires et civils pour l'ensemble de l'Europe. Il est considéré[Par qui ?] comme l'un des plus grands commandants de l'histoire, et ses guerres et campagnes sont étudiées dans les écoles militaires du monde entier.\r\n\r\nUne tradition romantique fait de Napoléon l'archétype du « grand homme » appelé à bouleverser le monde. C'est ainsi que le comte de Las Cases, auteur du Mémorial de Sainte-Hélène, tente de présenter Napoléon au Parlement britannique dans une pétition rédigée en 1818. Élie Faure, dans son ouvrage Napoléon, qui a inspiré le film d’Abel Gance, le compare à un « prophète des temps modernes ». D'autres auteurs, tel Victor Hugo, font du vaincu de Sainte-Hélène le « Prométhée moderne ». L'ombre de « Napoléon le Grand » plane sur de nombreux ouvrages de Balzac, Stendhal, Musset, mais aussi de Dostoïevski, de Tolstoï et de bien d'autres encore. Par ailleurs, un courant politique français émerge au xixe siècle, le bonapartisme, se réclamant de l'action et du mode de gouvernement de Napoléon.", 'resume': "La Biographie d'un des empereurs les plus emblématique de son époque. Une des plus grandes réussites de mère nature un homme qui sort la France du chaos de la Révolution sous les bases solides d’une expérience militaire.", 'note_personnelle': 'La biographie vaut le détour !!!'}
    for e in personnages:
        if e['nom'] == request.form["nom"]:
            perso = e
            break
    print('perso')
    print(perso)
    return afficherFiche(perso)


@app.route('/fiche', methods=['POST'])
def fiche():
    dico = {key: value for key, value in request.form.items()}
    print('dico')
    print(dico)
    print('personnages')
    print(personnages)
    return afficherFiche(dico)

def afficherFiche(perso):
    return render_template('fiche.html', perso=perso, exemple = {'nom': 'Legere', 'titre': 'Napoléon ', 'classe': 'Biographie', 'histoire': "Napoléon Bonaparte, né le 15 août 1769 à Ajaccio et mort le 5 mai 1821 sur l'île de Sainte-Hélène, est un militaire et homme d'État français, premier empereur des Français du 18 mai 1804 au 6 avril 1814 et du 20 mars au 22 juin 1815, sous le nom de Napoléon Ier.\r\n\r\nSecond enfant de Charles Bonaparte et Letizia Ramolino, Napoléon Bonaparte devient en 1793 général dans les armées de la Première République française, née de la Révolution, où il est notamment commandant en chef de l'armée d'Italie puis de l'armée d'Orient. Arrivé au pouvoir en 1799 par le coup d'État du 18 Brumaire, il est Premier consul — consul à vie à partir du 2 août 1802 — jusqu'au 18 mai 1804, date à laquelle l'Empire est proclamé par un sénatus-consulte suivi d'un plébiscite. Il est sacré empereur, en la cathédrale Notre-Dame de Paris, le 2 décembre 1804, par le pape Pie VII, en même temps que son épouse Joséphine de Beauharnais.\r\n\r\nEn tant que général en chef et chef d'État, Napoléon tente de briser les coalitions montées et financées par le royaume de Grande-Bretagne et qui rassemblent, à partir de 1792, les monarchies européennes contre la France et son régime né de la Révolution. Il conduit les armées françaises d'Italie au Nil et d'Autriche à la Prusse et à la Pologne : les nombreuses et brillantes victoires de Bonaparte (Arcole, Rivoli, Pyramides, Marengo, Austerlitz, Iéna, Friedland), dans des campagnes militaires rapides, disloquent les quatre premières coalitions. Les paix successives, qui mettent un terme à chacune de ces coalitions, renforcent la France et donnent à Napoléon un degré de puissance jusqu'alors rarement égalé en Europe, lors de la paix de Tilsit (1807).\r\n\r\nNapoléon réforme durablement l'État, en restaurant son autorité et sa primauté. La France connaît d'importantes réformes, qui font de Napoléon l'un des pères fondateurs des institutions contemporaines françaises. En ce sens, les codifications napoléoniennes, dont le Code civil de 1804, permettent de renforcer les libertés individuelles ou l'égalité des citoyens devant la loi, en opérant une synthèse par la garantie de certains acquis révolutionnaires et la reprise de principes traditionnels issus de l'Ancien Régime. L'administration française est réorganisée, avec la création des préfets dans les départements. De même, une nouvelle monnaie émerge, le franc, tandis qu'est instaurée la Banque de France. Le Conseil d'État est également créé, tout comme les lycées.\r\n\r\nNapoléon tente également de renforcer l'empire colonial français de l'Ancien Régime en outre-mer. Alors que la révolution haïtienne tourne à la sécession dans cette colonie, Napoléon rétablit l'esclavage en 1802, rétablissement qu’il souhaite provisoire, notamment pour empêcher l’indépendance proclamée de l'île par le général Toussaint Louverture. Toujours pour des raisons politiques, Napoléon revend paradoxalement la Louisiane aux États-Unis, en 1803. Il perd cependant la plupart des colonies qui l’intéressaient face aux Britanniques, et perd Saint-Domingue à la suite de l'échec de l'expédition militaire préalable (1802-1803), visant à combattre les indépendantistes.\r\n\r\nNapoléon porte le territoire français à son extension maximale en Europe, avec 134 départements en 1812, transformant Rome, Hambourg, Barcelone ou Amsterdam en chefs-lieux de départements français. Il est aussi président de la République italienne de 1802 à 1805, roi d'Italie de 1805 à 1814, médiateur de la Confédération suisse de 1803 à 1813 et protecteur de la confédération du Rhin de 1806 à 1813. Ses victoires lui permettent d'annexer à la France de vastes territoires et de gouverner la majeure partie de l'Europe continentale en plaçant les membres de sa famille sur les trônes de plusieurs royaumes : Joseph à Naples puis en Espagne, Louis en Hollande, Jérôme en Westphalie et son beau-frère Joachim Murat à Naples. Il crée également un duché de Varsovie, sans restaurer formellement l'indépendance polonaise, et soumet temporairement à son influence des puissances vaincues telles que le royaume de Prusse et l'empire d'Autriche.\r\n\r\nAlors qu'ils financent des coalitions de plus en plus générales, les alliés contre la France finissent par remporter des succès décisifs en Espagne (bataille de Vitoria) et en Allemagne (bataille de Leipzig) en 1813. L'intransigeance de Napoléon devant ces revers lui fait perdre le soutien de pans entiers de la nation française, tandis que ses anciens alliés ou vassaux se retournent contre lui. Amené à abdiquer en 1814 après la prise de Paris, capitale de l'Empire français, et à se retirer à l'île d'Elbe, il tente de reprendre le pouvoir en France, lors de l'épisode des Cent-Jours en 1815. Capable de reconquérir la France et d'y rétablir le régime impérial sans coup férir, il amène pourtant, à la suite de diverses trahisons et dissensions de ses maréchaux, le pays dans une impasse avec la lourde défaite de Waterloo, qui met fin à l'Empire napoléonien et assure la restauration de la dynastie des Bourbons. Sa mort en exil, à Sainte-Hélène, sous la garde des Britanniques, fait l'objet de nombreuses controverses.\r\n\r\nObjet dès son vivant d'une légende dorée comme d'une légende noire, il doit sa très grande notoriété à son habileté militaire, récompensée par de nombreuses victoires, et à sa trajectoire politique étonnante, mais aussi à son régime despotique et très centralisé ainsi qu'à son ambition, qui se traduit par des guerres meurtrières (au Portugal, en Espagne et en Russie) avec des millions de morts et blessés, militaires et civils pour l'ensemble de l'Europe. Il est considéré[Par qui ?] comme l'un des plus grands commandants de l'histoire, et ses guerres et campagnes sont étudiées dans les écoles militaires du monde entier.\r\n\r\nUne tradition romantique fait de Napoléon l'archétype du « grand homme » appelé à bouleverser le monde. C'est ainsi que le comte de Las Cases, auteur du Mémorial de Sainte-Hélène, tente de présenter Napoléon au Parlement britannique dans une pétition rédigée en 1818. Élie Faure, dans son ouvrage Napoléon, qui a inspiré le film d’Abel Gance, le compare à un « prophète des temps modernes ». D'autres auteurs, tel Victor Hugo, font du vaincu de Sainte-Hélène le « Prométhée moderne ». L'ombre de « Napoléon le Grand » plane sur de nombreux ouvrages de Balzac, Stendhal, Musset, mais aussi de Dostoïevski, de Tolstoï et de bien d'autres encore. Par ailleurs, un courant politique français émerge au xixe siècle, le bonapartisme, se réclamant de l'action et du mode de gouvernement de Napoléon.", 'resume': "La Biographie d'un des empereurs les plus emblématique de son époque. Une des plus grandes réussites de mère nature un homme qui sort la France du chaos de la Révolution sous les bases solides d’une expérience militaire.", 'note_personnelle': 'La biographie vaut le détour !!!'})


@app.route('/nouvelle')
def nouvelle():
    return render_template('nouvelle.html', classes=classes)


@app.route('/ajouter', methods=['POST'])
def ajouter():
    global personnages
    dico = {}
    for key, value in request.form.items():
        dico[key] = value
    personnages += [dico]
    return afficherFiche(dico)



# partie don
@app.route('/don')
def don():
    print('/don')
    return render_template('don.html')
    


donneepaypal = []

# parie paypal
@app.route('/paypal')
def paypal():
    print('/paypal')
    return render_template('paypal.html')

#
@app.route('/listepaypal')
def listepaypal():
    global donneepaypal
    return render_template('listepaypal.html', liste2=donneepaypal)


@app.route('/ficheDepuisListepaypal', methods=['POST'])
def ficheDepuisListepaypal():
    account = None
    for e in donneepaypal:
        if e['nom'] == request.form["nom"]:
            account = e
            break
    print(account)
    return afficherPayPal(account)


@app.route('/infopaypal', methods=['POST'])
def infopaypal():
    dico2 = {key: value for key, value in request.form.items()}

    print('/infopaypal')
    return afficherPayPal(dico2)

def afficherPayPal(account):
    return render_template('infopaypal.html', account=account)



@app.route('/addinfopaypal', methods=['POST'])
def addinfopaypal():
    global donneepaypal
    dico2 = {}
    for key, value in request.form.items():
        dico2[key] = value
    donneepaypal += [dico2]
    print('//addinfopaypal')
    return afficherPayPal(dico2)



app.run(host='0.0.0.0', port=8080)