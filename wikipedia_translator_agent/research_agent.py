import wikipedia
from deep_translator import GoogleTranslator

def main():
    try:
        topic = input("Enter a topic to research: ").strip()
        if not topic:
            print("No topic entered. Exiting.")
            return

        print(f"Searching Wikipedia for '{topic}'...")
        search_results = wikipedia.search(topic)
        if not search_results:
            print(f"No results found for '{topic}'.")
            return

        first_result = search_results[0]
        print(f"Fetching summary for '{first_result}'...")
        try:
            summary = wikipedia.summary(first_result)
        except wikipedia.DisambiguationError as e:
            print(f"Your topic '{first_result}' resulted in a disambiguation. Suggestions:")
            for option in e.options[:5]:
                print(" -", option)
            return
        except wikipedia.PageError:
            print(f"The page for '{first_result}' could not be found.")
            return

        print("Translating summary to Turkish...")
        try:
            summary_tr = GoogleTranslator(source='auto', target='tr').translate(summary)
        except Exception as e:
            print("Translation error:", str(e))
            return

        filename = f"{first_result.replace(' ', '_')}_summary.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(summary_tr)
        print(f"Translated summary saved to '{filename}'.")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()