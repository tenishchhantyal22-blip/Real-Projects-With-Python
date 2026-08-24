# Day to day Korean words for beginner
korean_dictionary = {
    "Hello": "안녕하세요 (An-nyeong-ha-se-yo)",
    "Yes": "네 (Ne)",
    "No": "아니요 (An-i-yo)",
    "Thank you": "감사합니다 (Gam-sa-ham-ni-da)",
    "I'm sorry": "죄송합니다 (Joe-song-ham-ni-da)",
    "Excuse me": "저기요 (Jeo-gi-yo)",
    "I'm ok": "괜찮아요 (Gwaen-chan-a-yo)",
    "Friend": "친구 (Chin-gu)",
    "Water": "물 (Mul)",
    "Coffee": "커피 (Keo-pi)",
    "Goodbye": "잘 가요 (Jal ga-yo)",
    "Please give me": "주세요 (Ju-se-yo)",
    "House": "집 (Jip)",
    "Bathroom": "화장실 (Hwa-jang-sil)",
    "Restaurant": "식당 (Sik-dang)",
    "Store": "가게 (Ga-ge)",
    "Person": "사람 (Sa-ram)",
    "Food": "밥 (Bap)",
    "Money": "돈 (Don)",
    "Car": "차 (Cha)",
    "Phone": "핸드폰 (Haen-deu-pon)",
    "Today": "오늘 (O-neul)",
    "Tomorrow": "내일 (Nae-il)",
    "Yesterday": "어제 (Eo-je)",
    "Now": "지금 (Ji-geum)",
    "Time": "시간 (Si-gan)",
    "Where": "어디 (Eo-di)",
    "Who": "누구 (Nu-gu)",
    "What": "무엇 (Mu-eot)",
    "When": "언제 (Eon-je)",
    "Why": "왜 (Wae)",
    "How": "어떻게 (Eo-tteoh-ge)",
    "How much": "얼마예요 (Eol-ma-ye-yo)",
    "Really": "진짜요 (Jin-jja-yo)",
    "Hungry": "배고파요 (Bae-go-pa-yo)",
    "I don't know": "몰라요 (Mol-la-yo)",
    "I know": "알아요 (Al-a-yo)",
    "Good": "좋아요 (Jo-a-yo)",
    "Bad": "나빠요 (Na-ppa-yo)",
    "Delicious": "맛있어요 (Mas-is-seo-yo)",
    "Hot": "더워요 (Deo-wo-yo)",
    "Cold": "추워요 (Chu-wo-yo)",
    "Tired": "피곤해요 (Pi-gon-hae-yo)",
    "Happy": "행복해요 (Haeng-bok-hae-yo)",
    "Beautiful": "예뻐요 (Yeo-ppeo-yo)",
    "Help": "도와주세요 (Do-wa-ju-se-yo)",
    "Wait a minute": "잠깐만요 (Jam-kkan-man-yo)",
    "Hurry up": "빨리요 (Ppal-li-yo)",
    "Welcome": "어서 오세요 (Eo-seo o-se-yo)",
    "Cheer up": "화이팅 (Hwai-ting)",
    "Computer": "컴퓨터 (Keom-pyu-teo)",
    "Internet": "인터넷 (In-teo-net)",
    "Program": "프로그램 (Peu-ro-gue-rem)",
    "Code": "코드 (Ko-deu)",
    "Data": "데이터 (Dei-teo)",
    "Network": "네트워크 (Ne-teu-wo-keu)",
    "Security": "보안 (Bo-an)",
    "Error": "오류 (O-ryu)",
    "System": "시스템 (Si-seu-tem)",
    "Software": "소프트웨어 (So-peu-teu-we-eo)",
    "Hardware": "하드웨어 (Ha-deu-we-eo)",
    "Server": "서버 (Seo-beo)",
    "Database": "데이터베이스 (Dei-teo-be-i-seu)",
    "Algorithm": "알고리즘 (Al-go-ri-jeum)",
    "Artificial intelligence": "인공지능 (In-gong-ji-neung)",
    "Web site": "웹사이트 (Wep-sa-i-teu)",
    "Application": "앱 (Aep)",
    "Screen": "화면 (Hwa-myeon)",
    "Keyboard": "키보드 (Ki-bo-deu)",
    "Mouse": "마우스 (Ma-u-seu)",
    "Password": "비밀번호 (Bi-mil-beon-ho)",
    "File": "파일 (Pa-il)",
    "Memory": "메모리 (Me-mo-ri)",
    "Cloud": "클라우드 (Keul-ra-u-deu)",
    "Search": "검색 (Geom-saek)",
    "Download": "다운로드 (Da-un-ro-deu)",
    "Upload": "업로드 (Eop-ro-deu)",
    "Development": "개발 (Gae-bal)",
    "Design": "디자인 (Di-ja-in)",
    "Function": "함수 (Ham-su)"
}
print("--Welcome to Korean Learning class (Type exit) to terminate class--")
while True:
    english_word = input("Enter any english word\n").strip().capitalize()

    if english_word == "Exit":
        print("Thank you! keep studying 😂")
        break
    if english_word in korean_dictionary:
        print(f"{english_word} = {korean_dictionary[english_word]}")
    else:
        print(f"Sorry!, {english_word} is not in dictionary yet")






