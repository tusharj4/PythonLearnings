# we should not include input method in
# the function as it makes it reusable, which we
# don't want, although if we want then we can do that
def emo(message):
    words=message.split(" ")
    emojis={
        ":)":"😭",
        ":(":"💦"
    }
    output=""
    for word in words:
        output+=emojis.get(word, word)+" "
    return output


m=input('>')
m=emo(m)
print(m)