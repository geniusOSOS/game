import json

# New sentences to add
new_sentences = [
    {"sentence": "Using PyCharm can enhance your coding efficiency.", "translation": "使用PyCharm可以提高你的编码效率。", "phonetics": ["ˈjuːzɪŋ", "ˈpaɪʧɑrm", "kæn", "ɪnˈhæns", "jʊr", "ˈkoʊdɪŋ", "ɪˈfɪʃənsi"]},
    {"sentence": "Docker is essential for modern software development.", "translation": "Docker在现代软件开发中是必不可少的。", "phonetics": ["ˈdɑkər", "ɪz", "ɪˈsɛnʃəl", "fɔr", "ˈmɑdərn", "ˈsɔftˌwɛr", "dɪˈvɛləpmənt"]},
    {"sentence": "Learning Python can open up many career opportunities.", "translation": "学习Python可以打开许多职业机会。", "phonetics": ["ˈlɜrnɪŋ", "ˈpaɪθɑn", "kæn", "ˈoʊpən", "ʌp", "ˈmɛni", "kəˈrɪr", "ˌɑpərˈtunɪtiz"]},
    {"sentence": "Git helps in managing project versions effectively.", "translation": "Git有助于有效管理项目版本。", "phonetics": ["ɡɪt", "hɛlps", "ɪn", "ˈmænɪʤɪŋ", "ˈprɑʤɛkt", "ˈvɜrʒənz", "ɪˈfɛktɪvli"]},
    {"sentence": "Using APIs can greatly enhance the functionality of applications.", "translation": "使用API可以大大增强应用程序的功能。", "phonetics": ["ˈjuːzɪŋ", "eɪ-pi-aɪz", "kæn", "ˈɡreɪtli", "ɪnˈhæns", "ðə", "ˌfʌŋkʃəˈnælɪti", "ʌv", "ˌæpləˈkeɪʃənz"]},
    {"sentence": "Data visualization tools help in better data understanding.", "translation": "数据可视化工具有助于更好地理解数据。", "phonetics": ["ˈdeɪtə", "ˌvɪʒuəˈleɪʃən", "tulz", "hɛlp", "ɪn", "ˈbɛtər", "ˈdeɪtə", "ˌʌndərˈstændɪŋ"]},
    {"sentence": "Flask allows for flexible and rapid web development.", "translation": "Flask允许灵活和快速的Web开发。", "phonetics": ["flæsk", "əˈlaʊz", "fɔr", "ˈflɛksəbl", "ænd", "ˈræpɪd", "wɛb", "dɪˈvɛləpmənt"]},
    {"sentence": "Unit testing ensures that your code works as expected.", "translation": "单元测试确保你的代码按预期工作。", "phonetics": ["ˈjunɪt", "ˈtɛstɪŋ", "ɪnˈʃʊrz", "ðæt", "jʊr", "koʊd", "wɜrks", "æz", "ɪkˈspɛktɪd"]},
    {"sentence": "Virtual environments prevent dependency conflicts.", "translation": "虚拟环境防止依赖冲突。", "phonetics": ["ˈvɜrʧuəl", "ɪnˈvaɪrənmənts", "prɪˈvɛnt", "dɪˈpɛndənsi", "ˈkɑnflɪkts"]},
    {"sentence": "Beautiful Soup is a powerful library for web scraping.", "translation": "Beautiful Soup是一个强大的网页抓取库。", "phonetics": ["ˈbjutəfəl", "sup", "ɪz", "ə", "ˈpaʊərfəl", "ˈlaɪbrəri", "fɔr", "wɛb", "ˈskreɪpɪŋ"]}
]

# Load existing sentences
try:
    with open("sentence_list.json", "r", encoding="utf-8") as file:
        sentence_list = json.load(file)
except FileNotFoundError:
    sentence_list = []
except json.JSONDecodeError:
    sentence_list = []

# Add new sentences
sentence_list.extend(new_sentences)

# Save updated sentences
with open("sentence_list.json", "w", encoding="utf-8") as file:
    json.dump(sentence_list, file, ensure_ascii=False, indent=4)

print("Added new sentences to sentence_list.json")
