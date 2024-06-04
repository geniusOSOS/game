import json

sentence_list = [
    {
        "sentence": "I want to use my MacBook to train AI.",
        "translation": "我想用我的苹果笔记本电脑训练AI。",
        "phonetics": ["aɪ", "wɑnt", "tu", "juz", "maɪ", "ˈmækˌbʊk", "tu", "treɪn", "eɪˈaɪ"]
    },
    {
        "sentence": "Can you help me with the typing game?",
        "translation": "你能帮我处理打字游戏吗？",
        "phonetics": ["kæn", "ju", "hɛlp", "mi", "wɪð", "ðə", "ˈtaɪpɪŋ", "ɡeɪm"]
    },
    {
        "sentence": "I need to install TensorFlow.",
        "translation": "我需要安装TensorFlow。",
        "phonetics": ["aɪ", "nid", "tu", "ɪnˈstɔl", "ˈtɛnsərfloʊ"]
    },
    {
        "sentence": "The program is running on a Mac system.",
        "translation": "程序在Mac系统上运行。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ɪz", "ˈrʌnɪŋ", "ɑn", "ə", "mæk", "ˈsɪstəm"]
    },
    {
        "sentence": "I use PyCharm for Python development.",
        "translation": "我使用PyCharm进行Python开发。",
        "phonetics": ["aɪ", "juz", "ˈpaɪˌtʃɑrm", "fɔr", "ˈpaɪˌθɑn", "dɪˈvɛləpmənt"]
    },
    {
        "sentence": "There is an error in the code.",
        "translation": "代码中有一个错误。",
        "phonetics": ["ðɛr", "ɪz", "ən", "ˈɛrər", "ɪn", "ðə", "koʊd"]
    },
    {
        "sentence": "The typing game helps me learn English.",
        "translation": "打字游戏帮助我学习英语。",
        "phonetics": ["ðə", "ˈtaɪpɪŋ", "ɡeɪm", "hɛlps", "mi", "lɜrn", "ˈɪŋɡlɪʃ"]
    },
    {
        "sentence": "I want to add more words to the game.",
        "translation": "我想在游戏中添加更多单词。",
        "phonetics": ["aɪ", "wɑnt", "tu", "æd", "mɔr", "wɜrdz", "tu", "ðə", "ɡeɪm"]
    },
    {
        "sentence": "How can I fix this bug?",
        "translation": "我该如何修复这个错误？",
        "phonetics": ["haʊ", "kæn", "aɪ", "fɪks", "ðɪs", "bʌɡ"]
    },
    {
        "sentence": "The application is crashing unexpectedly.",
        "translation": "应用程序意外崩溃。",
        "phonetics": ["ðə", "ˌæplɪˈkeɪʃən", "ɪz", "ˈkræʃɪŋ", "ˌʌnɪkˈspɛktɪdli"]
    },
    {
        "sentence": "I need to update the sentence list.",
        "translation": "我需要更新句子列表。",
        "phonetics": ["aɪ", "nid", "tu", "ʌpˈdeɪt", "ðə", "ˈsɛntəns", "lɪst"]
    },
    {
        "sentence": "The game should read the sentences aloud.",
        "translation": "游戏应该朗读句子。",
        "phonetics": ["ðə", "ɡeɪm", "ʃʊd", "rid", "ðə", "ˈsɛntənsɪz", "əˈlaʊd"]
    },
    {
        "sentence": "How can I integrate the phonetics?",
        "translation": "我该如何整合音标？",
        "phonetics": ["haʊ", "kæn", "aɪ", "ˈɪntəˌɡreɪt", "ðə", "fəˈnɛtɪks"]
    },
    {
        "sentence": "The sentences are too long for one line.",
        "translation": "句子太长了，无法显示在一行。",
        "phonetics": ["ðə", "ˈsɛntənsɪz", "ɑr", "tu", "lɔŋ", "fɔr", "wʌn", "laɪn"]
    },
    {
        "sentence": "The program crashed because of an error.",
        "translation": "程序因错误而崩溃。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "kræʃt", "bɪˈkəz", "ʌv", "ən", "ˈɛrər"]
    },
    {
        "sentence": "I need to install additional libraries.",
        "translation": "我需要安装额外的库。",
        "phonetics": ["aɪ", "nid", "tu", "ɪnˈstɔl", "əˈdɪʃənəl", "ˈlaɪˌbrɛriz"]
    },
    {
        "sentence": "My typing speed is improving.",
        "translation": "我的打字速度在提高。",
        "phonetics": ["maɪ", "ˈtaɪpɪŋ", "spid", "ɪz", "ɪmˈpruvɪŋ"]
    },
    {
        "sentence": "The game should include a timer.",
        "translation": "游戏应该包括一个计时器。",
        "phonetics": ["ðə", "ɡeɪm", "ʃʊd", "ɪnˈklud", "ə", "ˈtaɪmər"]
    },
    {
        "sentence": "Can you recommend a good library?",
        "translation": "你能推荐一个好的库吗？",
        "phonetics": ["kæn", "ju", "ˌrɛkəˈmɛnd", "ə", "ɡʊd", "ˈlaɪˌbrɛri"]
    },
    {
        "sentence": "The translation should be accurate.",
        "translation": "翻译应该准确。",
        "phonetics": ["ðə", "trænsˈleɪʃən", "ʃʊd", "bi", "ˈækjərət"]
    },
    {
        "sentence": "I enjoy playing the typing game.",
        "translation": "我喜欢玩打字游戏。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈpleɪɪŋ", "ðə", "ˈtaɪpɪŋ", "ɡeɪm"]
    },
    {
        "sentence": "Let's add more functionality to the game.",
        "translation": "让我们为游戏添加更多功能。",
        "phonetics": ["lɛts", "æd", "mɔr", "ˌfʌŋkʃəˈnælɪti", "tu", "ðə", "ɡeɪm"]
    },
    {
        "sentence": "The game should help with learning English.",
        "translation": "游戏应该有助于学习英语。",
        "phonetics": ["ðə", "ɡeɪm", "ʃʊd", "hɛlp", "wɪð", "ˈlɜrnɪŋ", "ˈɪŋɡlɪʃ"]
    },
    {
        "sentence": "The code needs to be optimized.",
        "translation": "代码需要优化。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "ˈɑptəˌmaɪzd"]
    },
    {
        "sentence": "The program should support multiple languages.",
        "translation": "程序应支持多种语言。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "səˈpɔrt", "ˈmʌltəpəl", "ˈlæŋɡwɪdʒɪz"]
    },
    {
        "sentence": "I enjoy learning new programming languages.",
        "translation": "我喜欢学习新的编程语言。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈlɜrnɪŋ", "nu", "ˈproʊˌɡræmɪŋ", "ˈlæŋɡwɪdʒɪz"]
    },
    {
        "sentence": "How can I contribute to the project?",
        "translation": "我该如何为项目做出贡献？",
        "phonetics": ["haʊ", "kæn", "aɪ", "ˈkɑntrəˌbjut", "tu", "ðə", "ˈprɑdʒɛkt"]
    },
    {
        "sentence": "The user interface should be intuitive.",
        "translation": "用户界面应该直观。",
        "phonetics": ["ðə", "ˈjuzər", "ˈɪntərˌfeɪs", "ʃʊd", "bi", "ɪnˈtuɪtɪv"]
    },
    {
        "sentence": "We need to test the application thoroughly.",
        "translation": "我们需要彻底测试应用程序。",
        "phonetics": ["wi", "nid", "tu", "tɛst", "ðə", "ˌæplɪˈkeɪʃən", "ˈθɜroʊli"]
    },
    {
        "sentence": "I found a bug in the program.",
        "translation": "我在程序中发现了一个错误。",
        "phonetics": ["aɪ", "faʊnd", "ə", "bʌɡ", "ɪn", "ðə", "ˈproʊˌɡræm"]
    },
    {
        "sentence": "The code needs to be refactored.",
        "translation": "代码需要重构。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "riˈfæktərd"]
    },
    {
        "sentence": "I want to add a new feature to the game.",
        "translation": "我想在游戏中添加一个新功能。",
        "phonetics": ["aɪ", "wɑnt", "tu", "æd", "ə", "nu", "ˈfitʃər", "tu", "ðə", "ɡeɪm"]
    },
    {
        "sentence": "The program should handle errors gracefully.",
        "translation": "程序应优雅地处理错误。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "ˈhændəl", "ˈɛrərz", "ˈɡreɪsfəli"]
    },
    {
        "sentence": "I enjoy coding in Python.",
        "translation": "我喜欢用Python编程。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈkoʊdɪŋ", "ɪn", "ˈpaɪˌθɑn"]
    },
    {
        "sentence": "The typing game helps me practice typing.",
        "translation": "打字游戏帮助我练习打字。",
        "phonetics": ["ðə", "ˈtaɪpɪŋ", "ɡeɪm", "hɛlps", "mi", "ˈpræktɪs", "ˈtaɪpɪŋ"]
    },
    {
        "sentence": "The application should be user-friendly.",
        "translation": "应用程序应对用户友好。",
        "phonetics": ["ðə", "ˌæplɪˈkeɪʃən", "ʃʊd", "bi", "ˈjuzər-ˈfrɛndli"]
    },
    {
        "sentence": "I need to learn more about cybersecurity.",
        "translation": "我需要了解更多关于网络安全的知识。",
        "phonetics": ["aɪ", "nid", "tu", "lɜrn", "mɔr", "əˈbaʊt", "ˌsaɪbərsɪˈkjʊrɪti"]
    },
    {
        "sentence": "How can I secure my application?",
        "translation": "我该如何保护我的应用程序？",
        "phonetics": ["haʊ", "kæn", "aɪ", "sɪˈkjʊr", "maɪ", "ˌæplɪˈkeɪʃən"]
    },
    {
        "sentence": "The code should be well-documented.",
        "translation": "代码应有良好的文档记录。",
        "phonetics": ["ðə", "koʊd", "ʃʊd", "bi", "wɛl-ˈdɑkjəˌmɛntɪd"]
    },
    {
        "sentence": "I need to fix the bugs in the program.",
        "translation": "我需要修复程序中的错误。",
        "phonetics": ["aɪ", "nid", "tu", "fɪks", "ðə", "bʌɡz", "ɪn", "ðə", "ˈproʊˌɡræm"]
    },
    {
        "sentence": "The user experience should be seamless.",
        "translation": "用户体验应该是无缝的。",
        "phonetics": ["ðə", "ˈjuzər", "ɪkˈspɪriəns", "ʃʊd", "bi", "ˈsimləs"]
    },
    {
        "sentence": "I am learning how to develop applications.",
        "translation": "我正在学习如何开发应用程序。",
        "phonetics": ["aɪ", "æm", "ˈlɜrnɪŋ", "haʊ", "tu", "dɪˈvɛləp", "ˌæplɪˈkeɪʃənz"]
    },
    {
        "sentence": "The program needs to be tested thoroughly.",
        "translation": "程序需要彻底测试。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "nidz", "tu", "bi", "ˈtɛstɪd", "ˈθɜroʊli"]
    },
    {
        "sentence": "I want to create a new project.",
        "translation": "我想创建一个新项目。",
        "phonetics": ["aɪ", "wɑnt", "tu", "kriˈeɪt", "ə", "nu", "ˈprɑdʒɛkt"]
    },
    {
        "sentence": "The game should provide feedback to users.",
        "translation": "游戏应该向用户提供反馈。",
        "phonetics": ["ðə", "ɡeɪm", "ʃʊd", "prəˈvaɪd", "ˈfidˌbæk", "tu", "ˈjuzərz"]
    },
    {
        "sentence": "I need to debug the application.",
        "translation": "我需要调试应用程序。",
        "phonetics": ["aɪ", "nid", "tu", "diˈbʌɡ", "ðə", "ˌæplɪˈkeɪʃən"]
    },
    {
        "sentence": "The program should be scalable.",
        "translation": "程序应该具有可扩展性。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "bi", "ˈskeɪləbəl"]
    },
    {
        "sentence": "I want to add more features to the game.",
        "translation": "我想在游戏中添加更多功能。",
        "phonetics": ["aɪ", "wɑnt", "tu", "æd", "mɔr", "ˈfitʃərz", "tu", "ðə", "ɡeɪm"]
    },
    {
        "sentence": "The code needs to be refactored for clarity.",
        "translation": "代码需要重构以提高清晰度。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "riˈfæktərd", "fɔr", "ˈklærəti"]
    },
    {
        "sentence": "I enjoy solving programming challenges.",
        "translation": "我喜欢解决编程挑战。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈsɑlvɪŋ", "ˈproʊˌɡræmɪŋ", "ˈtʃælɪndʒɪz"]
    },
    {
        "sentence": "The application should be responsive.",
        "translation": "应用程序应该响应迅速。",
        "phonetics": ["ðə", "ˌæplɪˈkeɪʃən", "ʃʊd", "bi", "rɪˈspɑnsɪv"]
    },
    {
        "sentence": "I need to learn how to optimize code.",
        "translation": "我需要学习如何优化代码。",
        "phonetics": ["aɪ", "nid", "tu", "lɜrn", "haʊ", "tu", "ˈɑptəˌmaɪz", "koʊd"]
    },
    {
        "sentence": "The game should include various levels.",
        "translation": "游戏应该包括不同的关卡。",
        "phonetics": ["ðə", "ɡeɪm", "ʃʊd", "ɪnˈklud", "ˈvɛriəs", "ˈlɛvəlz"]
    },
    {
        "sentence": "I want to improve my typing accuracy.",
        "translation": "我想提高我的打字准确性。",
        "phonetics": ["aɪ", "wɑnt", "tu", "ɪmˈpruv", "maɪ", "ˈtaɪpɪŋ", "ˈækjərəsi"]
    },
    {
        "sentence": "The program should be cross-platform.",
        "translation": "程序应具有跨平台能力。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "bi", "krɔs-ˈplætfɔrm"]
    },
    {
        "sentence": "I enjoy learning about new technologies.",
        "translation": "我喜欢学习新技术。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈlɜrnɪŋ", "əˈbaʊt", "nu", "tɛkˈnɑlədʒiz"]
    },
    {
        "sentence": "The user interface needs to be improved.",
        "translation": "用户界面需要改进。",
        "phonetics": ["ðə", "ˈjuzər", "ˈɪntərˌfeɪs", "nidz", "tu", "bi", "ɪmˈpruvd"]
    },
    {
        "sentence": "I need to update the software regularly.",
        "translation": "我需要定期更新软件。",
        "phonetics": ["aɪ", "nid", "tu", "ʌpˈdeɪt", "ðə", "ˈsɔftˌwɛr", "ˈrɛɡjələrli"]
    },
    {
        "sentence": "The program should be efficient.",
        "translation": "程序应该高效。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "bi", "ɪˈfɪʃənt"]
    },
    {
        "sentence": "I enjoy working on challenging projects.",
        "translation": "我喜欢从事具有挑战性的项目。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈwɜrkɪŋ", "ɑn", "ˈtʃælɪndʒɪŋ", "ˈprɑdʒɛkts"]
    },
    {
        "sentence": "The code needs to be reviewed for quality.",
        "translation": "代码需要进行质量审查。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "rɪˈvjud", "fɔr", "ˈkwɑləti"]
    },
    {
        "sentence": "I want to create a user-friendly interface.",
        "translation": "我想创建一个用户友好的界面。",
        "phonetics": ["aɪ", "wɑnt", "tu", "kriˈeɪt", "ə", "ˈjuzər-ˈfrɛndli", "ˈɪntərˌfeɪs"]
    },
    {
        "sentence": "The program should be easy to use.",
        "translation": "程序应该易于使用。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "bi", "ˈizi", "tu", "juz"]
    },
    {
        "sentence": "I need to learn more about machine learning.",
        "translation": "我需要了解更多关于机器学习的知识。",
        "phonetics": ["aɪ", "nid", "tu", "lɜrn", "mɔr", "əˈbaʊt", "məˈʃin", "ˈlɜrnɪŋ"]
    },
    {
        "sentence": "The game should be engaging for users.",
        "translation": "游戏应该对用户有吸引力。",
        "phonetics": ["ðə", "ɡeɪm", "ʃʊd", "bi", "ɪnˈɡeɪdʒɪŋ", "fɔr", "ˈjuzərz"]
    },
    {
        "sentence": "I enjoy learning new skills.",
        "translation": "我喜欢学习新技能。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈlɜrnɪŋ", "nu", "skɪlz"]
    },
    {
        "sentence": "The application should have a clean design.",
        "translation": "应用程序应该有一个干净的设计。",
        "phonetics": ["ðə", "ˌæplɪˈkeɪʃən", "ʃʊd", "hæv", "ə", "klin", "dɪˈzaɪn"]
    },
    {
        "sentence": "I need to debug the code for errors.",
        "translation": "我需要调试代码以查找错误。",
        "phonetics": ["aɪ", "nid", "tu", "diˈbʌɡ", "ðə", "koʊd", "fɔr", "ˈɛrərz"]
    },
    {
        "sentence": "The program should be reliable.",
        "translation": "程序应该可靠。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "bi", "rɪˈlaɪəbəl"]
    },
    {
        "sentence": "I enjoy working on innovative projects.",
        "translation": "我喜欢从事创新项目。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈwɜrkɪŋ", "ɑn", "ˈɪnəˌveɪtɪv", "ˈprɑdʒɛkts"]
    },
    {
        "sentence": "The code needs to be optimized for performance.",
        "translation": "代码需要针对性能进行优化。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "ˈɑptəˌmaɪzd", "fɔr", "pərˈfɔrməns"]
    },
    {
        "sentence": "I want to create a high-quality application.",
        "translation": "我想创建一个高质量的应用程序。",
        "phonetics": ["aɪ", "wɑnt", "tu", "kriˈeɪt", "ə", "haɪ-ˈkwɑləti", "ˌæplɪˈkeɪʃən"]
    },
    {
        "sentence": "The program should be flexible.",
        "translation": "程序应该灵活。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "bi", "ˈflɛksəbəl"]
    },
    {
        "sentence": "I enjoy solving complex problems.",
        "translation": "我喜欢解决复杂问题。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈsɑlvɪŋ", "ˈkɑmplɛks", "ˈprɑbləmz"]
    },
    {
        "sentence": "The application should be robust.",
        "translation": "应用程序应该健壮。",
        "phonetics": ["ðə", "ˌæplɪˈkeɪʃən", "ʃʊd", "bi", "roʊˈbʌst"]
    },
    {
        "sentence": "I need to learn more about software development.",
        "translation": "我需要了解更多关于软件开发的知识。",
        "phonetics": ["aɪ", "nid", "tu", "lɜrn", "mɔr", "əˈbaʊt", "ˈsɔftˌwɛr", "dɪˈvɛləpmənt"]
    },
    {
        "sentence": "The code needs to be modular.",
        "translation": "代码需要模块化。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "ˈmɑdʒələr"]
    },
    {
        "sentence": "I want to add more functionality to the application.",
        "translation": "我想为应用程序添加更多功能。",
        "phonetics": ["aɪ", "wɑnt", "tu", "æd", "mɔr", "ˌfʌŋkʃəˈnælɪti", "tu", "ðə", "ˌæplɪˈkeɪʃən"]
    },
    {
        "sentence": "The program should be secure.",
        "translation": "程序应该安全。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "bi", "sɪˈkjʊr"]
    },
    {
        "sentence": "I enjoy working on open-source projects.",
        "translation": "我喜欢从事开源项目。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈwɜrkɪŋ", "ɑn", "ˈoʊpən-ˈsɔrs", "ˈprɑdʒɛkts"]
    },
    {
        "sentence": "The code needs to be efficient and clean.",
        "translation": "代码需要高效且简洁。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "ɪˈfɪʃənt", "ænd", "klin"]
    },
    {
        "sentence": "I want to create a seamless user experience.",
        "translation": "我想创建无缝的用户体验。",
        "phonetics": ["aɪ", "wɑnt", "tu", "kriˈeɪt", "ə", "ˈsimləs", "ˈjuzər", "ɪkˈspɪriəns"]
    },
    {
        "sentence": "The program should handle large datasets.",
        "translation": "程序应处理大型数据集。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "ˈhændəl", "lɑrdʒ", "ˈdeɪtəˌsɛts"]
    },
    {
        "sentence": "I need to update the documentation regularly.",
        "translation": "我需要定期更新文档。",
        "phonetics": ["aɪ", "nid", "tu", "ʌpˈdeɪt", "ðə", "ˌdɑkjəmənˈteɪʃən", "ˈrɛɡjələrli"]
    },
    {
        "sentence": "The game should be fun and educational.",
        "translation": "游戏应该既有趣又有教育意义。",
        "phonetics": ["ðə", "ɡeɪm", "ʃʊd", "bi", "fʌn", "ænd", "ˌɛdʒəˈkeɪʃənəl"]
    },
    {
        "sentence": "I enjoy learning about new programming paradigms.",
        "translation": "我喜欢学习新的编程范式。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈlɜrnɪŋ", "əˈbaʊt", "nu", "ˈproʊˌɡræmɪŋ", "ˈpærəˌdaɪmz"]
    },
    {
        "sentence": "The user interface should be intuitive and responsive.",
        "translation": "用户界面应该直观且响应迅速。",
        "phonetics": ["ðə", "ˈjuzər", "ˈɪntərˌfeɪs", "ʃʊd", "bi", "ɪnˈtuɪtɪv", "ænd", "rɪˈspɑnsɪv"]
    },
    {
        "sentence": "I need to learn more about database management.",
        "translation": "我需要了解更多关于数据库管理的知识。",
        "phonetics": ["aɪ", "nid", "tu", "lɜrn", "mɔr", "əˈbaʊt", "ˈdeɪtəˌbeɪs", "ˈmænɪdʒmənt"]
    },
    {
        "sentence": "The code needs to be scalable and maintainable.",
        "translation": "代码需要具有可扩展性和可维护性。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "ˈskeɪləbəl", "ænd", "meɪnˈteɪnəbəl"]
    },
    {
        "sentence": "I want to create a feature-rich application.",
        "translation": "我想创建一个功能丰富的应用程序。",
        "phonetics": ["aɪ", "wɑnt", "tu", "kriˈeɪt", "ə", "ˈfitʃər-rɪtʃ", "ˌæplɪˈkeɪʃən"]
    },
    {
        "sentence": "The program should be compatible with various platforms.",
        "translation": "程序应与各种平台兼容。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "bi", "kəmˈpætəbəl", "wɪð", "ˈvɛriəs", "ˈplætfɔrmz"]
    },
    {
        "sentence": "I enjoy working on software development projects.",
        "translation": "我喜欢从事软件开发项目。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈwɜrkɪŋ", "ɑn", "ˈsɔftˌwɛr", "dɪˈvɛləpmənt", "ˈprɑdʒɛkts"]
    },
    {
        "sentence": "The code needs to be reviewed regularly.",
        "translation": "代码需要定期审查。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "rɪˈvjud", "ˈrɛɡjələrli"]
    },
    {
        "sentence": "I want to create an innovative solution.",
        "translation": "我想创建一个创新的解决方案。",
        "phonetics": ["aɪ", "wɑnt", "tu", "kriˈeɪt", "ən", "ˈɪnəˌveɪtɪv", "səˈluʃən"]
    },
    {
        "sentence": "The program should be optimized for speed.",
        "translation": "程序应该针对速度进行优化。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "bi", "ˈɑptəˌmaɪzd", "fɔr", "spid"]
    },
    {
        "sentence": "I enjoy working on collaborative projects.",
        "translation": "我喜欢从事合作项目。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈwɜrkɪŋ", "ɑn", "kəˈlæbrəˌtɪv", "ˈprɑdʒɛkts"]
    },
    {
        "sentence": "The code needs to be well-structured.",
        "translation": "代码需要结构良好。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "wɛl-ˈstrʌktʃərd"]
    },
    {
        "sentence": "I want to create a user-centric application.",
        "translation": "我想创建一个以用户为中心的应用程序。",
        "phonetics": ["aɪ", "wɑnt", "tu", "kriˈeɪt", "ə", "ˈjuzər-ˈsɛntrɪk", "ˌæplɪˈkeɪʃən"]
    },
    {
        "sentence": "The program should handle concurrent users efficiently.",
        "translation": "程序应有效地处理并发用户。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "ˈhændəl", "kənˈkɜrənt", "ˈjuzərz", "ɪˈfɪʃəntli"]
    },
    {
        "sentence": "I need to learn more about front-end development.",
        "translation": "我需要了解更多关于前端开发的知识。",
        "phonetics": ["aɪ", "nid", "tu", "lɜrn", "mɔr", "əˈbaʊt", "frʌnt-ɛnd", "dɪˈvɛləpmənt"]
    },
    {
        "sentence": "The code needs to be maintainable and scalable.",
        "translation": "代码需要具有可维护性和可扩展性。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "meɪnˈteɪnəbəl", "ænd", "ˈskeɪləbəl"]
    },
    {
        "sentence": "I want to create a feature-rich and user-friendly application.",
        "translation": "我想创建一个功能丰富且用户友好的应用程序。",
        "phonetics": ["aɪ", "wɑnt", "tu", "kriˈeɪt", "ə", "ˈfitʃər-rɪtʃ", "ænd", "ˈjuzər-ˈfrɛndli", "ˌæplɪˈkeɪʃən"]
    },
    {
        "sentence": "The program should be compatible with various devices.",
        "translation": "程序应与各种设备兼容。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "bi", "kəmˈpætəbəl", "wɪð", "ˈvɛriəs", "dɪˈvaɪsɪz"]
    },
    {
        "sentence": "I enjoy working on innovative software solutions.",
        "translation": "我喜欢从事创新的软件解决方案。",
        "phonetics": ["aɪ", "ɪnˈdʒɔɪ", "ˈwɜrkɪŋ", "ɑn", "ˈɪnəˌveɪtɪv", "ˈsɔftˌwɛr", "səˈluʃənz"]
    },
    {
        "sentence": "The code needs to be optimized for both performance and maintainability.",
        "translation": "代码需要针对性能和可维护性进行优化。",
        "phonetics": ["ðə", "koʊd", "nidz", "tu", "bi", "ˈɑptəˌmaɪzd", "fɔr", "boʊθ", "pərˈfɔrməns", "ænd", "meɪnˈteɪnəbɪlɪti"]
    },
    {
        "sentence": "I want to create a seamless and intuitive user experience.",
        "translation": "我想创建无缝且直观的用户体验。",
        "phonetics": ["aɪ", "wɑnt", "tu", "kriˈeɪt", "ə", "ˈsimləs", "ænd", "ɪnˈtuɪtɪv", "ˈjuzər", "ɪkˈspɪriəns"]
    },
    {
        "sentence": "The program should handle large-scale data efficiently.",
        "translation": "程序应高效地处理大规模数据。",
        "phonetics": ["ðə", "ˈproʊˌɡræm", "ʃʊd", "ˈhændəl", "lɑrdʒ-skeɪl", "ˈdeɪtə", "ɪˈfɪʃəntli"]
    },
    {
        "sentence": "I need to update the codebase regularly.",
        "translation": "我需要定期更新代码库。",
        "phonetics": ["aɪ", "nid", "tu", "ʌpˈdeɪt", "ðə", "ˈkoʊdˌbeɪs", "ˈrɛɡjələrli"]
    },
    {
        "sentence": "The game should be engaging and informative.",
        "translation": "游戏应该既有吸引力又有信息量。",
        "phonetics": ["ðə", "ɡeɪm", "ʃʊd", "bi", "ɪnˈɡeɪdʒɪŋ", "ænd", "ɪnˈfɔrmətɪv"]
    }
]

# 将句子库保存为JSON文件
with open("sentence_list.json", "w", encoding="utf-8") as file:
    json.dump(sentence_list, file, ensure_ascii=False, indent=4)

print("句子库已生成并保存到'sentence_list.json'文件中。")
