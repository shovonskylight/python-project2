inputString = ("The metaverse is an emerging digital realm that is captivating imaginations worldwide. In essence, it represents a collective virtual universe where individuals can interact, socialize, work, and play within a vast interconnected space. Imagine a sprawling digital landscape, akin to a science fiction dream, where people utilize avatars to navigate this immersive environment. Within the metaverse, possibilities are seemingly limitless, encompassing everything from virtual reality gaming and educational experiences to social gatherings and commerce.Key technologies driving the metaverse include augmented reality (AR), virtual reality (VR), blockchain, and advanced artificial intelligence (AI). Companies like Facebook's Meta, Roblox, and Fortnite's Epic Games are already investing heavily in metaverse development, envisioning a future where it becomes an integral part of our daily lives. The metaverse's potential extends far beyond entertainment; it could revolutionize remote work, education, and even healthcare, offering new ways to connect and collaborate across distances.")
wordCount = inputString.count(" ")+1
sentenceCount = inputString.count(".")
totalCount = len(inputString)
averageCount = int(totalCount/wordCount)
print("no of word: ",wordCount)
print("no of sentence: ",sentenceCount)
print("average word length: ", averageCount)
