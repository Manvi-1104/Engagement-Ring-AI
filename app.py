# # # from flask import Flask, request, jsonify, send_file
# # # from diffusers import StableDiffusionPipeline
# # # import torch
# # # from PIL import Image
# # # import io
# # #
# # # app = Flask(__name__)
# # #
# # # # Load the fine-tuned model
# # # model_path = "/Users/manvi11/Downloads/Dataset/fineTuned"
# # # pipe = StableDiffusionPipeline.from_pretrained(model_path)
# # # pipe = pipe.to("cpu")  # Use CPU since CUDA is not available
# # # seed = 42  # Fixed seed for reproducibility
# # #
# # # # Define allowed keywords
# # # allowed_keywords = [
# # #     "ring", "engagement", "diamond", "gold", "silver", "jewelry", "precious", "band"
# # # ]
# # #
# # # @app.route('/')
# # # def home():
# # #     return '''
# # #     <html>
# # #     <body>
# # #         <h1>Text-to-Image Generator</h1>
# # #         <input type="text" id="prompt" placeholder="Describe the ring you want...">
# # #         <button onclick="generateImage()">Generate Image</button>
# # #         <div id="loading" style="display:none;">Loading...</div>
# # #         <div id="result"></div>
# # #         <script>
# # #             async function generateImage() {
# # #                 const prompt = document.getElementById('prompt').value;
# # #                 document.getElementById('loading').style.display = 'block';
# # #                 document.getElementById('result').innerHTML = '';
# # #                 const response = await fetch('/generate_image', {
# # #                     method: 'POST',
# # #                     headers: { 'Content-Type': 'application/json' },
# # #                     body: JSON.stringify({ prompt: prompt })
# # #                 });
# # #                 document.getElementById('loading').style.display = 'none';
# # #                 if (response.ok) {
# # #                     const data = await response.blob();
# # #                     const url = URL.createObjectURL(data);
# # #                     const img = document.createElement('img');
# # #                     img.src = url;
# # #                     document.getElementById('result').innerHTML = '';
# # #                     document.getElementById('result').appendChild(img);
# # #                 } else {
# # #                     const error = await response.json();
# # #                     alert('Error: ' + error.message);
# # #                 }
# # #             }
# # #         </script>
# # #     </body>
# # #     </html>
# # #     '''
# # #
# # # @app.route('/generate_image', methods=['POST'])
# # # def generate_image():
# # #     prompt = request.json.get('prompt', '')
# # #     if any(keyword in prompt.lower() for keyword in allowed_keywords):
# # #         try:
# # #             generator = torch.manual_seed(seed)
# # #             result = pipe(prompt=prompt)
# # #             image = result.images[0]
# # #             img_io = io.BytesIO()
# # #             image.save(img_io, 'PNG')
# # #             img_io.seek(0)
# # #             return send_file(img_io, mimetype='image/png')
# # #         except Exception as e:
# # #             return jsonify({"error": str(e)}), 500
# # #     else:
# # #         return jsonify({"message": "Sorry, not found. Please include keywords related to rings."}), 400
# # #
# # # # Run Flask app
# # # if __name__ == '__main__':
# # #     app.run(port=5000)
# from flask import Flask, request, jsonify, send_file
# from diffusers import StableDiffusionPipeline
# import torch
# from PIL import Image
# import io
# import zipfile
#
# app = Flask(__name__)
#
# # Load the fine-tuned model
# model_path = "/Users/manvi11/Downloads/Dataset/fineTuned"
# pipe = StableDiffusionPipeline.from_pretrained(model_path)
# pipe = pipe.to("cpu")  # Use CPU since CUDA is not available
# seed = 42  # Fixed seed for reproducibility
#
# # Define allowed keywords
# allowed_keywords = [
#     "engagement", "wedding", "solitaire", "halo", "band", "promise", "cocktail", "eternity",
#     "vintage", "designer", "classic", "custom", "birthstone", "anniversary", "stackable", "statement",
#     "matching", "gold", "silver", "platinum", "palladium", "titanium", "tungsten", "stainless steel",
#     "bronze", "brass", "copper", "diamond", "round cut", "princess cut", "emerald cut", "cushion cut",
#     "marquise cut", "asscher cut", "pear cut", "sapphire", "ruby", "emerald", "amethyst", "topaz",
#     "garnet", "opal", "aquamarine", "peridot", "tourmaline", "citrine", "sparkling", "brilliant",
#     "elegant", "intricate", "minimalist", "bold", "modern", "antique", "handcrafted", "custom-made",
#     "unique", "luxurious", "refined", "polished", "textured", "engraved", "filigree", "bezel set",
#     "prong set", "channel set", "flush set", "pavé set", "three-stone", "flush fit", "adjustable",
#     "casual", "formal", "bridal", "everyday", "high fashion", "artistic", "personalized", "classic",
#     "contemporary", "retro", "art deco", "gothic", "romantic", "ring size", "band width", "gemstone setting",
#     "craftsmanship", "jewel", "precious metals", "semi-precious stones", "accent stones", "milgrain",
#     "inlay", "harmony", "anniversary band", "wedding band", "ring", "rings"
# ]
#
#
# @app.route('/')
# def home():
#     return '''
#     <html>
#     <head>
#         <style>
#             body {
#                 font-family: Arial, sans-serif;
#                 background-color: #f2f2f2;
#                 margin: 0;
#                 padding: 0;
#                 display: flex;
#                 justify-content: center;
#                 align-items: center;
#                 height: 100vh;
#                 flex-direction: column;
#             }
#             h1 {
#                 color: #333;
#             }
#             input[type="text"] {
#                 width: 300px;
#                 padding: 10px;
#                 border: 1px solid #ccc;
#                 border-radius: 5px;
#                 margin-bottom: 10px;
#                 font-size: 16px;
#             }
#             input[type="range"] {
#                 width: 300px;
#                 margin-bottom: 10px;
#             }
#             button {
#                 padding: 10px 20px;
#                 border: none;
#                 border-radius: 5px;
#                 background-color: #4CAF50;
#                 color: white;
#                 font-size: 16px;
#                 cursor: pointer;
#                 transition: background-color 0.3s;
#             }
#             button:hover {
#                 background-color: #45a049;
#             }
#             #loading {
#                 display: none;
#                 font-size: 16px;
#                 color: #666;
#                 margin-top: 10px;
#             }
#             #result img {
#                 max-width: 100%;
#                 border: 1px solid #ddd;
#                 border-radius: 5px;
#                 margin-top: 10px;
#             }
#         </style>
#     </head>
#     <body>
#         <h1>Text-to-Image Generator</h1>
#         <input type="text" id="prompt" placeholder="Describe the ring you want...">
#         <input type="range" id="numImages" min="1" max="10" value="1" oninput="this.nextElementSibling.value = this.value">
#         <output>1</output>
#         <button onclick="generateImage()">Generate Image</button>
#         <div id="loading">Loading...</div>
#         <div id="result"></div>
#         <script>
#             async function generateImage() {
#                 const prompt = document.getElementById('prompt').value;
#                 const numImages = document.getElementById('numImages').value;
#                 document.getElementById('loading').style.display = 'block';
#                 document.getElementById('result').innerHTML = '';
#                 const response = await fetch('/generate_image', {
#                     method: 'POST',
#                     headers: { 'Content-Type': 'application/json' },
#                     body: JSON.stringify({ prompt: prompt, num_images: numImages })
#                 });
#                 document.getElementById('loading').style.display = 'none';
#                 if (response.ok) {
#                     const data = await response.blob();
#                     const url = URL.createObjectURL(data);
#                     const link = document.createElement('a');
#                     link.href = url;
#                     link.download = 'generated_images.zip';
#                     link.click();
#                 } else {
#                     const error = await response.json();
#                     alert('Error: ' + error.message);
#                 }
#             }
#         </script>
#     </body>
#     </html>
#     '''
#
#
# @app.route('/generate_image', methods=['POST'])
# def generate_image():
#     prompt = request.json.get('prompt', '')
#     num_images = int(request.json.get('num_images', 1))
#     if any(keyword in prompt.lower() for keyword in allowed_keywords):
#         try:
#             images = []
#             generator = torch.manual_seed(seed)
#             for _ in range(num_images):
#                 result = pipe(prompt=prompt)
#                 images.append(result.images[0])
#
#             # Save images to a zip file
#             img_io = io.BytesIO()
#             with zipfile.ZipFile(img_io, 'w') as zipf:
#                 for i, img in enumerate(images):
#                     img_byte_arr = io.BytesIO()
#                     img.save(img_byte_arr, format='PNG')
#                     zipf.writestr(f'image_{i + 1}.png', img_byte_arr.getvalue())
#             img_io.seek(0)
#             return send_file(img_io, mimetype='application/zip', as_attachment=True,
#                              download_name='generated_images.zip')
#         except Exception as e:
#             return jsonify({"error": str(e)}), 500
#     else:
#         return jsonify({"message": "Sorry, not found. Please include keywords related to rings."}), 400
#
#
# # Run Flask app
# if __name__ == '__main__':
#     app.run(port=5000)
#
# # from flask import Flask, request, jsonify, send_file
# # from diffusers import StableDiffusionPipeline
# # import torch
# # from PIL import Image
# # import io
# # import zipfile
# # from accelerate import Accelerator
# #
# # app = Flask(__name__)
# #
# # # Initialize Accelerator
# # accelerator = Accelerator()
# #
# # # Load the fine-tuned model
# # model_path = "/Users/manvi11/Downloads/Dataset/fineTuned"
# # pipe = StableDiffusionPipeline.from_pretrained(model_path)
# # pipe.to(accelerator.device)
# # seed = 42  # Fixed seed for reproducibility
# #
# # # Define allowed keywords
# # allowed_keywords = [
# #     "ring", "engagement", "diamond", "gold", "silver", "jewelry", "precious", "band"
# # ]
# #
# #
# # @app.route('/')
# # def home():
# #     return '''
# #     <html>
# #     <head>
# #         <style>
# #             body {
# #                 font-family: Arial, sans-serif;
# #                 background-color: #f2f2f2;
# #                 margin: 0;
# #                 padding: 0;
# #                 display: flex;
# #                 justify-content: center;
# #                 align-items: center;
# #                 height: 100vh;
# #                 flex-direction: column;
# #             }
# #             h1 {
# #                 color: #333;
# #             }
# #             input[type="text"] {
# #                 width: 300px;
# #                 padding: 10px;
# #                 border: 1px solid #ccc;
# #                 border-radius: 5px;
# #                 margin-bottom: 10px;
# #                 font-size: 16px;
# #             }
# #             input[type="range"] {
# #                 width: 300px;
# #                 margin-bottom: 10px;
# #             }
# #             button {
# #                 padding: 10px 20px;
# #                 border: none;
# #                 border-radius: 5px;
# #                 background-color: #4CAF50;
# #                 color: white;
# #                 font-size: 16px;
# #                 cursor: pointer;
# #                 transition: background-color 0.3s;
# #             }
# #             button:hover {
# #                 background-color: #45a049;
# #             }
# #             #loading {
# #                 display: none;
# #                 font-size: 16px;
# #                 color: #666;
# #                 margin-top: 10px;
# #             }
# #             #result img {
# #                 max-width: 100%;
# #                 border: 1px solid #ddd;
# #                 border-radius: 5px;
# #                 margin-top: 10px;
# #             }
# #         </style>
# #     </head>
# #     <body>
# #         <h1>Text-to-Image Generator</h1>
# #         <input type="text" id="prompt" placeholder="Describe the ring you want...">
# #         <input type="range" id="numImages" min="1" max="10" value="1" oninput="this.nextElementSibling.value = this.value">
# #         <output>1</output>
# #         <button onclick="generateImage()">Generate Image</button>
# #         <div id="loading">Loading...</div>
# #         <div id="result"></div>
# #         <script>
# #             async function generateImage() {
# #                 const prompt = document.getElementById('prompt').value;
# #                 const numImages = document.getElementById('numImages').value;
# #                 document.getElementById('loading').style.display = 'block';
# #                 document.getElementById('result').innerHTML = '';
# #                 const response = await fetch('/generate_image', {
# #                     method: 'POST',
# #                     headers: { 'Content-Type': 'application/json' },
# #                     body: JSON.stringify({ prompt: prompt, num_images: numImages })
# #                 });
# #                 document.getElementById('loading').style.display = 'none';
# #                 if (response.ok) {
# #                     const data = await response.blob();
# #                     const url = URL.createObjectURL(data);
# #                     const link = document.createElement('a');
# #                     link.href = url;
# #                     link.download = 'generated_images.zip';
# #                     link.click();
# #                 } else {
# #                     const error = await response.json();
# #                     alert('Error: ' + error.message);
# #                 }
# #             }
# #         </script>
# #     </body>
# #     </html>
# #     '''
# #
# #
# # @app.route('/generate_image', methods=['POST'])
# # def generate_image():
# #     prompt = request.json.get('prompt', '')
# #     num_images = int(request.json.get('num_images', 1))
# #     if any(keyword in prompt.lower() for keyword in allowed_keywords):
# #         try:
# #             images = []
# #             generator = torch.Generator().manual_seed(seed)
# #             for _ in range(num_images):
# #                 with accelerator.autocast():
# #                     result = pipe(prompt=prompt, generator=generator)
# #                 images.append(result.images[0])
# #
# #             # Save images to a zip file
# #             img_io = io.BytesIO()
# #             with zipfile.ZipFile(img_io, 'w') as zipf:
# #                 for i, img in enumerate(images):
# #                     img_byte_arr = io.BytesIO()
# #                     img.save(img_byte_arr, format='PNG')
# #                     zipf.writestr(f'image_{i + 1}.png', img_byte_arr.getvalue())
# #             img_io.seek(0)
# #             return send_file(img_io, mimetype='application/zip', as_attachment=True,
# #                              download_name='generated_images.zip')
# #         except Exception as e:
# #             return jsonify({"error": str(e)}), 500
# #     else:
# #         return jsonify({"message": "Sorry, not found. Please include keywords related to rings."}), 400
# #
# #
# # # Run Flask app
# # if __name__ == '__main__':
# #     app.run(port=5000)

from flask import Flask, request, jsonify
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import io
import base64

app = Flask(__name__)

# Load the fine-tuned model
model_path = "/Users/manvi11/Downloads/Dataset/fineTuned"
pipe = StableDiffusionPipeline.from_pretrained(model_path)
pipe = pipe.to("cpu")  # Use CPU since CUDA is not available
seed = 42  # Fixed seed for reproducibility

# Define allowed keywords
allowed_keywords = [
    "engagement", "wedding", "solitaire", "halo", "band", "promise", "cocktail", "eternity",
    "vintage", "designer", "classic", "custom", "birthstone", "anniversary", "stackable", "statement",
    "matching", "gold", "silver", "platinum", "palladium", "titanium", "tungsten", "stainless steel",
    "bronze", "brass", "copper", "diamond", "round cut", "princess cut", "emerald cut", "cushion cut",
    "marquise cut", "asscher cut", "pear cut", "sapphire", "ruby", "emerald", "amethyst", "topaz",
    "garnet", "opal", "aquamarine", "peridot", "tourmaline", "citrine", "sparkling", "brilliant",
    "elegant", "intricate", "minimalist", "bold", "modern", "antique", "handcrafted", "custom-made",
    "unique", "luxurious", "refined", "polished", "textured", "engraved", "filigree", "bezel set",
    "prong set", "channel set", "flush set", "pavé set", "three-stone", "flush fit", "adjustable",
    "casual", "formal", "bridal", "everyday", "high fashion", "artistic", "personalized", "classic",
    "contemporary", "retro", "art deco", "gothic", "romantic", "ring size", "band width", "gemstone setting",
    "craftsmanship", "jewel", "precious metals", "semi-precious stones", "accent stones", "milgrain",
    "inlay", "harmony", "anniversary band", "wedding band", "ring", "rings"
]

@app.route('/')
def home():
    return '''
    <html>
<head>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #1e1e2f;
            color: #fff;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }
        h1 {
            margin-bottom: 20px;
            font-size: 2rem;
        }
        .input-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 20px;
        }
        input[type="text"] {
            width: 350px;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 8px;
            margin-bottom: 10px;
            font-size: 16px;
            background-color: #2b2b3d;
            color: #fff;
        }
        input[type="range"] {
            width: 350px;
            margin-bottom: 10px;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            background-color: #ff7b54;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #ff6b3b;
        }
        #loading {
            display: none;
            font-size: 16px;
            color: #666;
            margin-top: 10px;
        }
        .result-container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        #result {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
            width: 90%;
            max-width: 1200px;
        }
        #result img {
            width: 100%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 10px;
            transition: transform 0.3s;
        }
        #result img:hover {
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <h1>Text-to-Image Generator</h1>
    <div class="input-container">
        <input type="text" id="prompt" placeholder="Enter Prompt (e.g., Solitaire diamond ring for men)">
        <input type="range" id="numImages" min="1" max="10" value="1" oninput="this.nextElementSibling.value = this.value">
        <output>1</output>
        <button onclick="generateImage()">Generate Images</button>
    </div>
    <div id="loading">Loading...</div>
    <div class="result-container">
        <div id="result"></div>
    </div>
    <script>
        async function generateImage() {
            const prompt = document.getElementById('prompt').value;
            const numImages = document.getElementById('numImages').value;
            document.getElementById('loading').style.display = 'block';
            document.getElementById('result').innerHTML = '';
            const response = await fetch('/generate_image', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt: prompt, num_images: numImages })
            });
            document.getElementById('loading').style.display = 'none';
            if (response.ok) {
                const data = await response.json();
                data.images.forEach(imgData => {
                    const img = document.createElement('img');
                    img.src = 'data:image/png;base64,' + imgData;
                    document.getElementById('result').appendChild(img);
                });
            } else {
                const error = await response.json();
                alert('Error: ' + error.message);
            }
        }
    </script>
</body>
</html>

    '''

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.json.get('prompt', '')
    num_images = int(request.json.get('num_images', 1))
    if any(keyword in prompt.lower() for keyword in allowed_keywords):
        try:
            images = []
            generator = torch.manual_seed(seed)
            for _ in range(num_images):
                result = pipe(prompt=prompt)
                img = result.images[0]

                # Convert image to base64
                buffered = io.BytesIO()
                img.save(buffered, format="PNG")
                img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
                images.append(img_base64)

            return jsonify({"images": images})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"message": "Sorry, not found. Please include keywords related to rings."}), 400

if __name__ == '__main__':
    app.run(debug=True)
