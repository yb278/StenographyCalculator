import json

def load_json_file(json_file):
    with open(json_file, 'r', encoding='utf-8') as file: 
        return json.load(file)

def calculate_strokes(text, stroke_mapping, main_mapping, phonetic_strokes):
    words = text.lower().split()
    total_strokes = 0
    
    for word in words:
        word_strokes = 0
        
        for stroke, stroke_word in stroke_mapping.items():
            if word == stroke_word:
                word_strokes += 1 
                break
        else:
            if word in main_mapping:
                word_strokes += 1  
            else:
                i = 0
                while i < len(word):
                    found = False
                    for syllable in phonetic_strokes:
                        if word[i:i + len(syllable)] == syllable:
                            word_strokes += phonetic_strokes[syllable]
                            i += len(syllable)
                            found = True
                            break
                        
                    if not found:
                        word_strokes += 1
                        i += 1
        
        total_strokes += word_strokes
    
    return total_strokes


json_file_strokes = 'strokes.json'  
json_file_main = 'main.json' 

stroke_mapping = load_json_file(json_file_strokes)
main_mapping = load_json_file(json_file_main)

text_input = input("Enter your text: ")


phonetic_strokes = {

}

strokes_needed = calculate_strokes(text_input, stroke_mapping, main_mapping, phonetic_strokes)
print(f"Total strokes needed: {strokes_needed}")