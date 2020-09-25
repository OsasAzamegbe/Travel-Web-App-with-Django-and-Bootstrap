import requests

content = []
titles = []


for i in range(20):
    paragraphs = (i % 4) + 2
    r = requests.get(f"https://hipsum.co/api/?type=hipster-centric&paras={paragraphs}")
    r1 = requests.get(f"http://www.hippieipsum.me/api/v1/get/{paragraphs}")
    r2 = requests.get(f"http://ramenipsum.herokuapp.com/paragraphs/{paragraphs}")
    r3 = requests.get(f"http://metaphorpsum.com/sentences/3")

    # print(" ".join(r2.text.split('\n')))
    content.append(" ".join(r.json()))
    content.append(" ".join(r1.json()['paragraphs']))
    content.append(" ".join(r2.text.split('\n')))
    titles.extend(r3.text.split('. '))

with open('posts.json', 'a') as f:
    f.write("[")
    for t, c in zip(titles, content):
        f.write('\n\t{\n\t\"title\": ' + f"\"{t}\",")
        f.write('\n\t\"content\": ' + f"\"{c}\"\n\t" + '},')
    f.write("\n]")


