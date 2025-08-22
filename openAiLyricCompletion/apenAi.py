
import openai
import time
from sk import my_sk  


openai.api_key = my_sk  

def lyric_completion(messages_list, steps=4, max_tokens=15, temperature=0, delay=0.1):
    """
    Lyric completion assistant. Returns updated messages_list.
    """
    for _ in range(steps):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages_list,
            max_tokens=max_tokens,
            n=1,
            temperature=temperature
        )
        lyric = completion.choices[0].message.content
        print(lyric)
        messages_list.append({"role": "assistant", "content": lyric})
        time.sleep(delay)

messages_list = [
    {"role": "system", "content": "I am Roxette lyric completion assistant. "
                                 "I will provide the next line in a song."},
    {"role": "user", "content": "I know there's something in the wake of your smile"},
    {"role": "assistant", "content": "I get a notion from the look in your eyes, yeah"},
    {"role": "user", "content": "You've built a love but that love falls apart"},
    {"role": "assistant", "content": "Your little piece of Heaven turns too dark"},
    {"role": "user", "content": "Listen to your"}
]

print("\nLyric Completion (temperature=0):")
messages_list = lyric_completion(messages_list, steps=4, temperature=0)

print("\nLyric Completion (temperature=2):")
messages_list = lyric_completion(messages_list, steps=4, temperature=2)
