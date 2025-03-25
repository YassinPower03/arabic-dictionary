"""
Module containing the Arabic dictionary data and related functions.
This is a simplified in-memory dictionary for demonstration purposes.
In a production environment, this would likely be stored in a database.
"""

# Sample Arabic dictionary with word information
arabic_dictionary = {
    "كتاب": {
        "meanings": ["مجموعة من الأوراق المطبوعة والمجلدة التي تحتوي على نص أو صور"],
        "examples": ["قرأت كتاباً ممتعاً عن الحيوانات", "استعرت كتاباً من المكتبة"],
        "synonyms": ["مؤلف", "مصنف", "سفر"],
        "antonyms": [],
        "translations": {
            "english": "book",
            "french": "livre",
            "spanish": "libro"
        }
    },
    "مدرسة": {
        "meanings": ["مؤسسة تعليمية يتلقى فيها الطلاب الدروس"],
        "examples": ["ذهبت إلى المدرسة هذا الصباح", "المدرسة مكان للتعلم والتعليم"],
        "synonyms": ["معهد", "كتّاب"],
        "antonyms": [],
        "translations": {
            "english": "school",
            "french": "école",
            "spanish": "escuela"
        }
    },
    "بيت": {
        "meanings": ["مبنى يستخدم للسكن والعيش فيه"],
        "examples": ["عدت إلى البيت بعد المدرسة", "بيتنا جميل ومريح"],
        "synonyms": ["منزل", "دار", "مسكن"],
        "antonyms": [],
        "translations": {
            "english": "house",
            "french": "maison",
            "spanish": "casa"
        }
    },
    "شمس": {
        "meanings": ["النجم المركزي في المجموعة الشمسية الذي يوفر الضوء والحرارة للأرض"],
        "examples": ["تشرق الشمس في الصباح", "ضوء الشمس مفيد للصحة"],
        "synonyms": ["ضياء", "نور"],
        "antonyms": ["قمر", "ظلام"],
        "translations": {
            "english": "sun",
            "french": "soleil",
            "spanish": "sol"
        }
    },
    "قمر": {
        "meanings": ["جرم سماوي يدور حول الأرض ويعكس ضوء الشمس ليلاً"],
        "examples": ["القمر منير الليلة", "يظهر القمر كاملاً مرة كل شهر"],
        "synonyms": ["هلال", "بدر"],
        "antonyms": ["شمس"],
        "translations": {
            "english": "moon",
            "french": "lune",
            "spanish": "luna"
        }
    },
    "ماء": {
        "meanings": ["سائل شفاف بلا لون أو طعم أو رائحة، ضروري للحياة"],
        "examples": ["شربت ماءً بارداً", "الماء ضروري للحياة"],
        "synonyms": ["سائل", "عنصر"],
        "antonyms": ["جفاف", "عطش"],
        "translations": {
            "english": "water",
            "french": "eau",
            "spanish": "agua"
        }
    },
    "طعام": {
        "meanings": ["مواد تؤكل لتوفير التغذية للجسم"],
        "examples": ["تناولت طعاماً لذيذاً", "أعد أمي طعاماً شهياً"],
        "synonyms": ["غذاء", "أكل", "مأكولات"],
        "antonyms": ["جوع"],
        "translations": {
            "english": "food",
            "french": "nourriture",
            "spanish": "comida"
        }
    },
    "حب": {
        "meanings": ["شعور عميق بالمودة والرعاية تجاه شخص أو شيء"],
        "examples": ["الحب بين الأسرة مهم", "حب الوطن واجب على كل مواطن"],
        "synonyms": ["وِد", "عشق", "غرام"],
        "antonyms": ["كره", "بغض"],
        "translations": {
            "english": "love",
            "french": "amour",
            "spanish": "amor"
        }
    },
    "لعب": {
        "meanings": ["نشاط ممتع يقوم به الأطفال للتسلية"],
        "examples": ["الأطفال يحبون اللعب", "اللعب مهم لنمو الطفل"],
        "synonyms": ["تسلية", "مرح"],
        "antonyms": ["عمل", "جد"],
        "translations": {
            "english": "play",
            "french": "jouer",
            "spanish": "jugar"
        }
    },
    "مغرب": {
        "meanings": ["البلد الواقع في شمال أفريقيا", "اتجاه غروب الشمس"],
        "examples": ["المغرب بلد جميل", "تغرب الشمس في المغرب"],
        "synonyms": ["الغرب", "المملكة المغربية"],
        "antonyms": ["مشرق"],
        "translations": {
            "english": "Morocco / west",
            "french": "Maroc / ouest",
            "spanish": "Marruecos / oeste"
        }
    },
    "مدينة": {
        "meanings": ["منطقة مأهولة كبيرة ومنظمة"],
        "examples": ["مراكش مدينة جميلة", "أعيش في مدينة كبيرة"],
        "synonyms": ["حاضرة", "بلدة"],
        "antonyms": ["قرية", "ريف"],
        "translations": {
            "english": "city",
            "french": "ville",
            "spanish": "ciudad"
        }
    },
    "صديق": {
        "meanings": ["شخص تربطك به علاقة ود ومحبة"],
        "examples": ["أحمد صديقي المفضل", "الصديق الحقيقي يساعدك في وقت الحاجة"],
        "synonyms": ["رفيق", "خليل", "صاحب"],
        "antonyms": ["عدو", "خصم"],
        "translations": {
            "english": "friend",
            "french": "ami",
            "spanish": "amigo"
        }
    },
    "معلم": {
        "meanings": ["شخص يعلم الآخرين ويقدم لهم المعرفة"],
        "examples": ["المعلم يشرح الدرس", "أحترم معلمي كثيراً"],
        "synonyms": ["مدرس", "أستاذ", "مربي"],
        "antonyms": ["طالب", "تلميذ"],
        "translations": {
            "english": "teacher",
            "french": "enseignant",
            "spanish": "maestro"
        }
    },
    "طالب": {
        "meanings": ["شخص يتلقى التعليم في مدرسة أو جامعة"],
        "examples": ["أنا طالب في المدرسة الابتدائية", "الطالب المجتهد يحصل على درجات عالية"],
        "synonyms": ["تلميذ", "دارس"],
        "antonyms": ["معلم", "أستاذ"],
        "translations": {
            "english": "student",
            "french": "étudiant",
            "spanish": "estudiante"
        }
    },
    "قلم": {
        "meanings": ["أداة للكتابة على الورق"],
        "examples": ["أكتب بالقلم الأزرق", "اشتريت قلماً جديداً"],
        "synonyms": ["حبر", "يراعة"],
        "antonyms": [],
        "translations": {
            "english": "pen",
            "french": "stylo",
            "spanish": "bolígrafo"
        }
    }
}

def get_word_info(word):
    """
    Retrieve information about a specific word from the dictionary.
    
    Args:
        word (str): The Arabic word to look up
        
    Returns:
        dict or None: Dictionary with word information or None if not found
    """
    return arabic_dictionary.get(word)
