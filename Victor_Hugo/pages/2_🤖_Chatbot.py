import streamlit as st
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Fonction pour lire le fichier texte nettoyé
def read_cleaned_text(file_path):
    with open("Victor_Hugo/Miserable_Victor_Hugo.txt", 'r', encoding='utf-8') as file:
        content = file.readlines()
    return content

# Charger le texte nettoyé
cleaned_text = read_cleaned_text('Miserable_Victor_Hugo.txt')

# Convertir les paragraphes en vecteurs TF-IDF
vectorizer = TfidfVectorizer().fit(cleaned_text)
tfidf_matrix = vectorizer.transform(cleaned_text)

# Fonction pour répondre aux questions en utilisant le texte nettoyé
def get_response(user_input):
    # Vérifier si la question concerne le titre du livre
    if "titre" in user_input.lower():
        return "Le titre du livre est 'Les Misérables'."
    if "réception" in user_input.lower() or "accueil" in user_input.lower():
        return "Le livre a été accueilli favorablement par la critique et le public dès sa publication, et il est devenu rapidement populaire, attirant l'attention pour sa profondeur et son humanité."
    if "adaptations théâtrales" in user_input.lower() or "pièces de théâtre" in user_input.lower():
        return "Le livre a été adapté dans de nombreuses pièces de théâtre et comédies musicales, certaines d'entre elles étant devenues des succès durables sur les scènes du monde entier."
    if "symbolisme" in user_input.lower() or "symboles" in user_input.lower():
        return "Le livre est riche en symbolisme, avec des éléments tels que la lumière et l'obscurité, les couleurs, les noms des personnages et les motifs récurrents qui ajoutent des couches de signification à l'histoire."
    if "éditions" in user_input.lower() or "versions" in user_input.lower():
        return "Il existe de nombreuses éditions du livre, y compris des éditions abrégées, annotées et illustrées, ainsi que des éditions spéciales pour les lecteurs jeunes et adultes."
    if "contexte social" in user_input.lower() or "social" in user_input.lower():
        return "Le livre offre un aperçu profond des conditions sociales de la France du 19ème siècle, y compris la pauvreté, l'injustice sociale, la lutte des classes et les aspirations à la liberté et à l'égalité."
    if "contexte politique" in user_input.lower() or "politique" in user_input.lower():
        return "Le livre explore les thèmes politiques de l'époque, y compris les révoltes populaires, les idéaux républicains et les luttes pour le changement social et politique."
    if "contexte économique" in user_input.lower() or "économique" in user_input.lower():
        return "Le livre met en lumière les disparités économiques de la France du 19ème siècle, avec une classe ouvrière appauvrie et exploitée et une élite riche et privilégiée."
    if "contexte culturel" in user_input.lower() or "culturel" in user_input.lower():
        return "Le livre reflète les valeurs culturelles de son époque, ainsi que les changements et les défis auxquels la société française était confrontée au 19ème siècle."
    if "contexte littéraire" in user_input.lower() or "littéraire" in user_input.lower():
        return "Le livre s'inscrit dans le contexte du mouvement romantique en littérature, avec ses thèmes de passion, d'émotion et de rébellion contre les conventions."
    if "références historiques" in user_input.lower() or "historiques" in user_input.lower():
        return "Le livre contient de nombreuses références historiques, notamment des événements politiques et sociaux de la France du 19ème siècle, qui enrichissent le contexte de l'histoire."
    if "intrigue" in user_input.lower() or "histoire" in user_input.lower() or "de quoi parle" in user_input.lower():
        return "Le livre raconte l'histoire de plusieurs personnages, mais il se concentre principalement sur le parcours de Jean Valjean, un ancien forçat qui cherche la rédemption après avoir purgé une peine de prison pour avoir volé du pain. L'histoire explore les thèmes de la justice, de la rédemption, de l'amour et de la moralité, et se déroule dans la France du 19ème siècle."
    if "personnages principaux" in user_input.lower() or "principaux personnages" in user_input.lower():
        return (
            "Les principaux personnages incluent : Jean Valjean, un ancien forçat cherchant la rédemption ; Javert, l'inspecteur de police obsédé par la capture de Valjean ; Fantine, une jeune mère célibataire ; Cosette, la fille de Fantine ; Marius Pontmercy, un jeune révolutionnaire ; et les Thénardier, un couple d'aubergistes sans scrupules.")
    if "contexte historique" in user_input.lower() or "historique" in user_input.lower():
        return "Le livre se déroule dans le contexte de la France du 19ème siècle, une période marquée par des bouleversements politiques, sociaux et économiques, y compris la Révolution française et ses répercussions."
    if "thèmes" in user_input.lower() or "messages" in user_input.lower():
        return "Les thèmes principaux du livre comprennent la rédemption, la justice, l'amour, la moralité, la lutte des classes, et les inégalités sociales."
    if "structure narrative" in user_input.lower() or "structure" in user_input.lower():
        return "Le livre est divisé en plusieurs volumes et suit les parcours de différents personnages à travers une période d'environ vingt ans. Il comprend également des digressions historiques et des réflexions philosophiques."
    if "style d'écriture" in user_input.lower() or "écriture" in user_input.lower():
        return "Victor Hugo est connu pour son style d'écriture lyrique et évocateur, ainsi que pour sa capacité à dépeindre des émotions et des scènes de manière puissante et visuelle."
    if "date de naissance" in user_input.lower() or "né" in user_input.lower():
        return "Victor Hugo est né le 26 février 1802 à Besançon, en France."
    if "date de décès" in user_input.lower() or "mort" in user_input.lower():
        return "Victor Hugo est décédé le 22 mai 1885 à Paris, en France."
    if "style d'écriture" in user_input.lower() or "écriture" in user_input.lower():
        return "Victor Hugo est connu pour son style d'écriture lyrique et évocateur, ainsi que pour sa capacité à dépeindre des émotions et des scènes de manière puissante et visuelle."
    if "contexte historique" in user_input.lower() or "historique" in user_input.lower():
        return "Le livre se déroule dans le contexte de la France du 19ème siècle, une période de bouleversements politiques, sociaux et économiques, y compris la Révolution française et ses répercussions."
    if "structure narrative" in user_input.lower() or "structure" in user_input.lower():
        return "Le livre est divisé en cinq volumes et comprend plusieurs parties et chapitres qui suivent les parcours de différents personnages à travers une période d'environ vingt ans."
    if "influences littéraires" in user_input.lower() or "influences" in user_input.lower():
        return "Victor Hugo a été influencé par de nombreux écrivains et courants littéraires de son époque, ainsi que par ses propres expériences de vie et ses voyages."
    if "réception critique" in user_input.lower() or "critique" in user_input.lower():
        return "Le livre a été largement salué par la critique pour sa profondeur, son humanité et son exploration des thèmes universels. Cependant, certains critiques ont également soulevé des questions sur sa longueur et sa complexité."
    if "adaptations cinématographiques" in user_input.lower() or "films" in user_input.lower():
        return "Le livre a été adapté dans de nombreux films, dont plusieurs versions cinématographiques et télévisées, mettant en vedette des acteurs célèbres et récompensés."
    if "contexte politique" in user_input.lower() or "politique" in user_input.lower():
        return "Le livre explore les thèmes politiques de l'époque, y compris les inégalités sociales, la lutte des classes, les révoltes populaires et les idéaux républicains."
    if "contexte social" in user_input.lower() or "social" in user_input.lower():
        return "Le livre offre un aperçu profond des conditions sociales de la France du 19ème siècle, y compris la pauvreté, la criminalité, l'injustice et les luttes pour la liberté et l'égalité."
    if "références religieuses" in user_input.lower() or "religion" in user_input.lower():
        return "Le livre contient de nombreuses références religieuses et morales, y compris des thèmes de rédemption, de compassion et de destinée divine."
    if "morale" in user_input.lower() or "leçon" in user_input.lower():
        return "Le livre enseigne des leçons importantes sur la rédemption, la compassion, la justice et la dignité humaine."
    if "analyse littéraire" in user_input.lower() or "analyse" in user_input.lower():
        return "De nombreuses analyses littéraires ont été écrites sur 'Les Misérables', explorant ses thèmes, son style, ses personnages et son importance historique et culturelle."
    if "format" in user_input.lower() or "structure" in user_input.lower():
        return "Le livre est généralement publié sous forme de roman, mais il existe également des éditions abrégées, des adaptations pour les jeunes lecteurs et d'autres formats."
    if "traduction" in user_input.lower() or "traduit" in user_input.lower():
        return "Le livre a été traduit dans de nombreuses langues à travers le monde, permettant à un large public de découvrir son histoire et ses thèmes."
    if "publicité" in user_input.lower() or "promotion" in user_input.lower():
        return "Le livre a été promu à sa sortie par des critiques élogieuses et des campagnes de marketing visant à attirer l'attention sur son importance littéraire."
    if "difficulté" in user_input.lower() or "compréhension" in user_input.lower():
        return "La lecture peut être difficile pour certains lecteurs en raison de la densité du texte, de la complexité des thèmes et de la longueur du livre."
    if "impact culturel" in user_input.lower() or "culture" in user_input.lower():
        return "Le livre a eu un impact durable sur la culture mondiale, inspirant de nombreux artistes, écrivains, cinéastes et intellectuels à travers les générations."
    if "signification" in user_input.lower() or "importance" in user_input.lower():
        return "Le livre est important à la fois en tant que témoignage historique et en tant qu'œuvre d'art intemporelle, offrant des perspectives uniques sur la condition humaine et la société."
    # Ajouter d'autres réponses ici ...

    # Convertir l'entrée de l'utilisateur en vecteur TF-IDF
    user_tfidf = vectorizer.transform([user_input])

    # Calculer les similarités de cosinus entre l'entrée de l'utilisateur et chaque paragraphe
    similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()

    # Récupérer l'indice du paragraphe avec la plus grande similarité
    most_similar_paragraph_index = similarities.argmax()
    max_similarity = similarities[most_similar_paragraph_index]

    # Vérifier si la similarité est suffisante pour retourner une réponse
    if max_similarity > 0.1:  # Ajuster le seuil de similarité si nécessaire
        return cleaned_text[most_similar_paragraph_index]
    else:
        return "Je suis désolé, je n'ai pas trouvé de réponse à votre question."


# Interface utilisateur Streamlit
st.title("Chatbot des Misérables")

# Zone de texte pour poser des questions
st.header("Posez une question sur le livre :")
user_input = st.text_input("Vous : ")

# Bouton pour soumettre la question
submit_button = st.button("Poser la question")

if submit_button and user_input:
    # Obtenir la réponse
    response = get_response(user_input)

    # Afficher la réponse
    st.header("Réponse du Chatbot :")
    st.write(response)

 # Lien vers l'autre page ou section
st.subheader("Hyperlien vers la page Acceuil")


# Liste de lien
st.write("""

- [Acceuil](http://localhost:8501/)

""")
