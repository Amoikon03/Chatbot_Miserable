# Import des librairies
import streamlit as st
from PIL import Image

# Configuration de la page
st.set_page_config(
    page_title="Les Misérables De Victor Hugo",
)

# Fonction pour afficher une section avec titre et contenu
def section(titre, contenu):
    st.header(titre)
    st.write(contenu)

# Fonction pour afficher une image avec un titre en dessous
def image_with_caption(image_path, caption):
    img = Image.open(image_path)
    st.image(img, caption=caption, use_column_width=True)

# Fonction pour afficher un paragraphe justifié
def paragraphe(texte):
    st.write(f"<div style='text-align: justify'>{texte}</div>", unsafe_allow_html=True)

# Titre de page
st.title("Les Misérables De Victor Hugo")

# Image illustrative de l'application
image_with_caption("2052088.webp", " ")

# Résumé du livre avec texte justifié
summary = """
**Résumé de "Les Misérables"**

<div style='text-align: justify;'>
L'histoire suit plusieurs personnages, mais se concentre principalement sur Jean Valjean, un ancien forçat qui cherche la rédemption après avoir purgé une peine de dix-neuf ans de travaux forcés pour avoir volé du pain. Valjean tente de reconstruire sa vie, mais il est constamment poursuivi par l'inspecteur Javert, un policier inflexible qui croit que les criminels ne peuvent pas changer.

### **Principaux personnages et intrigues :**

1. **Jean Valjean** : Après avoir été libéré, il est rejeté par la société à cause de son passé. Grâce à la bonté de l'évêque Myriel, Valjean décide de mener une vie honnête. Il devient riche et respectable, mais son passé le rattrape constamment.

2. **Fantine** : Une jeune femme abandonnée par son amant, qui se retrouve seule avec sa fille, Cosette. Fantine tombe dans la misère et est obligée de vendre ses cheveux et ses dents, puis de se prostituer pour subvenir aux besoins de sa fille. Elle meurt après avoir confié Cosette à Valjean.

3. **Cosette** : La fille de Fantine, maltraitée par les Thénardier, une famille d'aubergistes cupides. Valjean la sauve et l'élève comme sa propre fille. Cosette tombe amoureuse de Marius, un jeune révolutionnaire.

4. **Javert** : L'inspecteur de police obsédé par la capture de Valjean. Sa vision du monde est manichéenne, croyant fermement en la loi et en la punition des criminels sans possibilité de réhabilitation.

5. **Marius Pontmercy** : Un jeune étudiant idéaliste, engagé dans la lutte politique, qui tombe amoureux de Cosette. Leur amour traverse de nombreux obstacles, notamment les émeutes révolutionnaires de Paris.

6. **Les Thénardier** : Un couple sans scrupules qui exploite et maltraite Cosette. Ils réapparaissent dans la vie de Valjean et de Marius, impliqués dans diverses intrigues criminelles.

### **Développement et dénouement :**

Le roman couvre une période d'environ vingt ans, explorant les thèmes de la justice, la rédemption, l'amour et la moralité. Les vies des personnages se croisent sur fond de bouleversements politiques et sociaux, notamment les émeutes de juin 1832 à Paris. Jean Valjean lutte pour protéger Cosette et Marius, tout en échappant à Javert.

Dans la conclusion, Javert se suicide, incapable de concilier sa croyance en la loi et l'acte de miséricorde de Valjean. Marius et Cosette se marient, mais Valjean, fatigué et sentant sa fin proche, leur révèle son passé. Marius, d'abord choqué, finit par pardonner à Valjean. Jean Valjean meurt en paix, entouré de l'amour de Cosette et Marius, ayant finalement trouvé la rédemption et la paix intérieure.

Les Misérables est une œuvre poignante qui dépeint la lutte incessante entre le bien et le mal, tout en offrant un puissant plaidoyer pour la compassion et la justice sociale.
</div>
"""

st.markdown(summary, unsafe_allow_html=True)

# Lien vers l'autre page ou section
st.subheader("Hyperlien vers la page Chatbot")

# Liste de lien
st.write("""

- [Chatbot](http://localhost:8501/Chatbot)

""")
