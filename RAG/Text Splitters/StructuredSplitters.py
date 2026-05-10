from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
The old railway station stood at the edge of the town like a forgotten memory. Rust covered the iron benches, and faded posters peeled slowly from the walls whenever the wind passed through the empty corridors. Every evening, a single train crossed the tracks without stopping, its distant whistle echoing through the quiet streets. The locals often said the station carried stories from another time, though no one could explain why the clocks there had stopped working years ago.

In the middle of the city market, a street musician played a violin beneath strings of yellow lights. People hurried past carrying bags of fruit, spices, and fresh bread, yet the melody managed to slow them down for a moment. Children gathered near the fountain while shopkeepers leaned against their doors listening quietly. As night approached, the music blended with the sound of rain beginning to fall on the stone pavement, turning the crowded market into something strangely peaceful.

Far beyond the hills, a research team worked inside a remote observatory surrounded by snow-covered mountains. Large computer screens displayed streams of data collected from deep space signals arriving every few seconds. The scientists barely slept, driven by the possibility that one unusual pattern might reveal something entirely unknown. Outside, the sky remained perfectly clear, filled with countless stars that seemed brighter in the silence of the frozen landscape.

"""
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0
)

docs = splitter.split_text(text)

print(docs)