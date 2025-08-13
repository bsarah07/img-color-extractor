from flask import Flask, jsonify, request, render_template
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        file = request.files['photo']
        file.save(file.filename)

        img = Image.open(file.filename)
        img = img.resize((150, 150))

        pixels = np.array(img)
        pixels = pixels.reshape(-1, 3)
        colors, counts = np.unique(pixels,
                                   axis=0,
                                   return_counts=True)
        sorted_indices = np.argsort(-counts)
        top_colors = colors[sorted_indices][:10]
        top_colors_tuple = []
        for color in top_colors:
            r = int(color[0])
            g = int(color[1])
            b = int(color[2])
            color_tuple = f"{r}, {g}, {b}"

            top_colors_tuple.append(color_tuple)



        return render_template('index.html', colors = top_colors_tuple)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
