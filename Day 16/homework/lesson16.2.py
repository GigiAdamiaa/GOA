question = int(input("1) შეკითხვის დასმისთვის ჩაწერეთ 1: "
                     "2) შეკითხვის დაიგნორებისთვის ჩაწერეთ 2: "
                     "3) გამოსვლისთვის ჩაწერეთ 3: "))


if question == 1:
    black_boy_question = int(input("რა კაცი ხარ?: "  "1) კაი ბიჭი ვარ" + " 2) დედიკოს ბიჭი ვარ" + " 3) შენ ვინ გეკითხება? : "))
    if black_boy_question == 1:
        print("შენ და ბენსიმონებში გაზმანული შავი ბიჭი დაძმაკაცდით") 
    elif black_boy_question == 2:
        print("შენ აგეხა ფული და დედასთან გაიქეცი")
    elif black_boy_question == 3:
        print("შენ გცემეს და სავაადმყოფოში გადაგიყვანეს")

if question == 2:
    print("შენ გცემა უბანმა რადგან შავი ბიჭის კითხვა დააიგნორე")
elif question == 3:
    print("თქვენ დატოვეთ უბნის ტერიტორა")